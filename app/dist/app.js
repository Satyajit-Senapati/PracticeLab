const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

const STORAGE_KEY = "python-practice-lab:progress:v1";
const CUSTOM_KEY = "python-practice-lab:custom:v1";

const elements = {
  problemCount: $("#problem-count"),
  progressRing: $("#progress-ring"),
  progressPercent: $("#progress-percent"),
  search: $("#problem-search"),
  difficultyFilters: $("#difficulty-filters"),
  topicFilter: $("#topic-filter"),
  problemList: $("#problem-list"),
  emptyList: $("#empty-list"),
  problemMeta: $("#problem-meta"),
  problemTitle: $("#problem-title"),
  fileName: $("#file-name"),
  solveButton: $("#solve-button"),
  solveLabel: $("#solve-label"),
  promptTab: $("#prompt-tab"),
  solutionTab: $("#solution-tab"),
  promptView: $("#prompt-view"),
  solutionView: $("#solution-view"),
  codeEditor: $("#code-editor"),
  testsEditor: $("#tests-editor"),
  stdinEditor: $("#stdin-editor"),
  lineNumbers: $("#line-numbers"),
  testsTab: $("#tests-tab"),
  inputTab: $("#input-tab"),
  testsView: $("#tests-view"),
  inputView: $("#input-view"),
  autosaveStatus: $("#autosave-status"),
  resetButton: $("#reset-button"),
  runButton: $("#run-button"),
  runLabel: $("#run-label"),
  consoleOutput: $("#console-output"),
  executionTime: $("#execution-time"),
  clearConsole: $("#clear-console"),
  runtimePill: $("#runtime-pill"),
  runtimeLabel: $("#runtime-label"),
  addProblemButton: $("#add-problem-button"),
  addProblemDialog: $("#add-problem-dialog"),
  addProblemForm: $("#add-problem-form"),
  closeAddProblem: $("#close-add-problem"),
  cancelAddProblem: $("#cancel-add-problem"),
  addModeNote: $("#add-mode-note"),
  createProblemButton: $("#create-problem-button"),
  shortcutsButton: $("#shortcuts-button"),
  shortcutsDialog: $("#shortcuts-dialog"),
  toastRegion: $("#toast-region"),
};

const state = {
  problems: [],
  filtered: [],
  selectedId: null,
  difficulty: "all",
  topic: "all",
  query: "",
  localMode: false,
  progress: loadJson(STORAGE_KEY, {}),
  customProblems: loadJson(CUSTOM_KEY, []),
  saveTimer: null,
  runner: null,
  running: false,
  runningProblemId: null,
  results: new Map(),
  storageWarningShown: false,
};

class PythonRunner {
  constructor(onStatus) {
    this.onStatus = onStatus;
    this.sequence = 0;
    this.pending = new Map();
    this.createWorker();
  }

  createWorker() {
    this.worker?.terminate();
    const worker = new Worker(new URL("./python-worker.js", import.meta.url), { type: "module" });
    this.worker = worker;
    this.failed = false;
    this.ready = new Promise((resolve, reject) => {
      const readyTimer = window.setTimeout(() => {
        if (this.worker !== worker) return;
        worker.terminate();
        this.failed = true;
        this.onStatus({ status: "error", message: "Python load timed out — run to retry" });
        reject(new Error("The local Python runtime took too long to load. Restart the local server and try again."));
      }, 45_000);

      worker.addEventListener("message", (event) => {
        if (this.worker !== worker || this.failed) return;
        const message = event.data;
        if (message.type === "status") {
          this.onStatus(message);
          if (message.status === "ready") {
            window.clearTimeout(readyTimer);
            this.failed = false;
            resolve();
          } else if (message.status === "error") {
            window.clearTimeout(readyTimer);
            worker.terminate();
            this.failed = true;
            reject(new Error(message.detail || message.message));
          }
          return;
        }

        if (message.type === "result") {
          const pending = this.pending.get(message.id);
          if (!pending) return;
          window.clearTimeout(pending.timer);
          this.pending.delete(message.id);
          pending.resolve(message);
        }
      });

      worker.addEventListener("error", (event) => {
        if (this.worker !== worker) return;
        window.clearTimeout(readyTimer);
        worker.terminate();
        this.failed = true;
        this.onStatus({ status: "error", message: "Python worker stopped — run to retry" });
        reject(new Error(event.message || "Python worker failed."));
        for (const pending of this.pending.values()) {
          window.clearTimeout(pending.timer);
          pending.reject(new Error("Python worker failed."));
        }
        this.pending.clear();
      });
    });
    this.ready.catch(() => undefined);
  }

