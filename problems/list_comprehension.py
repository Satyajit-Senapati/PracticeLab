"""list_comprehension.py

Problem Statement:
Implement a Python module that demonstrates list comprehensions for transforming,
filtering, and combining collections in a concise and readable way.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: list comprehensions, iteration, filtering, nested loops,
conditional expressions, readability, data transformation
Real-world Use Case: Creating feature vectors, filtering invalid rows,
formatting data records, and generating derived collections in ETL workflows.
Input Description: Functions accept iterables, numeric values, strings, and
nested collections to demonstrate comprehension patterns.
Output Description: Functions return transformed lists, filtered results, and
combinations generated from the input data.
Example Inputs and Outputs:
    square_numbers([1, 2, 3]) -> [1, 4, 9]
    filter_positive([-1, 0, 3, 5]) -> [3, 5]
    pairwise_sum([1, 2], [3, 4]) -> [4, 6]
Constraints: Use list comprehensions for concise expressions, avoid overly
complex nesting, and preserve readability with helper functions where needed.
Brute Force Approach: Use explicit loops and append operations for every
transformation.
Optimized Approach: Use list comprehensions to express transformations in a
single readable statement.
Time Complexity: O(n) for single comprehensions, O(n*m) for nested
comprehensions.
Space Complexity: O(n) for output lists.
Step-by-step Dry Run:
    result = square_numbers([2, 3])
    return [4, 9]
Edge Cases: empty inputs, nested empty collections, filtering to an empty list,
and non-iterable inputs.
Common Mistakes: using list comprehensions for side effects, creating overly
complex nested expressions, and ignoring readability when combining filters.
Follow-up Interview Questions:
    1. When should you prefer a list comprehension over a loop?
    2. How do you create a nested comprehension?
    3. What are the memory considerations for list comprehensions?
Alternative Approaches: Use generator expressions for lazy evaluation, explicit
loops for readability, or helper functions for complex transformations.
Expected Output: The script prints several list comprehension examples including
mapped values, filtered results, nested combinations, and conditional mappings.
Key Takeaways: List comprehensions are powerful when used for simple,
readable collection transformations.
"""

from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple


def square_numbers(values: Iterable[int]) -> List[int]:
    """Return the square of each integer using a list comprehension."""
    return [value * value for value in values]


def filter_positive(values: Iterable[int]) -> List[int]:
    """Return only positive integers from the input iterable."""
    return [value for value in values if value > 0]


def convert_to_uppercase(values: Sequence[str]) -> List[str]:
    """Convert each string in the sequence to uppercase."""
    return [value.upper() for value in values]


def pairwise_sum(first: Sequence[int], second: Sequence[int]) -> List[int]:
    """Return pairwise sums of two sequences of equal length."""
    return [a + b for a, b in zip(first, second)]


def nested_combinations(rows: Sequence[int], cols: Sequence[int]) -> List[Tuple[int, int]]:
    """Return all pairs of values from two sequences using a nested comprehension."""
    return [(row, col) for row in rows for col in cols]


def conditional_transform(values: Iterable[int]) -> List[str]:
    """Map values to status strings with a conditional expression."""
    return ["positive" if value > 0 else "non-positive" for value in values]


def main() -> None:
    """Main function demonstrating list comprehension use cases."""
    values = [1, -2, 3, 0, 5]
    squared = square_numbers(values)
    positives = filter_positive(values)
    uppercase = convert_to_uppercase(["apple", "banana", "cherry"])
    summed_pairs = pairwise_sum([1, 2, 3], [4, 5, 6])
    combinations = nested_combinations([1, 2], ["a", "b"])
    statuses = conditional_transform(values)

    print("Squared values:", squared)
    print("Positive values:", positives)
    print("Uppercase strings:", uppercase)
    print("Pairwise sums:", summed_pairs)
    print("Nested combinations:", combinations)
    print("Conditional status mapping:", statuses)


if __name__ == "__main__":
    main()
