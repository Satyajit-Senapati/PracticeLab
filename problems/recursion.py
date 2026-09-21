"""recursion.py

Problem Statement:
Implement a Python module that demonstrates recursive problem solving, including
base cases, recursion depth control, and common recursive patterns.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, base case, recursive step, stack depth, memoization,
divide and conquer
Real-world Use Case: Recursive traversal of nested structures, evaluating
expressions, solving search problems, and processing hierarchical data.
Input Description: Functions accept integers, lists, nested collections, and
optional memoization caches.
Output Description: Functions return recursively computed values like factorial,
fibonacci sequence entries, and flattened nested lists.
Example Inputs and Outputs:
    factorial(5) -> 120
    fibonacci(6) -> 8
    flatten([[1, [2, 3], 4]]) -> [1, 2, 3, 4]
Constraints: Use explicit base cases, avoid excessive recursion depth for large
inputs, and keep recursive logic clear and well-documented.
Brute Force Approach: Use straightforward recursion without memoization or
iterative alternatives.
Optimized Approach: Apply memoization, tail recursion patterns, or iterative
solutions where recursion is expensive.
Time Complexity: O(n) for factorial, O(n) with memoization for fibonacci,
O(n) for flattening nested structures.
Space Complexity: O(n) call stack depth for recursion, O(n) output list size.
Step-by-step Dry Run:
    result = factorial(4)
    return 24
Edge Cases: zero and negative inputs, deep nesting, non-integer values, and
stack overflow for large recursion depth.
Common Mistakes: missing base case, infinite recursion, modifying shared state,
and inefficient repeated computation.
Follow-up Interview Questions:
    1. When should you avoid recursion?
    2. How can memoization improve recursive performance?
    3. What is tail recursion and does Python optimize it?
Alternative Approaches: Use iterative loops, dynamic programming, or explicit
stack simulation instead of recursion.
Expected Output: The script prints results for factorial, fibonacci,
flattened structures, and nested recursion examples.
Key Takeaways: Recursion is powerful for structured problems, but each
recursive function must have a clear base case and manageable depth.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Iterable, List, Sequence


def factorial(value: int) -> int:
    """Compute the factorial of a non-negative integer recursively."""
    if value < 0:
        raise ValueError("Factorial is not defined for negative values")
    if value in (0, 1):
        return 1
    return value * factorial(value - 1)


def fibonacci(value: int) -> int:
    """Compute the fibonacci value recursively with memoization."""
    if value < 0:
        raise ValueError("Fibonacci is not defined for negative values")
    if value in (0, 1):
        return value
    return fibonacci(value - 1) + fibonacci(value - 2)


@lru_cache(maxsize=None)
def fibonacci_memoized(value: int) -> int:
    """Compute the fibonacci value recursively using memoization."""
    if value < 0:
        raise ValueError("Fibonacci is not defined for negative values")
    if value in (0, 1):
        return value
    return fibonacci_memoized(value - 1) + fibonacci_memoized(value - 2)


def flatten(nested: Iterable[Any]) -> List[Any]:
    """Flatten a nested iterable structure recursively."""
    result: List[Any] = []
    for item in nested:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def recursive_sum(values: Sequence[int]) -> int:
    """Compute the sum of a sequence recursively."""
    if not values:
        return 0
    return values[0] + recursive_sum(values[1:])


def main() -> None:
    """Main function demonstrating recursive examples."""
    factorial_result = factorial(5)
    fibonacci_result = fibonacci_memoized(10)
    flattened = flatten([1, [2, [3, 4], 5], 6])
    recursive_total = recursive_sum([1, 2, 3, 4])

    print("Factorial of 5:", factorial_result)
    print("Memoized Fibonacci of 10:", fibonacci_result)
    print("Flattened structure:", flattened)
    print("Recursive sum:", recursive_total)


if __name__ == "__main__":
    main()