  async run(code, stdin) {
    if (this.failed) this.createWorker();
    await this.ready;
    const worker = this.worker;
    const id = ++this.sequence;
    return new Promise((resolve, reject) => {
      const timer = window.setTimeout(() => {
        this.pending.delete(id);
        worker.terminate();
        this.failed = true;
        this.onStatus({ status: "error", message: "Timed out · run to retry" });
        reject(new Error("Execution stopped after 10 seconds. Check for an infinite loop."));
      }, 10_000);
      this.pending.set(id, { resolve, reject, timer });
      try { worker.postMessage({ type: "run", id, code, stdin }); }
      catch (error) {
        window.clearTimeout(timer);
        this.pending.delete(id);
        worker.terminate();
        this.failed = true;
        reject(error);
      }
    });
  }
}

function loadJson(key, fallback) {
  try {
    const value = JSON.parse(localStorage.getItem(key));
    if (Array.isArray(fallback)) {
      return Array.isArray(value) ? value.filter((item) => item && typeof item.id === "string" &&
        typeof item.title === "string" && typeof item.file === "string" &&
        (item.concepts == null || Array.isArray(item.concepts)) && (item.companies == null || Array.isArray(item.companies))) : fallback;
    }
    return value && typeof value === "object" && !Array.isArray(value)
      ? Object.fromEntries(Object.entries(value).filter(([, item]) => item && typeof item === "object" && !Array.isArray(item)))
      : fallback;
  } catch {
    return fallback;
  }
}

function saveProgress() {
  const saved = saveJson(STORAGE_KEY, state.progress);
  updateProgressSummary();
  return saved;
}

function saveJson(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch {
    if (!state.storageWarningShown) {
      state.storageWarningShown = true;
      showToast("Browser storage is unavailable or full. Keep this tab open and copy your work before leaving.", true);
    }
    return false;
  }
}

function requestedProblemId() {
  try { return decodeURIComponent(location.hash.slice(1)); }
  catch { return ""; }
}

function selectedProblem() {
  return state.problems.find((problem) => problem.id === state.selectedId);
}

function draftFor(problem) {
  return state.progress[problem.id] ?? {};
}

function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
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

function badge(text, className = "") {
  return `<span class="badge ${className}">${escapeHtml(text)}</span>`;
}

function section(title, content, { code = false } = {}) {
  if (!content) return "";
  const body = code
    ? `<pre>${escapeHtml(content)}</pre>`
    : `<p>${escapeHtml(content).replaceAll("\n", "<br>")}</p>`;
  return `<section class="content-section"><h3>${escapeHtml(title)}</h3>${body}</section>`;
}

function statusFor(problem) {
  const status = draftFor(problem).status;
  return ["new", "attempted", "solved"].includes(status) ? status : "new";
}

function difficultyClass(value) {
  const normalized = String(value).toLowerCase();
  return ["easy", "medium", "hard"].includes(normalized) ? normalized : "unrated";
}

function setRuntimeStatus({ status, message }) {
  elements.runtimePill.classList.toggle("is-ready", status === "ready");
  elements.runtimePill.classList.toggle("is-loading", status === "loading");
  elements.runtimePill.classList.toggle("is-error", status === "error");
  elements.runtimeLabel.textContent = message;
}

async function detectLocalMode() {
  try {
    const response = await fetch("/api/health", { cache: "no-store", signal: AbortSignal.timeout(5000) });
    if (!response.ok) return false;
    const data = await response.json();
    return data.mode === "local";
  } catch {
    return false;
  }
}

