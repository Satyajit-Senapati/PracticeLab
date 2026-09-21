const PYODIDE_BASE = new URL("./vendor/pyodide/314.0.6/", import.meta.url).href;

let runtimePromise;

async function getRuntime() {
  if (!runtimePromise) {
    self.postMessage({ type: "status", status: "loading", message: "Loading Python…" });
    runtimePromise = import(`${PYODIDE_BASE}pyodide.mjs`).then(({ loadPyodide }) =>
      loadPyodide({ indexURL: PYODIDE_BASE }),
    );
  }
  return runtimePromise;
}

async function runPython({ id, code, stdin }) {
  const startedAt = performance.now();
  try {
    const pyodide = await getRuntime();
    self.postMessage({ type: "status", status: "ready", message: "Python ready" });
    pyodide.globals.set("_practice_code", code);
    pyodide.globals.set("_practice_stdin", stdin);

    const payload = await pyodide.runPythonAsync(`
import contextlib
import io
import json
import sys
import traceback

class _PracticeBuffer(io.StringIO):
    def __init__(self, limit=120_000):
        super().__init__()
        self.limit = limit
        self.size = 0
        self.truncated = False

    def write(self, value):
        text = str(value)
        remaining = self.limit - self.size
        if remaining > 0:
            super().write(text[:remaining])
            self.size += min(len(text), remaining)
        if len(text) > remaining:
            self.truncated = True
        return len(text)

    def result(self):
        suffix = "\\n[output truncated]" if self.truncated else ""
        return self.getvalue() + suffix

_practice_stdout = _PracticeBuffer()
_practice_stderr = _PracticeBuffer()
_practice_previous_stdin = sys.stdin
_practice_exit_code = 0
_practice_namespace = {"__name__": "__main__"}

try:
    sys.stdin = io.StringIO(_practice_stdin)
    with contextlib.redirect_stdout(_practice_stdout), contextlib.redirect_stderr(_practice_stderr):
        exec(compile(_practice_code, "solution.py", "exec"), _practice_namespace)
except SystemExit as _practice_error:
    _practice_exit_code = 0 if _practice_error.code is None else (_practice_error.code if isinstance(_practice_error.code, int) else 1)
    if _practice_error.code not in (None, 0):
        print(_practice_error, file=_practice_stderr)
except BaseException:
    _practice_exit_code = 1
    traceback.print_exc(file=_practice_stderr)
finally:
    sys.stdin = _practice_previous_stdin

json.dumps({
    "stdout": _practice_stdout.result(),
    "stderr": _practice_stderr.result(),
    "exitCode": _practice_exit_code,
})
    `);

    pyodide.globals.delete("_practice_code");
    pyodide.globals.delete("_practice_stdin");
    self.postMessage({
      type: "result",
      id,
      durationMs: Math.round(performance.now() - startedAt),
      ...JSON.parse(payload),
    });
  } catch (error) {
    self.postMessage({
      type: "result",
      id,
      durationMs: Math.round(performance.now() - startedAt),
      stdout: "",
      stderr: error?.message || String(error),
      exitCode: 1,
    });
  }
}

self.addEventListener("message", (event) => {
  if (event.data?.type === "run") runPython(event.data);
});

getRuntime()
  .then(() => self.postMessage({ type: "status", status: "ready", message: "Python ready" }))
  .catch((error) =>
    self.postMessage({
      type: "status",
      status: "error",
      message: "Python could not load",
      detail: error?.message || String(error),
    }),
  );
