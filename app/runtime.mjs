import { stat } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { join } from "node:path";

export const RUNTIME_VERSION = "314.0.6";
export const RUNTIME_FILES = [
  "pyodide.mjs", "pyodide.asm.mjs", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json", "LICENSE",
];
export const RUNTIME_DIR = fileURLToPath(new URL(`./dist/vendor/pyodide/${RUNTIME_VERSION}/`, import.meta.url));

export async function assertLocalRuntime() {
  for (const name of RUNTIME_FILES) {
    const info = await stat(join(RUNTIME_DIR, name)).catch(() => null);
    if (!info?.isFile() || !info.size) {
      throw new Error("Local Python runtime is missing. Run: node app/setup-runtime.mjs");
    }
  }
}
