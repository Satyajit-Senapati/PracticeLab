#!/usr/bin/env node

import { createServer } from "node:http";
import { access, mkdir, readFile, readdir, rename, unlink, writeFile } from "node:fs/promises";
import { spawn } from "node:child_process";
import { randomUUID } from "node:crypto";
import { dirname, extname, join, relative, resolve, sep } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { formatProblemSource, METADATA_MARKER } from "./dist/problem-format.js";
import { assertLocalRuntime } from "./runtime.mjs";

const APP_DIR = dirname(fileURLToPath(import.meta.url));
const REPO_DIR = resolve(APP_DIR, "..");
const PROBLEMS_DIR = join(REPO_DIR, "problems");
const DIST_DIR = join(APP_DIR, "dist");
const DATA_FILE = join(DIST_DIR, "data", "problems.json");
const SPECS_DIR = join(REPO_DIR, "practice_specs");
let catalogWriteQueue = Promise.resolve();

const LABELS = [
  "Problem Statement",
  "Interview Difficulty",
  "Commonly Asked By",
  "Concepts Tested",
  "Real-world Use Case",
  "Input Description",
  "Output Description",
  "Example Inputs and Outputs",
  "Constraints",
  "Brute Force Approach",
  "Optimized Approach",
  "Time Complexity",
  "Space Complexity",
  "Step-by-step Dry Run",
  "Edge Cases",
  "Common Mistakes",
  "Follow-up Interview Questions",
  "Alternative Approaches",
  "Expected Output",
  "Key Takeaways",
];

const FIELD_NAMES = new Map([
  ["Problem Statement", "statement"],
  ["Interview Difficulty", "difficulty"],
  ["Commonly Asked By", "companies"],
  ["Concepts Tested", "concepts"],
  ["Real-world Use Case", "realWorldUse"],
  ["Input Description", "input"],
  ["Output Description", "output"],
  ["Example Inputs and Outputs", "examples"],
  ["Constraints", "constraints"],
  ["Brute Force Approach", "bruteForce"],
  ["Optimized Approach", "optimized"],
  ["Time Complexity", "timeComplexity"],
  ["Space Complexity", "spaceComplexity"],
  ["Step-by-step Dry Run", "dryRun"],
  ["Edge Cases", "edgeCases"],
  ["Common Mistakes", "commonMistakes"],
  ["Follow-up Interview Questions", "followUps"],
  ["Alternative Approaches", "alternatives"],
  ["Expected Output", "expectedOutput"],
  ["Key Takeaways", "takeaways"],
]);

const ACRONYMS = new Map([
  ["bst", "BST"],
  ["dfs", "DFS"],
  ["bfs", "BFS"],
  ["lru", "LRU"],
  ["ii", "II"],
  ["iii", "III"],
  ["iv", "IV"],
  ["2d", "2D"],
]);

