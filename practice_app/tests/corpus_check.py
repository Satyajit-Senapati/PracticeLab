"""Read-only syntax and regression checks. Run from any directory with Python 3.10+."""

import ast
import importlib
import json
import pathlib
import sys
import unittest

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
        source = (REPO / "practice_app" / "dist" / "python-worker.js").read_text(encoding="utf-8")
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