async function loadCatalog() {
  state.localMode = await detectLocalMode();
  if (!state.localMode) throw new Error("Start the local app with node app/server.mjs serve, then open http://127.0.0.1:8765.");
  elements.addModeNote.textContent = "Saves the problem and reference solution in problems/, with its title, starter code, and tests in practice_specs/.";

  const response = await fetch("/api/problems", { cache: "no-store" });
  if (!response.ok) throw new Error(`Could not load the problem catalog (${response.status}).`);
  const catalog = await response.json();
  let customCatalogChanged = false;
  state.customProblems = state.customProblems.map((problem) => {
    if (!/^[A-Za-z0-9_]+\.py$/.test(problem.file)) return problem;
    customCatalogChanged = true;
    return { ...problem, file: `problems/${problem.file}` };
  });
  const merged = new Map(catalog.problems.map((problem) => [problem.id, problem]));
  const localOnlyProblems = state.customProblems.filter((problem) => !merged.has(problem.id));
  if (localOnlyProblems.length !== state.customProblems.length) {
    state.customProblems = localOnlyProblems;
    customCatalogChanged = true;
  }
  if (customCatalogChanged) saveJson(CUSTOM_KEY, state.customProblems);
  for (const problem of localOnlyProblems) merged.set(problem.id, problem);
  state.problems = [...merged.values()].sort((a, b) => a.title.localeCompare(b.title));
  elements.problemCount.textContent = state.problems.length;
  populateTopics();
  applyFilters();

  const requestedId = requestedProblemId();
  const initial = state.problems.find((problem) => problem.id === requestedId) ?? state.filtered[0] ?? state.problems[0];
  if (initial) selectProblem(initial.id, { updateHash: false });
}

function populateTopics() {
  const topics = [...new Set(state.problems.map((problem) => problem.topic).filter(Boolean))].sort();
  elements.topicFilter.innerHTML = '<option value="all">All topics</option>' +
    topics.map((topic) => `<option value="${escapeHtml(topic)}">${escapeHtml(topic)}</option>`).join("");
  if (!topics.includes(state.topic)) state.topic = "all";
  elements.topicFilter.value = state.topic;
}

