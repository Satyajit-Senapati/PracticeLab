import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import test from "node:test";

const source = (await readFile(new URL("../dist/app.js", import.meta.url), "utf8"))
  .replace(/\r\n/g, "\n")
  .replace(/^import .*;\n/m, "")
  .replaceAll("import.meta.url", JSON.stringify(import.meta.url))
  .replace(/\nstart\(\);\s*$/, "");

function harness({ storage = {}, failStorage = false, Worker } = {}) {
  const nodes = new Map();
  const timers = new Map();
  let nextTimer = 0;
  const node = (selector) => {
    if (!nodes.has(selector)) nodes.set(selector, {
      value: "", textContent: "", innerHTML: "", dataset: {}, disabled: false, hidden: false,
      scrollTop: 0, scrollLeft: 0, attributes: {},
      classList: { toggle() {}, add() {}, remove() {} }, style: { setProperty() {} },
      setAttribute(key, value) { this.attributes[key] = value; },
      querySelector: node, querySelectorAll: () => [], focus() {}, append() {}, remove() {},
      addEventListener() {},
    });
    return nodes.get(selector);
  };
  const context = vm.createContext({
    document: { querySelector: node, querySelectorAll: () => [], createElement: () => node("toast"), addEventListener() {} },
    window: { setTimeout(fn, delay) { timers.set(++nextTimer, { fn, delay }); return nextTimer; }, clearTimeout(id) { timers.delete(id); } },
    localStorage: {
      getItem(key) { return storage[key] ?? null; },
      setItem(key, value) { if (failStorage) throw new Error("QuotaExceededError"); storage[key] = value; },
    },
    location: { hash: "" }, history: { replaceState() {} }, CSS: { escape: (value) => value },
    Worker, URL, AbortSignal, console,
  });
  vm.runInContext(source, context);
  const run = (code) => vm.runInContext(code, context);
  run(`state.problems = ["alpha", "beta"].map(id => ({ id, title: id, file: "problems/" + id + ".py",
    difficulty: "Easy", topic: "Arrays", concepts: [], starterCode: "# starter", tests: "# tests" }));
    state.filtered = state.problems; selectProblem("alpha");`);
  return { run, node, timers, context, storage };
}

test("reopening the selected problem preserves edits before autosave", () => {
  const { run, node } = harness();
  node("#code-editor").value = "print('fresh draft')";
  run("saveActiveDraft(); selectProblem('alpha');");
  assert.equal(node("#code-editor").value, "print('fresh draft')");
  assert.equal(run("state.progress.alpha.code"), "print('fresh draft')");
});

test("storage failures do not stop execution or leave Run disabled", async () => {
  const { run, node } = harness({ failStorage: true });
  node("#code-editor").value = "print(42)";
  run("state.runner = { run: async () => ({stdout:'42', stderr:'', exitCode:0, durationMs:1}) };");
  const result = await run("runCode()");
  assert.equal(result.ok, true);
  assert.equal(run("state.running"), false);
  assert.equal(node("#run-button").disabled, false);
  assert.match(node("#autosave-status").textContent, /Unsaved/);
});

test("results stay with their problem when the selection changes during a run", async () => {
  const { run, node } = harness();
  node("#code-editor").value = "print('alpha output')";
  run("state.runner = { run: () => new Promise(resolve => globalThis.finishRun = resolve) };");
  const running = run("runCode()");
  run("selectProblem('beta');");
  assert.equal(node("#run-button").disabled, true);
  run("finishRun({stdout:'alpha output', stderr:'', exitCode:0, durationMs:3});");
  await running;
  assert.doesNotMatch(node("#console-output").textContent, /alpha output/);
  run("selectProblem('alpha');");
  assert.equal(node("#console-output").textContent, "alpha output");
  assert.equal(node("#run-button").disabled, false);
});

test("corrupt storage shapes and malformed URL hashes are recoverable", () => {
  const { run, context } = harness({ storage: {
    "python-practice-lab:custom:v1": '[null,42,{"id":"missing title"}]',
    "python-practice-lab:progress:v1": '["wrong shape"]',
  } });
  assert.equal(run("state.customProblems.length"), 0);
  context.location.hash = "#%";
  assert.equal(run("requestedProblemId()"), "");
});

test("topic refresh preserves the selected filter", () => {
  const { run, node } = harness();
  run("state.topic = 'Arrays'; populateTopics();");
  assert.equal(node("#topic-filter").value, "Arrays");
  run("state.topic = 'Removed'; populateTopics();");
  assert.equal(run("state.topic"), "all");
});

test("whitespace-only problems fail before a download or write", async () => {
  const { run, context } = harness();
  context.form = new Map([["title", "Title"], ["statement", "   "]]);
  await assert.rejects(run("submitProblem(form)"), /statement are required/);
});

test("new problems require the local server instead of browser-only storage", async () => {
  const { run, context, storage } = harness();
  context.form = new Map([["title", "Local problem"], ["statement", "Return the sum."]]);
  await assert.rejects(run("submitProblem(form)"), /Start the local server/);
  assert.equal(run("state.customProblems.length"), 0);
  assert.equal(Object.hasOwn(storage, "python-practice-lab:custom:v1"), false);
});

test("worker crashes clear old timers and timeout recovery settles before retry", async () => {
  const workers = [];
  class FakeWorker {
    constructor() { this.listeners = {}; workers.push(this); }
    addEventListener(type, fn) { this.listeners[type] = fn; }
    terminate() { this.terminated = true; }
    postMessage() {}
    ready() { this.listeners.message({ data: { type: "status", status: "ready" } }); }
  }
  const { run, timers } = harness({ Worker: FakeWorker });
  run("globalThis.runner = new PythonRunner(() => {});");
  workers[0].ready();
  const failed = run("runner.run('pass', '')");
  await Promise.resolve();
  workers[0].listeners.error({ message: "crashed" });
  await assert.rejects(failed, /worker failed/);
  assert.equal([...timers.values()].filter(timer => timer.delay === 10000).length, 0);
  const retry = run("runner.run('pass', '')");
  workers[1].ready();
  await Promise.resolve();
  const timeout = [...timers.values()].find(timer => timer.delay === 10000);
  assert.ok(timeout);
  timeout.fn();
  await assert.rejects(retry, /10 seconds/);
  assert.equal(workers.length, 2, "Timeout must not synchronously create another worker");
  assert.equal(run("runner.failed"), true);
});
