"""typing_i.py

Problem Statement:
Implement a Python module that demonstrates type annotations, type aliases,
Union, Optional, and collections typing for static type safety and readability.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: type hints, typing module, Optional, Union, Sequence,
Dict, Callable, static typing, readability
Real-world Use Case: Defining clear function contracts, improving editor
intellisense, documenting APIs, and reducing type-related bugs in pipelines.
Input Description: Functions accept typed values, optional parameters, and
generic sequences.
Output Description: Functions return typed results and illustrate how type
annotations guide API usage.
Example Inputs and Outputs:
    repeat_text("hi", 3) -> "hihihi"
    sum_numbers([1, 2, 3]) -> 6
    handle_data({"x": 1}) -> "Processed: {'x': 1}"
Constraints: Use Python 3.12+ type annotations, avoid overcomplicated types,
and keep function signatures readable.
Brute Force Approach: Use no annotations or only basic types.
Optimized Approach: Apply expressive annotations for generic and optional
inputs while maintaining simplicity.
Time Complexity: O(n) for sequence processing.
Space Complexity: O(n) for output collection when applicable.
Step-by-step Dry Run:
    result = repeat_text("a", 2)
    return "aa"
Edge Cases: None input, empty lists, invalid types, and heterogeneous
collections where supported.
Common Mistakes: misusing Optional vs Union, ignoring `Any`, and inconsistent
annotations across functions.
Follow-up Interview Questions:
    1. What is the difference between `Optional[str]` and `Union[str, None]`?
    2. How do type checkers use annotations in Python?
    3. When should you use `Any`?
Alternative Approaches: Use runtime validation libraries like Pydantic,
typeguard, or explicit assertion checks.
Expected Output: The script prints typed function results and demonstrates
annotation usage in common helper functions.
Key Takeaways: Type hints improve code clarity and tooling support without
changing runtime behavior.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Any, Dict, Optional, TypeAlias, Union


Number: TypeAlias = Union[int, float]


def repeat_text(text: str, count: int) -> str:
    """Repeat text a specified number of times."""
    return text * count


def sum_numbers(values: Sequence[Number]) -> Number:
    """Return the sum of numeric values in a sequence."""
    total: Number = 0
    for value in values:
        total += value
    return total


def handle_data(data: Optional[Dict[str, Any]]) -> str:
    """Return a processed representation of optional dictionary input."""
    if data is None:
        return "No data provided"
    return f"Processed: {data}"


def apply_callback(values: Sequence[int], callback: Callable[[int], int]) -> list[int]:
    """Apply a callback to each value in the sequence."""
    return [callback(value) for value in values]


def main() -> None:
    """Main function demonstrating typing usage."""
    repeated = repeat_text("hi", 3)
    summed = sum_numbers([1, 2, 3, 4])
    handled = handle_data({"x": 1, "y": 2})
    applied = apply_callback([1, 2, 3], lambda value: value * 10)

    print("Repeated text:", repeated)
    print("Summed numbers:", summed)
    print("Handled data:", handled)
    print("Applied callback:", applied)


if __name__ == "__main__":
    main()
