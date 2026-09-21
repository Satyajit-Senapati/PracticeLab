// The marker lets the catalog decode generated strings without changing legacy exercises.
export const METADATA_MARKER = "# practice-lab metadata v1\n";

export function formatProblemSource(docstring, solution = "") {
  const escaped = docstring.replaceAll("\\", "\\\\").replaceAll('"', '\\"');
  return `${METADATA_MARKER}"""${escaped}\n"""\n${solution ? `\n${solution}\n` : ""}`;
}