function applyFilters() {
  $$("[data-filter]", elements.difficultyFilters).forEach((button) => {
    const active = button.dataset.filter === state.difficulty;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  const query = state.query.trim().toLowerCase();
  state.filtered = state.problems.filter((problem) => {
    const difficultyMatches = state.difficulty === "all" || problem.difficulty === state.difficulty;
    const topicMatches = state.topic === "all" || problem.topic === state.topic;
    const searchable = [problem.title, problem.file, problem.topic, ...(problem.concepts ?? []), ...(problem.companies ?? [])]
      .join(" ")
      .toLowerCase();
    return difficultyMatches && topicMatches && (!query || searchable.includes(query));
  });
  renderProblemList();
}

function renderProblemList() {
  elements.problemList.innerHTML = state.filtered
    .map((problem) => {
      const status = statusFor(problem);
      const levelClass = difficultyClass(problem.difficulty);
      const check = status === "solved" ? '<svg class="icon" aria-hidden="true"><use href="#icon-check"></use></svg>' : "";
      return `
        <button
          class="problem-item ${problem.id === state.selectedId ? "is-active" : ""} is-${status}"
          type="button"
          ${problem.id === state.selectedId ? 'aria-current="true"' : ""}
          data-problem-id="${escapeHtml(problem.id)}"
          title="${escapeHtml(problem.title)}"
          aria-label="${escapeHtml(`${problem.title}, ${problem.difficulty}, ${status}`)}"
        >
          <span class="problem-status" aria-label="${escapeHtml(status)}">${check}</span>
          <span class="problem-name">${escapeHtml(problem.title)}</span>
          <span class="difficulty-dot ${levelClass}" title="${escapeHtml(problem.difficulty)}"></span>
        </button>`;
    })
    .join("");
  elements.emptyList.hidden = state.filtered.length > 0;
}

function updateProgressSummary() {
  const solved = state.problems.filter((problem) => statusFor(problem) === "solved").length;
  const percent = state.problems.length ? Math.round((solved / state.problems.length) * 100) : 0;
  elements.progressRing.style.setProperty("--progress", percent);
  elements.progressRing.setAttribute("aria-label", `${percent} percent complete`);
  elements.progressPercent.textContent = `${percent}%`;
}

function saveActiveDraft({ immediate = false } = {}) {
  const problem = selectedProblem();
  if (!problem) return;
  window.clearTimeout(state.saveTimer);

  const commit = () => {
    const previous = draftFor(problem);
    state.progress[problem.id] = {
      ...previous,
      code: elements.codeEditor.value,
      tests: elements.testsEditor.value,
      stdin: elements.stdinEditor.value,
      updatedAt: new Date().toISOString(),
    };
    const saved = saveProgress();
    elements.autosaveStatus.textContent = saved ? "Draft saved" : "Unsaved · storage unavailable";
    elements.autosaveStatus.classList.toggle("is-error", !saved);
  };

  if (immediate) commit();
  else {
    elements.autosaveStatus.textContent = "Saving draft…";
    state.saveTimer = window.setTimeout(commit, 350);
  }
}

function selectProblem(id, { updateHash = true, focusListItem = false } = {}) {
  const problem = state.problems.find((item) => item.id === id);
  if (!problem) return;
  if (state.selectedId) saveActiveDraft({ immediate: true });
  const changed = state.selectedId !== id;

  state.selectedId = id;
  if (updateHash) history.replaceState(null, "", `#${encodeURIComponent(id)}`);
  renderProblemList();
  if (focusListItem) elements.problemList.querySelector(`[data-problem-id="${CSS.escape(id)}"]`)?.focus();
  renderProblem(problem);
  updateProgressSummary();

  const draft = draftFor(problem);
  elements.codeEditor.value = draft.code ?? problem.starterCode ?? "# Write your solution here.\n";
  elements.testsEditor.value = draft.tests ?? problem.tests ?? "# Add assertions or print calls here.\n";
  elements.stdinEditor.value = draft.stdin ?? "";
  elements.codeEditor.disabled = false;
  elements.testsEditor.disabled = false;
  elements.solveButton.disabled = false;
  elements.runButton.disabled = state.running;
  elements.resetButton.disabled = false;
  elements.stdinEditor.disabled = false;
  elements.autosaveStatus.textContent = draft.updatedAt ? "Draft restored" : "Drafts save automatically";
  if (state.storageWarningShown) elements.autosaveStatus.textContent = "Kept in this tab · check storage";
  if (changed) {
    elements.codeEditor.scrollTop = 0;
    elements.codeEditor.scrollLeft = 0;
    $(".problem-scroll").scrollTop = 0;
    activateTabs(elements.promptTab, elements.solutionTab, elements.promptView, elements.solutionView);
    const result = state.results.get(id);
    showConsole(result?.message ?? (state.runningProblemId === id ? "Running Python…" : "Run your code to see output here."), Boolean(result?.isError), !result);
    elements.executionTime.textContent = result?.time ?? "";
  }
  syncLineNumbers();
}

function renderProblem(problem) {
  const levelClass = difficultyClass(problem.difficulty);
  elements.problemMeta.innerHTML = badge(problem.difficulty, levelClass) + badge(problem.topic);
  elements.problemTitle.textContent = problem.title;
  elements.fileName.textContent = problem.file;
  const isSolved = statusFor(problem) === "solved";
  elements.solveButton.classList.toggle("is-solved", isSolved);
  elements.solveButton.setAttribute("aria-pressed", String(isSolved));
  elements.solveButton.setAttribute("aria-label", isSolved ? "Mark as unsolved" : "Mark as solved");
  elements.solveLabel.textContent = isSolved ? "Solved" : "Mark solved";

  const inputOutput = problem.input || problem.output
    ? `<section class="content-section"><h3>Contract</h3><div class="complexity-grid">
        ${problem.input ? `<div class="complexity-card"><span>Input</span><p>${escapeHtml(problem.input).replaceAll("\n", "<br>")}</p></div>` : ""}
        ${problem.output ? `<div class="complexity-card"><span>Output</span><p>${escapeHtml(problem.output).replaceAll("\n", "<br>")}</p></div>` : ""}
      </div></section>`
    : "";
  const complexity = problem.timeComplexity || problem.spaceComplexity
    ? `<section class="content-section"><h3>Target complexity</h3><div class="complexity-grid">
        ${problem.timeComplexity ? `<div class="complexity-card"><span>Time</span><code>${escapeHtml(problem.timeComplexity)}</code></div>` : ""}
        ${problem.spaceComplexity ? `<div class="complexity-card"><span>Space</span><code>${escapeHtml(problem.spaceComplexity)}</code></div>` : ""}
      </div></section>`
    : "";
  const concepts = problem.concepts?.length
    ? `<section class="content-section"><h3>Concepts</h3><div class="concept-list">${problem.concepts.map((item) => `<span>${escapeHtml(item)}</span>`).join("")}</div></section>`
    : "";

  elements.promptView.innerHTML = [
    section("Problem", problem.statement),
    section("Examples", problem.examples, { code: true }),
    inputOutput,
    section("Constraints", problem.constraints),
    complexity,
    concepts,
    section("Approach hint", problem.optimized),
    section("Dry run", problem.dryRun, { code: true }),
    section("Edge cases", problem.edgeCases),
    section("Common mistakes", problem.commonMistakes),
    section("Key takeaway", problem.takeaways),
  ].join("");
  renderSolution(problem);
}

function renderSolution(problem) {
  const draft = draftFor(problem);
  if (problem.solutionStatus === "missing" || !problem.solution) {
    elements.solutionView.innerHTML = `
      <div class="missing-solution">
        <strong>Reference solution not added yet</strong>
        <p>This is a good one to solve from scratch. Add your reference implementation to ${escapeHtml(problem.file)} when you are ready.</p>
      </div>`;
    return;
  }

  if (!draft.solutionRevealed) {
    elements.solutionView.innerHTML = `
      <div class="solution-gate">
        <strong>Ready to compare?</strong>
        <p>Try an approach first. Revealing the reference won’t replace your draft.</p>
        <button class="reveal-button" id="reveal-solution" type="button">Reveal solution</button>
      </div>`;
    $("#reveal-solution")?.addEventListener("click", () => {
      state.progress[problem.id] = { ...draftFor(problem), solutionRevealed: true };
      saveProgress();
      renderSolution(problem);
    });
    return;
  }

  elements.solutionView.innerHTML = `
    <div class="solution-toolbar">
      <button class="copy-button" id="copy-solution" type="button">Copy</button>
      <button class="load-solution-button" id="load-solution" type="button">Load in editor</button>
    </div>
    <pre class="solution-code"><code>${escapeHtml(problem.solution)}</code></pre>`;
  $("#copy-solution")?.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(problem.solution);
      showToast("Reference solution copied.");
    } catch {
      showToast("Clipboard access is unavailable. Select the solution text to copy it.", true);
    }
  });
  $("#load-solution")?.addEventListener("click", () => {
    if (!window.confirm("Replace your current draft with the reference solution?")) return;
    elements.codeEditor.value = problem.solution;
    syncLineNumbers();
    saveActiveDraft({ immediate: true });
    elements.codeEditor.focus();
  });
}

