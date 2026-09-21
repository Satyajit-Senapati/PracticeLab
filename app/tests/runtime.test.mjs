import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import test from "node:test";
import { RUNTIME_DIR, RUNTIME_FILES, assertLocalRuntime } from "../runtime.mjs";

test("bundled Python runtime starts and runs standard-library code without fetching", async () => {
  await assertLocalRuntime();
  const checksums = JSON.parse(await readFile(join(RUNTIME_DIR, "checksums.json"), "utf8"));
  for (const name of RUNTIME_FILES) {
    const actual = createHash("sha256").update(await readFile(join(RUNTIME_DIR, name))).digest("hex");
    assert.equal(actual, checksums[name], `Runtime file changed: ${name}`);
  }

  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => { throw new Error("Network access is disabled in this test"); };
  try {
    const { loadPyodide } = await import(pathToFileURL(join(RUNTIME_DIR, "pyodide.mjs")).href);
    const python = await loadPyodide({ indexURL: RUNTIME_DIR });
    assert.equal(python.runPython("sum([1, 2, 3])"), 6);
    assert.equal(await python.runPythonAsync(`
import collections
import dataclasses
import json
import math

@dataclasses.dataclass
class Example:
    value: int

example = Example(math.factorial(5))
assert collections.Counter("aba")["a"] == 2
json.dumps({"result": example.value})
`), '{"result": 120}');
  } finally {
    globalThis.fetch = originalFetch;
  }
});
