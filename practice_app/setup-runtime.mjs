import { mkdir, readFile, rename, stat, unlink, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { createHash, randomUUID } from "node:crypto";
import { RUNTIME_VERSION, RUNTIME_FILES, RUNTIME_DIR, assertLocalRuntime } from "./runtime.mjs";

// Download once during setup. Normal practice loads these files from localhost.
const baseURL = `https://cdn.jsdelivr.net/pyodide/v${RUNTIME_VERSION}/full/`;
await mkdir(RUNTIME_DIR, { recursive: true });
const results = await Promise.allSettled(RUNTIME_FILES.map(async (name) => {
  const target = join(RUNTIME_DIR, name);
  const existing = await stat(target).catch(() => null);
  if (existing?.isFile() && existing.size > 0) return;
  if (existing) throw new Error(`The runtime file ${name} is empty or invalid. Remove it and run setup again.`);
  const url = name === "LICENSE"
    ? `https://raw.githubusercontent.com/pyodide/pyodide/${RUNTIME_VERSION}/LICENSE`
    : `${baseURL}${name}`;
  const response = await fetch(url, { signal: AbortSignal.timeout(120000) });
  if (!response.ok) throw new Error(`Could not download ${name}: HTTP ${response.status}`);
  const data = Buffer.from(await response.arrayBuffer());
  if (!data.length) throw new Error(`Received an empty runtime file: ${name}`);
  const temporary = `${target}.${randomUUID()}.download`;
  try {
    await writeFile(temporary, data, { flag: "wx" });
    await rename(temporary, target);
  } finally {
    await unlink(temporary).catch(() => undefined);
  }
  console.log(`Saved ${name} (${Math.round(data.length / 1024)} KB)`);
}));
const failures = results.filter(result => result.status === "rejected");
if (failures.length) {
  failures.forEach(result => console.error(result.reason.message));
  process.exitCode = 1;
} else {
  await assertLocalRuntime();
  const checksums = {};
  for (const name of RUNTIME_FILES) {
    checksums[name] = createHash("sha256").update(await readFile(join(RUNTIME_DIR, name))).digest("hex");
  }
  await writeFile(join(RUNTIME_DIR, "checksums.json"), `${JSON.stringify(checksums, null, 2)}\n`);
  console.log(`Pyodide ${RUNTIME_VERSION} is ready for local, offline practice.`);
}