function extractModuleDocstring(source) {
  source = source.replace(/^\uFEFF/, "").replace(/\r\n/g, "\n");
  const generated = source.startsWith(METADATA_MARKER);
  if (generated) source = source.slice(METADATA_MARKER.length);
  const opening = source.match(/^\s*(?:#[^\n]*\n\s*)*(?:[rRuU]{0,2})?("""|''')/);
  if (!opening) {
    const trailing = findTrailingMetadataDocstring(source);
    if (!trailing) return { docstring: "", solution: source.trim() };
    return {
      docstring: trailing.content.replace(/\r\n/g, "\n").trim(),
      solution: source.slice(0, trailing.start).trim(),
    };
  }

  const quote = opening[1];
  const contentStart = opening[0].length;
  let contentEnd = source.indexOf(quote, contentStart);
  while (contentEnd >= 0) {
    let backslashes = 0;
    for (let index = contentEnd - 1; source[index] === "\\"; index--) backslashes++;
    if (backslashes % 2 === 0) break;
    contentEnd = source.indexOf(quote, contentEnd + 1);
  }
  if (contentEnd < 0) {
    const unfinished = source.slice(contentStart).replace(/(?:\r?\n)?(?:""|'')\s*$/, "");
    return { docstring: unfinished.replace(/\r\n/g, "\n").trim(), solution: "" };
  }

  return {
    docstring: (generated
      ? source.slice(contentStart, contentEnd).replace(/\\([\\"])/g, "$1")
      : source.slice(contentStart, contentEnd)).trim(),
    solution: source.slice(contentEnd + quote.length).replace(/^\s+/, "").trimEnd(),
  };
}

function findTrailingMetadataDocstring(source) {
  const match = source.match(/(?:^|\r?\n)[rRuU]{0,2}("""|''')([A-Za-z0-9_]+\.py\r?\n[\s\S]*?Problem Statement:[\s\S]*?)\1\s*$/);
  return match ? { content: match[2], start: match.index } : null;
}

function parseMetadata(docstring) {
  const result = {};
  let currentLabel = null;
  const buckets = new Map();
  const labelPattern = new RegExp(`^(${LABELS.map(escapeRegExp).join("|")}):\\s*(.*)$`);

  for (const line of docstring.split("\n")) {
    const match = line.match(labelPattern);
    if (match) {
      currentLabel = match[1];
      buckets.set(currentLabel, [match[2]]);
    } else if (currentLabel) {
      buckets.get(currentLabel).push(line);
    }
  }

  for (const [label, fieldName] of FIELD_NAMES) {
    result[fieldName] = (buckets.get(label) ?? []).join("\n").trim();
  }
  return result;
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function humanize(stem) {
  return stem
    .split("_")
    .filter(Boolean)
    .map((word) => ACRONYMS.get(word.toLowerCase()) ?? `${word[0].toUpperCase()}${word.slice(1).toLowerCase()}`)
    .join(" ");
}

function splitList(value) {
  return value
    .split(/,|\n/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function inferTopic(stem, concepts) {
  const text = `${stem} ${concepts}`.toLowerCase();
  const rules = [
    ["Python", /closure|decorator|descriptor|metaclass|iterator|generator|comprehension|garbage|memory|magic method|abstract|context manager|namedtuple|protocol|typing|lambda|variable|operator|if_else|loop|function|enum/],
    ["Design", /design_|cache|hashmap|randomized set|hit counter|snake game/],
    ["Linked Lists", /linked.?list|list node|random pointer|sort_list|rotate_list|partition_list|reorder_list/],
    ["Trees", /binary tree|binary_tree|\bbst\b|tree traversal|tree node|trie/],
    ["Graphs", /graph|island|course schedule|word ladder|genetic mutation|connected component/],
    ["Dynamic Programming", /dynamic programming|memoization|coin change|word break|subsequence|decode ways|unique paths|climbing stairs/],
    ["Backtracking", /backtrack|n_queens|permutation|combination|subsets|word search|palindrome partition/],
    ["Stacks & Queues", /stack|queue|parentheses|calculator|polish notation/],
    ["Heaps", /heap|priority queue|kth largest|median from data stream/],
    ["Intervals", /interval|meeting room/],
    ["Searching & Sorting", /binary search|search_|sort|rotated sorted|median sorted/],
    ["Strings", /string|substring|anagram|palindrome|word_|text justification|regex|roman|parentheses/],
    ["Arrays", /array|matrix|sum|duplicate|stock|sliding window|subarray|container|rain water|spiral/],
    ["Math", /prime|pow_|bit|number|integer|arithmetic/],
  ];
  return rules.find(([, pattern]) => pattern.test(text))?.[0] ?? "General";
}

function findEntrypoints(solution) {
  const entries = [];
  const pattern = /^(?:(async)\s+)?(def|class)\s+([A-Za-z_]\w*)/gm;
  for (const match of solution.matchAll(pattern)) {
    if (match[3] === "main" || match[3].startsWith("_")) continue;
    entries.push({ name: match[3], type: match[2] === "def" ? "function" : "class" });
  }
  return entries;
}

function makeStarter(title, solution, entries, stem, examples) {
  const functions = entries.filter((entry) => entry.type === "function");
  const firstFunction = functions.find((entry) => entry.name === stem || entry.name === `is_${stem}`)
    ?? functions.find((entry) => new RegExp(`\\b${escapeRegExp(entry.name)}\\s*\\(`).test(examples))
    ?? functions[0];
  const firstClass = entries.find((entry) => entry.type === "class" && !/^(?:Node|TreeNode|ListNode)$/.test(entry.name))
    ?? entries.find((entry) => entry.type === "class");
  let skeleton = "";

  if (firstFunction) {
    const escapedName = escapeRegExp(firstFunction.name);
    const headerMatch = solution.match(new RegExp(`^(?:async\\s+)?def\\s+${escapedName}\\s*\\(([\\s\\S]*?)\\)\\s*(?:->\\s*([^:\\n]+))?:`, "m"));
    if (headerMatch) {
      const params = headerMatch[1].trim().replace(/\s*\n\s*/g, " ");
      const returnType = headerMatch[2]?.trim();
      const prefix = headerMatch[0].startsWith("async") ? "async " : "";
      skeleton = `${prefix}def ${firstFunction.name}(${params})${returnType ? ` -> ${returnType}` : ""}:\n    raise NotImplementedError\n`;
    } else {
      skeleton = `def ${firstFunction.name}(*args, **kwargs):\n    raise NotImplementedError\n`;
    }
  } else if (firstClass) {
    skeleton = `class ${firstClass.name}:\n    pass\n`;
  }

  return `# ${title}\n# Build your solution, then use the Tests panel for assertions.\n\nfrom __future__ import annotations\n\n${skeleton || "# Write your solution here.\n"}`;
}

function makeTests(examples) {
  const lines = examples.split("\n").filter(Boolean).slice(0, 5);
  const exampleComments = lines.length
    ? `\n# Examples from the prompt:\n${lines.map((line) => `# ${line}`).join("\n")}`
    : "";
  return `# Add assertions or print calls here.${exampleComments}\n`;
}

async function readSpec(stem) {
  try {
    const spec = JSON.parse(await readFile(join(SPECS_DIR, `${stem}.json`), "utf8"));
    if (!spec || typeof spec !== "object" || Array.isArray(spec)) throw new Error("Expected a JSON object.");
    for (const key of ["title", "difficulty", "category", "starter_code", "tests"]) {
      if (key in spec && typeof spec[key] !== "string") throw new Error(`${key} must be text.`);
    }
    return spec;
  } catch (error) {
    if (error.code === "ENOENT") return {};
    throw new Error(`Invalid practice spec for ${stem}: ${error.message}`);
  }
}

async function problemFromFile(fileName) {
  const stem = fileName.slice(0, -3);
  const source = await readFile(join(PROBLEMS_DIR, fileName), "utf8");
  const { docstring, solution } = extractModuleDocstring(source);
  const metadata = parseMetadata(docstring);
  const spec = await readSpec(stem);
  const title = spec.title ?? humanize(stem);
  const entries = findEntrypoints(solution);
  const difficulty = spec.difficulty || metadata.difficulty || "Unrated";
  const topic = spec.category ?? inferTopic(stem, metadata.concepts);

  return {
    id: stem.toLowerCase(),
    file: `problems/${fileName}`,
    title,
    difficulty,
    topic,
    concepts: splitList(metadata.concepts),
    companies: splitList(metadata.companies),
    statement: metadata.statement,
    realWorldUse: metadata.realWorldUse,
    input: metadata.input,
    output: metadata.output,
    examples: metadata.examples,
    constraints: metadata.constraints,
    bruteForce: metadata.bruteForce,
    optimized: metadata.optimized,
    timeComplexity: metadata.timeComplexity,
    spaceComplexity: metadata.spaceComplexity,
    dryRun: metadata.dryRun,
    edgeCases: metadata.edgeCases,
    commonMistakes: metadata.commonMistakes,
    followUps: metadata.followUps,
    alternatives: metadata.alternatives,
    expectedOutput: metadata.expectedOutput,
    takeaways: metadata.takeaways,
    entrypoints: entries,
    solutionStatus: solution.trim() ? "available" : "missing",
    solution,
    starterCode: spec.starter_code ?? makeStarter(title, solution, entries, stem, metadata.examples),
    tests: spec.tests ?? makeTests(metadata.examples),
  };
}

export async function scanCatalog() {
  const fileNames = (await readdir(PROBLEMS_DIR, { withFileTypes: true }))
    .filter((entry) => entry.isFile() && entry.name.toLowerCase().endsWith(".py"))
    .map((entry) => entry.name)
    .sort((a, b) => a.localeCompare(b));
  const problems = await Promise.all(fileNames.map(problemFromFile));
  problems.sort((a, b) => a.title.localeCompare(b.title));

  return { sourceCount: problems.length, problems };
}

export async function buildCatalog() {
  catalogWriteQueue = catalogWriteQueue
    .catch(() => undefined)
    .then(async () => {
      const catalog = await scanCatalog();
      await mkdir(dirname(DATA_FILE), { recursive: true });
      await atomicWrite(DATA_FILE, `${JSON.stringify(catalog, null, 2)}\n`);
      return catalog;
    });
  return catalogWriteQueue;
}

async function atomicWrite(filePath, content) {
  const suffix = `${process.pid}.${randomUUID()}`;
  const temporaryPath = `${filePath}.${suffix}.tmp`;
  const backupPath = `${filePath}.${suffix}.bak`;
  await writeFile(temporaryPath, content, "utf8");
  let hasBackup = false;
  try {
    await rename(filePath, backupPath);
    hasBackup = true;
  } catch (error) {
    if (error.code !== "ENOENT") {
      await unlink(temporaryPath).catch(() => undefined);
      throw error;
    }
  }
  try {
    await rename(temporaryPath, filePath);
    if (hasBackup) await unlink(backupPath).catch(() => undefined);
  } catch (error) {
    if (hasBackup) await rename(backupPath, filePath).catch(() => undefined);
    await unlink(temporaryPath).catch(() => undefined);
    throw error;
  }
}

function slugify(value) {
  const slug = value
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .slice(0, 80);
  return /^(?:con|prn|aux|nul|com[1-9]|lpt[1-9])$/i.test(slug) ? `${slug}_problem` : slug;
}

function clean(value, maxLength = 20_000) {
  return String(value ?? "").replace(/\r\n/g, "\n").trim().slice(0, maxLength);
}

async function createProblem(payload) {
  if (!payload || typeof payload !== "object" || Array.isArray(payload) ||
      Object.values(payload).some((value) => typeof value !== "string")) {
    const error = new Error("Problem details must be a JSON object containing text fields.");
    error.statusCode = 400;
    throw error;
  }
  const title = clean(payload.title, 120);
  const statement = clean(payload.statement);
  const slug = slugify(payload.slug || title);
  if (!title || !statement || !slug) {
    const error = new Error("Title and problem statement are required.");
    error.statusCode = 400;
    throw error;
  }

  const filePath = join(PROBLEMS_DIR, `${slug}.py`);
  const fields = [
    [`${slug}.py`, ""],
    ["Problem Statement", statement],
    ["Interview Difficulty", clean(payload.difficulty, 20) || "Medium"],
    ["Concepts Tested", clean(payload.concepts, 500) || clean(payload.topic, 100)],
    ["Input Description", clean(payload.input)],
    ["Output Description", clean(payload.output)],
    ["Example Inputs and Outputs", clean(payload.examples)],
    ["Constraints", clean(payload.constraints)],
    ["Expected Output", clean(payload.expectedOutput)],
    ["Key Takeaways", clean(payload.takeaways)],
  ];
  const docstring = fields
    .filter(([label, value], index) => index === 0 || value)
    .map(([label, value], index) => (index === 0 ? label : `${label}:\n${value}`))
    .join("\n\n");
  const solution = clean(payload.solution, 100_000);
  const source = formatProblemSource(docstring, solution);
  const spec = { title };
  const starterCode = clean(payload.starterCode, 100_000);
  const tests = clean(payload.tests, 100_000);
  const category = clean(payload.topic, 100);
  if (starterCode) spec.starter_code = starterCode;
  if (tests) spec.tests = tests;
  if (category) spec.category = category;
  const specPath = join(SPECS_DIR, `${slug}.json`);
  const writesSpec = Object.keys(spec).length > 0;

  await ensureAvailable(filePath, `problems/${slug}.py already exists. Choose a different title or filename.`);
  if (writesSpec) await ensureAvailable(specPath, `practice_specs/${slug}.json already exists.`);

  const createdPaths = [];
  try {
    await mkdir(PROBLEMS_DIR, { recursive: true });
    await writeFile(filePath, source, { encoding: "utf8", flag: "wx" });
    createdPaths.push(filePath);
    if (writesSpec) {
      await mkdir(SPECS_DIR, { recursive: true });
      await writeFile(specPath, `${JSON.stringify(spec, null, 2)}\n`, { encoding: "utf8", flag: "wx" });
      createdPaths.push(specPath);
    }
    const catalog = await buildCatalog();
    return catalog.problems.find((problem) => problem.id === slug);
  } catch (error) {
    await Promise.allSettled(createdPaths.reverse().map((createdPath) => unlink(createdPath)));
    if (error.code === "EEXIST") {
      const conflict = new Error(`problems/${slug}.py or its practice spec was created by another request. Try a different title.`);
      conflict.statusCode = 409;
      throw conflict;
    }
    throw error;
  }
}

async function ensureAvailable(filePath, message) {
  try {
    await access(filePath);
  } catch (error) {
    if (error.code === "ENOENT") return;
    throw error;
  }
  const conflict = new Error(message);
  conflict.statusCode = 409;
  throw conflict;
}

async function readJsonBody(request) {
  const chunks = [];
  let size = 0;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > 400_000) {
      const error = new Error("Request is too large.");
      error.statusCode = 413;
      throw error;
    }
    chunks.push(chunk);
  }
  try {
    return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}");
  } catch {
    const error = new Error("Request body must be valid JSON.");
    error.statusCode = 400;
    throw error;
  }
}

function sendJson(response, statusCode, payload) {
  response.writeHead(statusCode, {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
  });
  response.end(JSON.stringify(payload));
}

const CONTENT_TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".wasm": "application/wasm",
  ".zip": "application/zip",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
};

async function serveStatic(pathname, response) {
  const normalizedPath = pathname === "/" ? "/index.html" : pathname;
  const filePath = resolve(DIST_DIR, `.${normalizedPath}`);
  if (filePath !== DIST_DIR && !filePath.startsWith(`${DIST_DIR}${sep}`)) {
    sendJson(response, 403, { error: "Invalid path." });
    return;
  }

  try {
    const body = await readFile(filePath);
    response.writeHead(200, {
      "Content-Type": CONTENT_TYPES[extname(filePath)] ?? "application/octet-stream",
      "Cache-Control": extname(filePath) === ".html" ? "no-cache" : "public, max-age=300",
      "X-Content-Type-Options": "nosniff",
    });
    response.end(body);
  } catch (error) {
    if (error.code === "ENOENT" || error.code === "EISDIR") {
      sendJson(response, 404, { error: "Not found." });
      return;
    }
    throw error;
  }
}

async function requestHandler(request, response) {
  try {
    const url = new URL(request.url, "http://127.0.0.1");
    if (request.method === "GET" && url.pathname === "/api/health") {
      sendJson(response, 200, { mode: "local", canCreateProblems: true });
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/problems") {
      sendJson(response, 200, await scanCatalog());
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/problems") {
      requireSameOriginJson(request);
      sendJson(response, 201, { problem: await createProblem(await readJsonBody(request)) });
      return;
    }
    if (!request.method || !["GET", "HEAD"].includes(request.method)) {
      sendJson(response, 405, { error: "Method not allowed." });
      return;
    }
    let pathname;
    try { pathname = decodeURIComponent(url.pathname); }
    catch {
      sendJson(response, 400, { error: "Invalid URL encoding." });
      return;
    }
    await serveStatic(pathname, response);
  } catch (error) {
    sendJson(response, error.statusCode ?? 500, {
      error: error.statusCode ? error.message : "Something went wrong while serving the practice app.",
    });
    if (!error.statusCode) console.error(error);
  }
}

function requireSameOriginJson(request) {
  const contentType = String(request.headers["content-type"] ?? "").split(";", 1)[0].trim().toLowerCase();
  if (contentType !== "application/json") {
    const error = new Error("Content-Type must be application/json.");
    error.statusCode = 415;
    throw error;
  }

  const origin = request.headers.origin;
  const host = request.headers.host;
  const localPort = request.socket.localPort;
  const allowedHosts = new Set([`127.0.0.1:${localPort}`, `localhost:${localPort}`]);
  let parsedOrigin;
  try {
    parsedOrigin = new URL(origin);
  } catch {
    // A browser request from the app always supplies a valid Origin header.
  }
  if (!origin || !host || !allowedHosts.has(host.toLowerCase()) || parsedOrigin?.protocol !== "http:" || parsedOrigin.host.toLowerCase() !== host.toLowerCase()) {
    const error = new Error("Problem creation is only allowed from this local app.");
    error.statusCode = 403;
    throw error;
  }
}

function openBrowser(url) {
  const commands = {
    win32: ["cmd", ["/c", "start", "", url]],
    darwin: ["open", [url]],
    linux: ["xdg-open", [url]],
  };
  const command = commands[process.platform];
  if (!command) return;
  const child = spawn(command[0], command[1], { detached: true, stdio: "ignore", windowsHide: true });
  child.unref();
}

function optionValue(name, fallback) {
  const index = process.argv.indexOf(name);
  return index >= 0 && process.argv[index + 1] ? process.argv[index + 1] : fallback;
}

async function main() {
  const command = process.argv[2] && !process.argv[2].startsWith("--") ? process.argv[2] : "serve";
  const catalog = await buildCatalog();
  if (command === "build") {
    console.log(`Indexed ${catalog.sourceCount} problems in ${relative(REPO_DIR, DATA_FILE)}.`);
    return;
  }
  if (command !== "serve") {
    console.error("Usage: node app/server.mjs [serve|build] [--port 8765] [--no-browser]");
    process.exitCode = 1;
    return;
  }

  await assertLocalRuntime();

  const port = Number.parseInt(optionValue("--port", "8765"), 10);
  const host = "127.0.0.1";
  const server = createServer(requestHandler);
  server.listen(port, host, () => {
    const address = server.address();
    const url = `http://${host}:${address.port}`;
    console.log(`Practice Lab is ready locally at ${url}`);
    console.log(`Indexed ${catalog.sourceCount} problems. Press Ctrl+C to stop.`);
    if (!process.argv.includes("--no-browser")) openBrowser(url);
  });
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