function activateTabs(activeTab, inactiveTab, activeView, inactiveView) {
  activeTab.classList.add("is-active");
  activeTab.setAttribute("aria-selected", "true");
  activeTab.tabIndex = 0;
  inactiveTab.classList.remove("is-active");
  inactiveTab.setAttribute("aria-selected", "false");
  inactiveTab.tabIndex = -1;
  activeView.hidden = false;
  inactiveView.hidden = true;
}

function syncLineNumbers() {
  const count = elements.codeEditor.value.split("\n").length;
  elements.lineNumbers.textContent = Array.from({ length: count }, (_, index) => index + 1).join("\n");
  const scrollbarHeight = Math.max(0, elements.codeEditor.offsetHeight - elements.codeEditor.clientHeight) || 0;
  elements.lineNumbers.style.paddingBottom = `calc(2rem + ${scrollbarHeight}px)`;
  elements.lineNumbers.scrollTop = elements.codeEditor.scrollTop;
}

function insertIndent(event) {
  const editor = event.currentTarget;
  if (event.key === "Escape") {
    editor.dataset.allowTabExit = "true";
    return;
  }
  if (event.key !== "Tab" || event.shiftKey) return;
  if (editor.dataset.allowTabExit === "true") {
    delete editor.dataset.allowTabExit;
    return;
  }
  event.preventDefault();
  const start = editor.selectionStart;
  const end = editor.selectionEnd;
  editor.setRangeText("    ", start, end, "end");
  editor.dispatchEvent(new Event("input", { bubbles: true }));
}

