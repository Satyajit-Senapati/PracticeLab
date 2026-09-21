import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { scanCatalog } from "./server.mjs";
import { assertLocalRuntime } from "./runtime.mjs";

const appDir = dirname(fileURLToPath(import.meta.url));
const distDir = resolve(appDir, "dist");

for (const file of ["server.mjs", "validate.mjs", "runtime.mjs", "setup-runtime.mjs", "dist/app.js", "dist/python-worker.js", "dist/problem-format.js"]) {
  const result = spawnSync(process.execPath, ["--check", resolve(appDir, file)], { encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr || `${file} did not pass the JavaScript syntax check.`);
}

await assertLocalRuntime();

const [html, savedCatalog, liveCatalog] = await Promise.all([
  readFile(resolve(distDir, "index.html"), "utf8"),
  readFile(resolve(distDir, "data/problems.json"), "utf8").then(JSON.parse),
  scanCatalog(),
]);

assert.deepEqual(savedCatalog, liveCatalog, "The static catalog is stale. Run the build command.");
assert.ok(savedCatalog.sourceCount > 0, "The catalog is empty.");
assert.equal(savedCatalog.sourceCount, savedCatalog.problems.length, "The catalog count is incorrect.");
assert.equal(new Set(savedCatalog.problems.map((problem) => problem.id)).size, savedCatalog.problems.length, "Problem ids must be unique.");

for (const problem of savedCatalog.problems) {
  assert.ok(problem.id && problem.file && problem.title, "Every problem needs an id, file, and title.");
  assert.match(problem.file, /^problems\/[A-Za-z0-9_]+\.py$/, `${problem.file} must point into problems/.`);
  assert.ok(problem.statement, `${problem.file} is missing its parsed problem statement.`);
  assert.ok(problem.difficulty, `${problem.file} is missing its parsed difficulty.`);
  assert.ok(problem.starterCode, `${problem.file} is missing starter code.`);
}

const localReferences = [...html.matchAll(/(?:src|href)="([^"]+)"/g)]
  .map((match) => match[1])
  .filter((reference) => !/^(?:https?:|#|data:)/.test(reference));
for (const reference of localReferences) await access(resolve(distDir, reference));

for (const requiredId of ["problem-list", "problem-content", "code-editor", "tests-editor", "console-output", "add-problem-dialog"]) {
  assert.match(html, new RegExp(`id="${requiredId}"`), `The required #${requiredId} interface is missing.`);
}

const missingSolutions = savedCatalog.problems.filter((problem) => problem.solutionStatus === "missing").length;
console.log(`Validated ${savedCatalog.sourceCount} problems, ${localReferences.length} local assets, and all JavaScript entrypoints (${missingSolutions} reference solutions pending).`);
