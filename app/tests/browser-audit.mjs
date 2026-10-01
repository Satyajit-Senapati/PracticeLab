// Optional real-browser audit. Requires Node 24+ and an installed Chrome.
// Run: node app/tests/browser-audit.mjs
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { access, mkdtemp, readFile, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function waitFor(fn, label, timeout = 30000) {
  const end = Date.now() + timeout;
  while (Date.now() < end) {
    try {
      const result = await fn();
      if (result) return result;
    } catch (error) {
      if (!/navigated|context was destroyed|Cannot find context/i.test(error.message)) throw error;
    }
    await pause(100);
  }
  throw new Error("Timed out: " + label);
}
const profile = await mkdtemp(join(tmpdir(), "practice-lab-browser-"));
console.log("Audit screenshots: " + profile);
const chromePath = process.env.CHROME_PATH ?? "C:/Program Files/Google/Chrome/Application/chrome.exe";
await access(chromePath);
const server = spawn(process.execPath, [fileURLToPath(new URL("../server.mjs", import.meta.url)), "serve", "--port", "0", "--no-browser"], {
  stdio: ["ignore", "pipe", "pipe"], windowsHide: true,
});
let serverOutput = "";
let browser;
let socket;
const pending = new Map();
const errors = [];
let sequence = 0;
server.stdout.on("data", chunk => { serverOutput += chunk; });
server.stderr.on("data", chunk => { serverOutput += chunk; });
try {
  const url = await waitFor(() => {
    if (server.exitCode !== null) throw new Error(serverOutput);
    return serverOutput.match(/http:\/\/127\.0\.0\.1:\d+/)?.[0];
  }, "local server");
  browser = spawn(chromePath, [
    "--headless=new", "--disable-gpu", "--no-first-run", "--disable-extensions",
    "--disable-background-networking", "--remote-debugging-port=0",
    "--user-data-dir=" + profile, url,
  ], { stdio: "ignore", windowsHide: true });
  const port = await waitFor(async () => {
    try { return (await readFile(join(profile, "DevToolsActivePort"), "utf8")).split("\n")[0]; }
    catch { return null; }
  }, "isolated browser");
  const page = await waitFor(async () => {
    const pages = await (await fetch("http://127.0.0.1:" + port + "/json/list")).json();
    return pages.find(item => item.type === "page" && item.url.startsWith(url));
  }, "Practice Lab tab");
  socket = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    socket.addEventListener("open", resolve, { once: true });
    socket.addEventListener("error", reject, { once: true });
  });
  socket.addEventListener("message", event => {
    const message = JSON.parse(event.data);
    if (message.method === "Runtime.exceptionThrown") errors.push(message.params.exceptionDetails);
    if (pending.has(message.id)) {
      const { resolve, reject, timer } = pending.get(message.id);
      clearTimeout(timer);
      pending.delete(message.id);
      if (message.error) reject(new Error(JSON.stringify(message.error)));
      else resolve(message.result);
    }
  });
  function cdp(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = ++sequence;
      const timer = setTimeout(() => {
        pending.delete(id);
        reject(new Error("Timed out: " + method));
      }, 60000);
      pending.set(id, { resolve, reject, timer });
      socket.send(JSON.stringify({ id, method, params }));
    });
  }
  async function evaluate(fn, ...args) {
    const result = await cdp("Runtime.evaluate", {
      expression: "(" + fn.toString() + ")(..." + JSON.stringify(args) + ")",
      awaitPromise: true, returnByValue: true, userGesture: true,
    });
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    return result.result.value;
  }
  await cdp("Runtime.enable");
  await cdp("Page.enable");
  const catalog = await (await fetch(url + "/api/problems")).json();
  const expectedCount = catalog.problems.length;
  await waitFor(() => evaluate(count => document.querySelector("#problem-count")?.textContent === String(count), expectedCount), "catalog");
  const layouts = [];
  for (const width of [320, 390, 768, 1024, 1180, 1181, 1440, 1920]) {
    const height = ({ 320: 568, 390: 844, 768: 1024, 1024: 768 })[width] ?? 900;
    await cdp("Emulation.setDeviceMetricsOverride", { width, height, deviceScaleFactor: 1, mobile: width < 700 });
    const layout = await evaluate(() => {
      const controls = ["#add-problem-button", "#status-filter", '[data-filter="Hard"]', "#jump-to-editor", "#run-button"];
      return {
        width: innerWidth, scrollWidth: document.documentElement.scrollWidth,
        controls: controls.map(selector => {
          const rect = document.querySelector(selector).getBoundingClientRect();
          return { selector, left: rect.left, right: rect.right, height: rect.height };
        }),
      };
    });
    assert.ok(layout.scrollWidth <= width, JSON.stringify(layout));
    for (const control of layout.controls) {
      assert.ok(control.left >= 0 && control.right <= width + 1 && control.height > 0, JSON.stringify({ width, control }));
      if (width < 700) assert.ok(control.height >= 44, JSON.stringify({ width, control }));
    }
    await evaluate(() => document.querySelector("#add-problem-button").click());
    const dialog = await evaluate(() => {
      const dialog = document.querySelector("#add-problem-dialog");
      const rect = dialog.getBoundingClientRect();
      const result = { open: dialog.open, left: rect.left, right: rect.right, top: rect.top, bottom: rect.bottom };
      dialog.close();
      return result;
    });
    assert.ok(dialog.open && dialog.left >= 0 && dialog.right <= width && dialog.top >= 0 && dialog.bottom <= height + 1, JSON.stringify(dialog));
    if ([390, 768, 1440].includes(width)) {
      const shot = await cdp("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
      await writeFile(join(profile, "screen-" + width + ".png"), Buffer.from(shot.data, "base64"));
    }
    layouts.push({ width, height, fits: true });
  }
  const flow = await evaluate(async expectedCount => {
    const $ = selector => document.querySelector(selector);
    const input = element => element.dispatchEvent(new Event("input", { bubbles: true }));
    const check = (condition, message) => { if (!condition) throw new Error(message); };
    const wait = async predicate => {
      const end = Date.now() + 45000;
      while (!predicate()) {
        if (Date.now() > end) throw new Error("Execution timed out");
        await new Promise(resolve => setTimeout(resolve, 100));
      }
    };
    $("#problem-search").value = "no matching exercise 12345"; input($("#problem-search"));
    check(!$("#empty-list").hidden, "Empty state");
    $("#clear-filters").click();
    check($("#problem-list").children.length === expectedCount, "Clear filters");
    $("#problem-search").value = "balanced brackets"; input($("#problem-search"));
    $("#problem-list [data-problem-id]").click();
    check($("#problem-title").textContent === "Balanced Brackets", "Select new exercise");
    $("#jump-to-editor").click();
    check(document.activeElement.id === "code-editor", "Editor jump focus");
    const response = await fetch("/api/problems");
    const catalog = await response.json();
    const problem = catalog.problems.find(item => item.id === "balanced_brackets");
    $("#code-editor").value = problem.solution; input($("#code-editor"));
    $("#tests-editor").value = problem.tests; input($("#tests-editor"));
    $("#run-button").click();
    await wait(() => !$("#run-button").disabled);
    check($("#console-output").textContent.includes("Example checks passed."), "Reference execution");
    $("#solve-button").click();
    $("#status-filter").value = "solved"; $("#status-filter").dispatchEvent(new Event("change", { bubbles: true }));
    check($("#problem-list").children.length === 1, "Solved progress filter");
    $("#solve-button").click();
    check(!$("#empty-list").hidden, "Progress filter refresh");
    $("#clear-filters").click();
    $("#shortcuts-button").click();
    check($("#shortcuts-dialog").open, "Shortcuts dialog"); $("#shortcuts-dialog").close();
    $("#solution-tab").focus();
    $("#solution-tab").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowLeft", bubbles: true }));
    check(document.activeElement.id === "prompt-tab", "Keyboard tabs");
    $("#code-editor").value = "print(input())"; input($("#code-editor"));
    $("#tests-editor").value = ""; input($("#tests-editor"));
    $("#stdin-editor").value = "hello"; input($("#stdin-editor"));
    $("#run-button").click(); await wait(() => !$("#run-button").disabled);
    check($("#console-output").textContent.trim() === "hello", "Standard input");
    $("#code-editor").value = "broken("; input($("#code-editor"));
    $("#run-button").click(); await wait(() => !$("#run-button").disabled);
    check($("#console-output").classList.contains("is-error"), "Python error");
    $("#code-editor").value = "print('retry passed')"; input($("#code-editor"));
    $("#run-button").click(); await wait(() => !$("#run-button").disabled);
    check($("#console-output").textContent.includes("retry passed"), "Retry");
    return { filters: true, editorJump: true, progress: true, dialogs: true, keyboardTabs: true, execution: true, stdin: true, errorRecovery: true };
  }, expectedCount);
  await cdp("Page.addScriptToEvaluateOnNewDocument", {
    source: 'globalThis.__aliasMigrationSeeded = true; localStorage.setItem("python-practice-lab:progress:v1", JSON.stringify({permute: {code: "# saved alias draft", status: "solved", updatedAt: "2026-10-01"}}));',
  });
  await cdp("Page.navigate", { url: url + "/?alias-migration=1#permute" });
  await waitFor(() => evaluate(() => globalThis.__aliasMigrationSeeded && document.querySelector("#problem-title")?.textContent === "Permutations"), "alias link");
  assert.equal(await evaluate(() => document.querySelector("#code-editor").value), "# saved alias draft");
  assert.equal(await evaluate(() => document.querySelector("#solve-button").getAttribute("aria-pressed")), "true");
  assert.equal(errors.length, 0, JSON.stringify(errors));
  console.log(JSON.stringify({ layouts, flow, aliasMigration: true, uncaughtErrors: errors.length, screenshots: profile }, null, 2));
} finally {
  for (const entry of pending.values()) clearTimeout(entry.timer);
  socket?.close();
  browser?.kill();
  server.kill();
}
