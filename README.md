# Practice Lab — Local Only

This repo is both a collection of Python problem/solution files and an interactive practice workspace. The workspace reads the structured docstring at the top of every `problems/*.py` file, so the files you already have remain the source of truth.

## Open the practice workspace

Node.js is the only local requirement. The Python runtime is already saved in this project's `practice_app/dist/vendor/` folder. From the repository root, run:

```powershell
node practice_app/server.mjs serve
```

The app opens at `http://127.0.0.1:8765`. It includes:

- Search and filters across every problem
- Prompt and reference-solution views
- Separate solution, test, and standard-input editors
- A browser-based Python runner with a 10-second timeout
- Automatically saved drafts and solved/attempted progress
- An **Add problem** form that creates a new `.py` file in `problems/`

Python runs inside an isolated browser worker using the bundled local runtime. Normal practice works without an internet connection. An infinite loop is stopped after 10 seconds; running again starts a fresh worker. The server listens only on `127.0.0.1`, so the app is available on this computer.

If you copy or clone the source without the downloaded runtime, perform this one-time setup while online:

```powershell
node practice_app/setup-runtime.mjs
```

The setup script downloads the pinned Pyodide runtime and license. After setup, the app serves those files locally. Extra third-party Python packages are not bundled. See [Pyodide's self-hosting documentation](https://pyodide.org/en/stable/usage/downloading-and-deploying.html).

## Add a problem

The easiest route is **Add problem** in the workspace. When the local server is running, it creates a file in `problems/` using the same docstring format as the existing collection.

Expand **Starter code, tests, and reference solution** to add your solution and optional tests. Click **Create problem** to save directly to your repository. No publishing step is needed.

You can also add a file manually under `problems/`. Only `Problem Statement` and `Interview Difficulty` are needed; every other field is optional:

```python
"""example_problem.py

Problem Statement:
Describe the task here.

Interview Difficulty: Easy
Concepts Tested: arrays, hash maps
Example Inputs and Outputs:
    solve([1, 2, 3]) -> 6
"""


def solve(values):
    return sum(values)
```

Refresh the page after adding or editing files manually. The app reads the current files on each page load. To regenerate its catalog for validation, run:

```powershell
node practice_app/server.mjs build
```

## Optional starter code and tests

The app makes a basic starter automatically. For a richer exercise, create `practice_specs/<file_stem>.json`:

```json
{
  "category": "Arrays",
  "starter_code": "def solve(values):\n    raise NotImplementedError\n",
  "tests": "assert solve([1, 2, 3]) == 6\n"
}
```

This keeps learner-facing scaffolding separate from the reference solution. The Add problem form writes this sidecar for you, preserving the exact title as well as any starter code or tests.

## Run an exercise directly

From the repository root, use module mode:

```powershell
python -m problems.n_queens
```

Module mode keeps exercises named `enum.py` and `dataclasses.py` from shadowing Python's standard-library modules. The app's browser console also runs independently of these filenames.

## Check the project

```powershell
node practice_app/server.mjs build
node practice_app/validate.mjs
node --test practice_app/tests/*.test.mjs
python -B practice_app/tests/corpus_check.py
```

The checks cover catalog integrity, saving and runner regressions, local problem creation, offline Python startup, Python syntax, and the corrected reference examples. Some exercises still have statements only; the workspace labels those as missing a reference solution.

## Local data and backups

Problems and reference solutions live in `problems/`; titles and optional starter/test overrides live in `practice_specs/`. Back up these folders together with the app. Copy `practice_app/dist/vendor/` too if the destination computer must work offline immediately.

Drafts and solved/attempted progress stay in your browser's storage. Use the same browser and `http://127.0.0.1:8765` to return to them; a different hostname or port has separate storage. Clearing browser data removes those drafts.

Data saved only in the former hosted site's browser storage does not transfer automatically. Before deleting that site, copy any drafts you need and keep downloaded `.py` and `.json` files. Place those files in `problems/` and `practice_specs/` respectively.

This project is intentionally local only. It has no active hosting manifest or deployment remote. Do not publish it unless explicitly requested.

## Project layout

```text
problems/*.py                problem statements and reference solutions
practice_specs/              optional per-problem starter/test overrides
practice_app/server.mjs      local catalog builder and server
practice_app/dist/           browser application and generated catalog
practice_app/dist/vendor/    locally installed Python runtime (not Git-tracked)
practice_app/setup-runtime.mjs  one-time runtime download for a fresh checkout
```
