import assert from "node:assert/strict";
import { mkdtemp, mkdir, copyFile, writeFile, readFile, readdir, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve, dirname } from "node:path";
import { pathToFileURL } from "node:url";
import { spawn } from "node:child_process";
import { once } from "node:events";
import test from "node:test";
import { RUNTIME_VERSION, RUNTIME_FILES } from "../runtime.mjs";

test("catalog and local creation preserve content and validate inputs", async (t) => {
  const fixture = await mkdtemp(join(tmpdir(), "practice-lab-test-"));
  const app = join(fixture, "app");
  let child;
  t.after(async () => {
    if (child && child.exitCode === null) { const exited = once(child, "exit"); child.kill(); await exited; }
    assert.equal(dirname(fixture), resolve(tmpdir()));
    assert.ok(fixture.startsWith(join(tmpdir(), "practice-lab-test-")));
    await rm(fixture, { recursive: true, force: true });
  });
  await mkdir(join(app, "dist"), { recursive: true });
  await mkdir(join(fixture, "problems"));
  await mkdir(join(fixture, "problems", "ignored.py"));
  await copyFile(new URL("../server.mjs", import.meta.url), join(app, "server.mjs"));
  await copyFile(new URL("../runtime.mjs", import.meta.url), join(app, "runtime.mjs"));
  await copyFile(new URL("../dist/problem-format.js", import.meta.url), join(app, "dist", "problem-format.js"));
  const runtime = join(app, "dist", "vendor", "pyodide", RUNTIME_VERSION);
  await mkdir(runtime, { recursive: true });
  await Promise.all(RUNTIME_FILES.map(name => writeFile(join(runtime, name), "fixture")));
  await writeFile(join(app, "package.json"), '{"type":"module"}');
  await writeFile(join(app, "dist", "index.html"), "<!doctype html><title>Fixture</title>");
  await writeFile(join(fixture, "problems", "base.py"), '#!/usr/bin/env python\n# coding: utf-8\n"""base.py\nProblem Statement: Base problem\nInterview Difficulty: Easy\n"""\ndef base(\n    value: int,\n) -> int:\n    return value\n');

  child = spawn(process.execPath, [join(app, "server.mjs"), "serve", "--no-browser", "--port", "0"], { stdio: ["ignore", "pipe", "pipe"] });
  const baseURL = await new Promise((resolveURL, reject) => {
    const timeout = setTimeout(() => reject(new Error("Fixture server did not start")), 10000);
    child.once("error", reject);
    child.once("exit", code => reject(new Error(`Fixture server exited: ${code}`)));
    let output = "";
    child.stdout.on("data", chunk => {
      output += chunk;
      const match = output.match(/http:\/\/127\.0\.0\.1:\d+/);
      if (match) { clearTimeout(timeout); resolveURL(match[0]); }
    });
  });
  const post = (body, origin = baseURL) => fetch(`${baseURL}/api/problems`, {
    method: "POST", headers: { "Content-Type": "application/json", Origin: origin }, body: JSON.stringify(body),
  });
  const initial = await (await fetch(`${baseURL}/api/problems`)).json();
  assert.equal(initial.sourceCount, 1);
  assert.equal(initial.problems[0].statement, "Base problem");
  assert.match(initial.problems[0].starterCode, /def base\(value: int,\) -> int:/);
  for (const [name, mime] of [["pyodide.mjs", "text/javascript"], ["pyodide.asm.wasm", "application/wasm"], ["python_stdlib.zip", "application/zip"]]) {
    const runtimeResponse = await fetch(`${baseURL}/vendor/pyodide/${RUNTIME_VERSION}/${name}`);
    assert.equal(runtimeResponse.status, 200);
    assert.ok(runtimeResponse.headers.get("content-type").startsWith(mime));
    assert.equal(await runtimeResponse.text(), "fixture");
  }

  const statement = 'Match """ and \'\'\' delimiters, C:\\new\\test, \\"quoted", and Unicode →.';
  const response = await post({ title: "API & JSON", statement, difficulty: "Easy", starterCode: "def solve():\n    pass", tests: "assert True" });
  assert.equal(response.status, 201);
  const { problem } = await response.json();
  assert.equal(problem.title, "API & JSON");
  assert.equal(problem.statement, statement);
  assert.equal(problem.file, "problems/api_json.py");
  assert.equal(problem.tests, "assert True");
  const spec = JSON.parse(await readFile(join(fixture, "practice_specs", "api_json.json"), "utf8"));
  assert.equal(spec.title, "API & JSON");
  assert.equal((await post({ title: "API & JSON", statement })).status, 409);
  for (const invalid of [null, [], "text", { title: 4 }, { title: "Blank", statement: " " }]) {
    assert.equal((await post(invalid)).status, 400);
  }
  assert.equal((await post({ title: "Foreign", statement: "No" }, "https://example.invalid")).status, 403);
  assert.equal((await fetch(`${baseURL}/%ZZ`)).status, 400);
  assert.equal((await fetch(`${baseURL}/missing.js`)).status, 404);
  assert.equal((await readdir(join(fixture, "problems"))).length, 3);

  const concurrent = await Promise.all(["One", "Two"].map(title => post({ title, statement: title })));
  assert.ok(concurrent.every(result => result.status === 201));
  const catalog = JSON.parse(await readFile(join(app, "dist", "data", "problems.json"), "utf8"));
  assert.equal(catalog.sourceCount, 4);

  const { scanCatalog } = await import(pathToFileURL(join(app, "server.mjs")).href);
  for (const name of ["permute", "permutations"]) {
    await writeFile(join(fixture, "problems", name + ".py"), `"""\nProblem Statement: Permutations\nInterview Difficulty: Medium\n"""\ndef permute(values):\n    return [values]\n`);
  }
  const deduplicated = await scanCatalog();
  assert.equal(deduplicated.sourceFileCount, 6);
  assert.equal(deduplicated.sourceCount, 5);
  assert.deepEqual(deduplicated.problems.find(problem => problem.id === "permutations").aliases, ["permute"]);
  assert.ok(!deduplicated.problems.some(problem => problem.id === "permute"));
  await writeFile(join(fixture, "practice_specs", "base.json"), '{"starter_code":[]}');
  await assert.rejects(scanCatalog(), /starter_code must be text/);
});