async function runCode() {
  if (state.running || !selectedProblem()) return { ok: false, error: "The runner is busy or no problem is selected." };
  const code = elements.codeEditor.value.trimEnd();
  const tests = elements.testsEditor.value.trim();
  if (!code.trim()) {
    showConsole("Write some Python before running it.", true);
    return { ok: false, error: "No Python code was provided." };
  }

  state.running = true;
  state.runningProblemId = state.selectedId;
  state.results.delete(state.selectedId);
  elements.runButton.disabled = true;
  elements.runLabel.textContent = "Running…";
  elements.executionTime.textContent = "";
  showConsole("Starting Python…", false, true);

  const problem = selectedProblem();
  try {
    const current = draftFor(problem);
    state.progress[problem.id] = { ...current, status: current.status === "solved" ? "solved" : "attempted" };
    saveActiveDraft({ immediate: true });
    renderProblemList();
    const combined = tests ? `${code}\n\n# --- Tests ---\n${tests}\n` : `${code}\n`;
    const result = await state.runner.run(combined, elements.stdinEditor.value);
    const output = [result.stdout, result.stderr].filter(Boolean).join(result.stdout && result.stderr ? "\n" : "");
    const message = output || (result.exitCode === 0 ? "Finished successfully. No output." : `Program exited with code ${result.exitCode}.`);
    const time = `${result.durationMs} ms`;
    state.results.set(problem.id, { message, isError: result.exitCode !== 0, time });
    if (state.selectedId === problem.id) {
      showConsole(message, result.exitCode !== 0);
      elements.executionTime.textContent = time;
    }
    return {
      ok: result.exitCode === 0,
      problemId: problem.id,
      stdout: result.stdout,
      stderr: result.stderr,
      exitCode: result.exitCode,
      durationMs: result.durationMs,
    };
  } catch (error) {
    state.results.set(problem.id, { message: error.message, isError: true, time: "" });
    if (state.selectedId === problem.id) showConsole(error.message, true);
    return { ok: false, problemId: problem.id, error: error.message };
  } finally {
    state.running = false;
    state.runningProblemId = null;
    elements.runButton.disabled = !selectedProblem();
    elements.runLabel.textContent = "Run code";
  }
}

function registerWebMcpTools() {
  const context = document.modelContext;
  if (!context?.registerTool) return;
  const lifecycle = new AbortController();

  const reportRegistrationError = (error) => console.warn("Could not register practice tool:", error);
  const registrations = [
    {
      name: "open_practice_problem",
      title: "Open practice problem",
      description: "Open a Python problem in the visible practice workspace by its exact id.",
      inputSchema: {
        type: "object",
        properties: { problemId: { type: "string", minLength: 1 } },
        required: ["problemId"],
        additionalProperties: false,
      },
      annotations: { readOnlyHint: true, untrustedContentHint: false },
      execute(input) {
        if (!input || typeof input.problemId !== "string") throw new TypeError("problemId must be a string.");
        const problem = state.problems.find((item) => item.id === input.problemId);
        if (!problem) throw new Error(`Unknown problem id: ${input.problemId}`);
        selectProblem(problem.id);
        return { problemId: problem.id, title: problem.title, difficulty: problem.difficulty, topic: problem.topic };
      },
    },
    {
      name: "run_python_attempt",
      title: "Run Python attempt",
      description: "Put Python code and optional tests into the visible workbench, run them, and return the console result.",
      inputSchema: {
        type: "object",
        properties: {
          problemId: { type: "string", minLength: 1 },
          code: { type: "string", minLength: 1, maxLength: 100000 },
          tests: { type: "string", maxLength: 100000 },
          stdin: { type: "string", maxLength: 20000 },
        },
        required: ["problemId", "code"],
        additionalProperties: false,
      },
      annotations: { readOnlyHint: false, untrustedContentHint: true },
      async execute(input) {
        if (state.running) throw new Error("Wait for the current run to finish before replacing the editor.");
        if (!input || typeof input.problemId !== "string" || typeof input.code !== "string" || !input.code.trim()) {
          throw new TypeError("problemId and non-empty code are required.");
        }
        const problem = state.problems.find((item) => item.id === input.problemId);
        if (!problem) throw new Error(`Unknown problem id: ${input.problemId}`);
        selectProblem(problem.id);
        elements.codeEditor.value = input.code.slice(0, 100000);
        elements.testsEditor.value = typeof input.tests === "string" ? input.tests.slice(0, 100000) : "";
        elements.stdinEditor.value = typeof input.stdin === "string" ? input.stdin.slice(0, 20000) : "";
        syncLineNumbers();
        saveActiveDraft({ immediate: true });
        return runCode();
      },
    },
  ];

  for (const tool of registrations) {
    try {
      void Promise.resolve(context.registerTool(tool, { signal: lifecycle.signal })).catch(reportRegistrationError);
    } catch (error) {
      reportRegistrationError(error);
    }
  }

  window.addEventListener("pagehide", () => lifecycle.abort(), { once: true });
}

