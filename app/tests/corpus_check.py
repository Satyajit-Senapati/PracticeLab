"""Read-only syntax and regression checks. Run from any directory with Python 3.10+."""

import ast
import importlib
import json
import pathlib
import sys
import unittest
import subprocess
import types
from collections.abc import Iterator

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
sys.dont_write_bytecode = True


class CorpusChecks(unittest.TestCase):
    def test_all_exercises_compile(self):
        files = sorted((REPO / "problems").glob("*.py"))
        self.assertGreater(len(files), 0)
        for path in files:
            with self.subTest(problem=path.name):
                compile(ast.parse(path.read_text(encoding="utf-8-sig")), str(path), "exec")

    def test_all_programs_run(self):
        for path in sorted((REPO / "problems").glob("*.py")):
            with self.subTest(problem=path.name):
                result = subprocess.run(
                    [sys.executable, "-B", "-m", f"problems.{path.stem}"],
                    cwd=REPO, stdin=subprocess.DEVNULL, capture_output=True,
                    text=True, timeout=5,
                )
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_catalog_reference_checks(self):
        catalog = json.loads((REPO / "app/dist/data/problems.json").read_text(encoding="utf-8"))
        specs_checked = 0
        for problem in catalog["problems"]:
            with self.subTest(problem=problem["id"]):
                self.assertEqual(problem["solutionStatus"], "available")
                module = types.ModuleType("reference_check")
                sys.modules[module.__name__] = module
                try:
                    namespace = module.__dict__
                    exec(compile(problem["solution"], problem["file"], "exec"), namespace)
                    spec_path = REPO / "practice_specs" / f'{problem["id"]}.json'
                    if spec_path.exists():
                        spec = json.loads(spec_path.read_text(encoding="utf-8"))
                        tests = spec.get("tests", "")
                        if tests.strip():
                            # Keep learner-facing success messages out of the validation log.
                            namespace["print"] = lambda *args, **kwargs: None
                            exec(compile(tests, str(spec_path), "exec"), namespace)
                            specs_checked += 1
                finally:
                    sys.modules.pop(module.__name__, None)
        self.assertGreaterEqual(specs_checked, 22)

    def test_runnable_documented_examples(self):
        catalog = json.loads((REPO / "app/dist/data/problems.json").read_text(encoding="utf-8"))
        checked = 0
        unordered = {"permute", "permute_unique", "subsets", "combine", "combination_sum", "combination_sum2", "find_ladders"}
        for problem in catalog["problems"]:
            module = importlib.import_module("problems." + pathlib.Path(problem["file"]).stem)
            for line in problem["examples"].splitlines():
                if "->" not in line:
                    continue
                expression, expected = map(str.strip, line.split("->", 1))
                try:
                    call = ast.parse(expression, mode="eval").body
                    expected_tree = ast.parse(expected, mode="eval")
                    if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name):
                        continue
                    if not hasattr(module, call.func.id) or any(
                        isinstance(node, ast.Constant) and node.value is Ellipsis
                        for node in ast.walk(ast.Module(body=[call, expected_tree], type_ignores=[]))
                    ):
                        continue
                    args = [ast.literal_eval(arg) for arg in call.args]
                    kwargs = {item.arg: ast.literal_eval(item.value) for item in call.keywords}
                    alternatives = expected_tree.body.values if isinstance(expected_tree.body, ast.BoolOp) and isinstance(expected_tree.body.op, ast.Or) else [expected_tree.body]
                    wanted = [ast.literal_eval(value) for value in alternatives]
                except (SyntaxError, ValueError, TypeError):
                    continue
                with self.subTest(problem=problem["id"], example=line.strip()):
                    actual = getattr(module, call.func.id)(*args, **kwargs)
                    if isinstance(actual, Iterator):
                        actual = tuple(actual)
                    if call.func.id in unordered:
                        actual = sorted(tuple(value) for value in actual)
                        wanted = [sorted(tuple(value) for value in choice) for choice in wanted]
                    self.assertIn(actual, wanted)
                    checked += 1
        self.assertGreaterEqual(checked, 100)

    def test_matrix_search_matches_membership(self):
        import itertools
        for name in ["search_a_2d_matrix_ii", "search_a_2d_matrix_iii"]:
            search = importlib.import_module("problems." + name).search_matrix
            for values in itertools.combinations_with_replacement(range(4), 6):
                matrix = [list(values[:3]), list(values[3:])]
                for target in range(-1, 5):
                    with self.subTest(module=name, matrix=matrix, target=target):
                        self.assertEqual(search(matrix, target), any(target in row for row in matrix))
            overlapping = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
            for target in range(11):
                self.assertEqual(search(overlapping, target), any(target in row for row in overlapping))

    def test_first_missing_positive_matches_set_oracle(self):
        import itertools
        solve = importlib.import_module("problems.first_missing_positive").first_missing_positive
        for size in range(5):
            for values in itertools.product(range(-1, 4), repeat=size):
                expected = next(value for value in range(1, size + 2) if value not in values)
                self.assertEqual(solve(list(values)), expected)

    def test_longest_balanced_substring_matches_bruteforce(self):
        import itertools
        solve = importlib.import_module("problems.longest_valid_parentheses").longest_valid_parentheses
        for size in range(8):
            for chars in itertools.product("()", repeat=size):
                text = "".join(chars)
                expected = 0
                for start in range(size):
                    balance = 0
                    for end in range(start, size):
                        balance += 1 if text[end] == "(" else -1
                        if balance < 0:
                            break
                        if balance == 0:
                            expected = max(expected, end - start + 1)
                self.assertEqual(solve(text), expected)

    def test_course_schedule_matches_subset_oracle(self):
        import itertools
        solve = importlib.import_module("problems.course_schedule_iii").schedule_course
        for courses in itertools.product([(1,1), (2,2), (2,3), (3,4)], repeat=4):
            expected = 0
            for size in range(1, 5):
                for subset in itertools.combinations(courses, size):
                    elapsed = 0
                    for duration, deadline in sorted(subset, key=lambda course: course[1]):
                        elapsed += duration
                        if elapsed > deadline:
                            break
                    else:
                        expected = max(expected, size)
            self.assertEqual(solve(list(courses)), expected)

    def test_lazy_python_exercises(self):
        import itertools
        merge = importlib.import_module("problems.merge_sorted_iterators").merge_sorted_iterators
        self.assertEqual(list(itertools.islice(merge(itertools.count(0, 2), itertools.count(1, 2)), 8)), list(range(8)))
        flatten = importlib.import_module("problems.flatten_nested_iterables").flatten_nested_iterables
        nested = 1
        for _ in range(1500):
            nested = [nested]
        self.assertEqual(list(flatten(nested)), [1])
        group = importlib.import_module("problems.group_records").group_records
        with self.assertRaises(KeyError):
            group([{"other": 1}], "team")
        weighted = importlib.import_module("problems.dijkstra_shortest_paths").dijkstra_shortest_paths
        self.assertEqual(weighted({0: [(None, 1), ("a", 1)], None: [("a", 0)]}, 0), {0: 0, None: 1, "a": 1})
        with self.assertRaises(ValueError):
            weighted({"unreachable": [("x", -1)]}, "start")

    def test_n_queens(self):
        solve = importlib.import_module("problems.n_queens").solve_n_queens
        for size, count in [(1, 1), (2, 0), (3, 0), (4, 2), (8, 92)]:
            self.assertEqual(len(solve(size)), count)

    def test_clone_preserves_cycles_and_distinct_nodes(self):
        graph = importlib.import_module("problems.clone_graph")
        first, second = graph.Node(1), graph.Node(1)
        first.neighbors = [first, second]
        second.neighbors = [first]
        cloned = graph.clone_graph(first)
        self.assertIsNot(cloned, first)
        self.assertIs(cloned.neighbors[0], cloned)
        self.assertIsNot(cloned.neighbors[1], cloned)
        self.assertIs(cloned.neighbors[1].neighbors[0], cloned)
        self.assertIsNone(graph.clone_graph(None))

    def test_merge_duplicate_values(self):
        module = importlib.import_module("problems.merge_k_sorted_lists")
        heads = [module.build_list(values) for values in ([1, 4, 5], [1, 3, 4], [2, 6])]
        self.assertEqual(module.list_to_values(module.merge_k_lists(heads)), [1, 1, 2, 3, 4, 4, 5, 6])
        self.assertIsNone(module.merge_k_lists([]))

    def test_weak_references(self):
        self.assertTrue(importlib.import_module("problems.memory_management").weak_reference_demo())

    def test_metaclass_examples_and_required_method(self):
        module = importlib.import_module("problems.metaclasses")
        self.assertEqual(module.MyPlugin().run(), "MyPlugin executed")
        self.assertEqual(module.AnotherPlugin().run(), "AnotherPlugin executed")
        self.assertEqual(module.PluginRegistryMeta.plugins, ["MyPlugin", "AnotherPlugin"])
        with self.assertRaises(TypeError):
            class MissingRun(module.BasePlugin):
                pass
        with self.assertRaises(NotImplementedError):
            module.BasePlugin().run()
        original_registry = module.PluginRegistryMeta.plugins.copy()
        try:
            class ValidPlugin(module.BasePlugin):
                def run(self):
                    return "valid"
            self.assertEqual(ValidPlugin().run(), "valid")
            self.assertEqual(module.PluginRegistryMeta.plugins, original_registry + ["ValidPlugin"])
        finally:
            module.PluginRegistryMeta.plugins[:] = original_registry

    def test_phone_extraction_and_validation(self):
        module = importlib.import_module("problems.regex_matching")
        for phone in ["555-1234", "+1 (555) 123-4567", "5551234567"]:
            self.assertTrue(module.is_valid_phone(phone))
            self.assertEqual(module.extract_phone_number(f"Call {phone} today"), phone)
        self.assertIsNone(module.extract_phone_number("No phone here"))
        for value in ["555-1234\n", "(5551234567", "555)1234567", "123"]:
            self.assertFalse(module.is_valid_phone(value))
        self.assertFalse(module.is_valid_email("user@example.com\n"))

    def test_justification_examples(self):
        justify = importlib.import_module("problems.text_justification").justify_text
        self.assertEqual(justify(["This", "is", "an", "example"], 16), ["This    is    an", "example         "])
        self.assertEqual(justify(["This", "is", "text"], 10), ["This    is", "text      "])

    def test_standard_library_names_in_module_mode(self):
        importlib.import_module("problems.dataclasses")
        importlib.import_module("problems.enum")

    def test_browser_runner_python_harness(self):
        source = (REPO / "app" / "dist" / "python-worker.js").read_text(encoding="utf-8")
        harness = source.split("runPythonAsync(`\n", 1)[1].split("\n    `);", 1)[0].replace("\\\\", "\\")
        tree = ast.parse(harness)
        result_expression = compile(ast.Expression(tree.body[-1].value), "runner_result", "eval")

        def run(code, stdin=""):
            namespace = {"_practice_code": code, "_practice_stdin": stdin}
            exec(compile(tree, "runner", "exec"), namespace)
            return json.loads(eval(result_expression, namespace))

        for code in ["import sys; sys.exit()", "raise SystemExit(None)", "raise SystemExit(0)"]:
            self.assertEqual(run(code)["exitCode"], 0)
        self.assertEqual(run("raise SystemExit(2)")["exitCode"], 2)
        self.assertEqual(run("print(input()); print(input())", "one\ntwo")["stdout"], "one\ntwo\n")
        failure = run("assert 1 == 2")
        self.assertEqual(failure["exitCode"], 1)
        self.assertIn("AssertionError", failure["stderr"])
        self.assertIn("[output truncated]", run("print('x' * 150000)")["stdout"])
        run("previous_attempt = 1")
        self.assertIn("NameError", run("print(previous_attempt)")["stderr"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
