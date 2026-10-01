"""flatten_nested_iterables.py

Problem Statement:
Flatten nested lists and tuples lazily in left-to-right order using an explicit stack. Treat strings and other objects as atomic values. Inputs must be acyclic.
Interview Difficulty: Medium
Concepts Tested: generators, explicit stack, nested structures
Input Description: An iterable containing values, lists, or tuples.
Output Description: An iterator of leaf values.
Example Inputs and Outputs:
    list(flatten_nested_iterables([1, [2, (3,4)], "hi"])) -> [1,2,3,4,"hi"]
Constraints: An iterable containing values, lists, or tuples.
Time Complexity: O(n) for all visited values
Space Complexity: O(d) for maximum nesting depth
"""


def flatten_nested_iterables(values):
    stack = [iter(values)]
    while stack:
        try:
            value = next(stack[-1])
        except StopIteration:
            stack.pop()
            continue
        if isinstance(value, (list, tuple)):
            stack.append(iter(value))
        else:
            yield value