function showConsole(message, isError = false, isMuted = false) {
  elements.consoleOutput.textContent = message;
  elements.consoleOutput.classList.toggle("is-error", isError);
  if (isMuted) elements.consoleOutput.innerHTML = `<span class="console-muted">${escapeHtml(message)}</span>`;
}

function showToast(message, isError = false) {
  const toast = document.createElement("div");
  toast.className = `toast${isError ? " is-error" : ""}`;
  toast.textContent = message;
  elements.toastRegion.append(toast);
  window.setTimeout(() => toast.remove(), 3_600);
}

async function submitProblem(formData) {
  const payload = Object.fromEntries([...formData.entries()].map(([key, value]) => [key, String(value).trim()]));
  if (!payload.title || !payload.statement) throw new Error("Title and problem statement are required.");
  const slug = slugify(payload.title);
  if (!slug) throw new Error("Use at least one letter or number in the title.");

  if (!state.localMode) throw new Error("Start the local server before adding a problem.");
  const response = await fetch("/api/problems", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || "Could not create the problem.");
  state.problems.push(result.problem);
  state.problems.sort((a, b) => a.title.localeCompare(b.title));
  return result.problem;
}

function bindEvents() {
  elements.problemList.addEventListener("click", (event) => {
    const item = event.target.closest("[data-problem-id]");
    if (item) selectProblem(item.dataset.problemId, { focusListItem: true });
  });

  elements.search.addEventListener("input", () => {
    state.query = elements.search.value;
    applyFilters();
  });

  elements.difficultyFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-filter]");
    if (!button) return;
    state.difficulty = button.dataset.filter;
    $$("[data-filter]", elements.difficultyFilters).forEach((item) => item.classList.toggle("is-active", item === button));
    applyFilters();
  });

  elements.topicFilter.addEventListener("change", () => {
    state.topic = elements.topicFilter.value;
    applyFilters();
  });

  elements.promptTab.addEventListener("click", () =>
    activateTabs(elements.promptTab, elements.solutionTab, elements.promptView, elements.solutionView),
  );
  elements.solutionTab.addEventListener("click", () =>
    activateTabs(elements.solutionTab, elements.promptTab, elements.solutionView, elements.promptView),
  );
  elements.testsTab.addEventListener("click", () =>
    activateTabs(elements.testsTab, elements.inputTab, elements.testsView, elements.inputView),
  );
  elements.inputTab.addEventListener("click", () =>
    activateTabs(elements.inputTab, elements.testsTab, elements.inputView, elements.testsView),
  );

  elements.codeEditor.addEventListener("input", () => {
    syncLineNumbers();
    saveActiveDraft();
  });
  elements.testsEditor.addEventListener("input", () => saveActiveDraft());
  elements.stdinEditor.addEventListener("input", () => saveActiveDraft());
  elements.codeEditor.addEventListener("scroll", syncLineNumbers);
  elements.codeEditor.addEventListener("keydown", insertIndent);
  elements.testsEditor.addEventListener("keydown", insertIndent);
  elements.codeEditor.addEventListener("blur", () => delete elements.codeEditor.dataset.allowTabExit);
  elements.testsEditor.addEventListener("blur", () => delete elements.testsEditor.dataset.allowTabExit);

  for (const tabList of $$('[role="tablist"]')) {
    tabList.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      const tabs = $$('[role="tab"]', tabList);
      const currentIndex = tabs.indexOf(document.activeElement);
      if (currentIndex < 0) return;
      event.preventDefault();
      let nextIndex = event.key === "Home" ? 0 : event.key === "End" ? tabs.length - 1 : currentIndex + (event.key === "ArrowRight" ? 1 : -1);
      nextIndex = (nextIndex + tabs.length) % tabs.length;
      tabs[nextIndex].focus();
      tabs[nextIndex].click();
    });
  }

  elements.runButton.addEventListener("click", runCode);
  elements.clearConsole.addEventListener("click", () => {
    state.results.delete(state.selectedId);
    elements.executionTime.textContent = "";
    showConsole("Run your code to see output here.", false, true);
  });

  elements.resetButton.addEventListener("click", () => {
    const problem = selectedProblem();
    if (!problem) return;
    const hasChanges = elements.codeEditor.value !== problem.starterCode ||
      elements.testsEditor.value !== problem.tests || elements.stdinEditor.value !== "";
    if (hasChanges && !window.confirm("Reset this solution, tests, and input to their starting values?")) return;
    elements.codeEditor.value = problem.starterCode;
    elements.testsEditor.value = problem.tests;
    elements.stdinEditor.value = "";
    syncLineNumbers();
    saveActiveDraft({ immediate: true });
    showToast("Draft reset to starter code.");
  });

  elements.solveButton.addEventListener("click", () => {
    const problem = selectedProblem();
    if (!problem) return;
    const current = draftFor(problem);
    state.progress[problem.id] = { ...current, status: current.status === "solved" ? "attempted" : "solved" };
    saveProgress();
    renderProblem(problem);
    renderProblemList();
  });

  elements.addProblemButton.addEventListener("click", () => elements.addProblemDialog.showModal());
  elements.closeAddProblem.addEventListener("click", () => elements.addProblemDialog.close());
  elements.cancelAddProblem.addEventListener("click", () => elements.addProblemDialog.close());
  elements.shortcutsButton.addEventListener("click", () => elements.shortcutsDialog.showModal());
  elements.addProblemForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!elements.addProblemForm.reportValidity()) return;
    elements.createProblemButton.disabled = true;
    elements.createProblemButton.textContent = "Creating…";
    try {
      const problem = await submitProblem(new FormData(elements.addProblemForm));
      elements.addProblemDialog.close();
      elements.addProblemForm.reset();
      state.query = "";
      state.difficulty = "all";
      state.topic = "all";
      elements.search.value = "";
      populateTopics();
      applyFilters();
      selectProblem(problem.id);
      elements.problemCount.textContent = state.problems.length;
      showToast(`${problem.file} saved locally.`);
    } catch (error) {
      showToast(error.message, true);
    } finally {
      elements.createProblemButton.disabled = false;
      elements.createProblemButton.textContent = "Create problem";
    }
  });

  document.addEventListener("keydown", (event) => {
    if (elements.addProblemDialog.open || elements.shortcutsDialog.open) return;
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      elements.search.focus();
      elements.search.select();
    }
    if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
      event.preventDefault();
      runCode();
    }
  });

  window.addEventListener("beforeunload", () => saveActiveDraft({ immediate: true }));
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden") saveActiveDraft({ immediate: true });
  });
  window.addEventListener("hashchange", () => {
    const id = requestedProblemId();
    if (id && id !== state.selectedId) selectProblem(id, { updateHash: false });
  });
}

async function start() {
  bindEvents();
  try {
    state.runner = new PythonRunner(setRuntimeStatus);
  } catch {
    setRuntimeStatus({ status: "error", message: "Python unavailable" });
    state.runner = { run: async () => { throw new Error("This browser could not start Python. Try reloading or using a browser that supports web workers."); } };
  }
  try {
    await loadCatalog();
    updateProgressSummary();
    registerWebMcpTools();
  } catch (error) {
    elements.problemList.innerHTML = "";
    elements.emptyList.hidden = false;
    elements.emptyList.textContent = error.message;
    elements.problemTitle.textContent = "Could not load the practice library";
    showToast(error.message, true);
  }
}

start();
