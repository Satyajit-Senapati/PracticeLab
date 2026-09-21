"""loops.py

Problem Statement:
Implement a Python module that demonstrates loop constructs, including for loops,
while loops, nested loops, and iterator usage for common data processing tasks.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: loops, iteration, range, enumeration, iterator protocol,
list processing, aggregation, break and continue, nested loops
Real-world Use Case: Iterating over dataset rows, aggregating metrics, applying
transformations, generating combinations, and traversing nested structures.
Input Description: Functions accept lists, iterables, integers, and nested
collections to demonstrate looping behavior.
Output Description: The functions return summary values, filtered lists,
transformed collections, or nested aggregation results.
Example Inputs and Outputs:
    sum_values([1, 2, 3]) -> 6
    filter_even_numbers([1, 2, 3, 4]) -> [2, 4]
    multiplication_table(3, 3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
Constraints: Use clear loop structures, avoid mutating inputs when unnecessary,
and prefer readable code over complex one-liners.
Brute Force Approach: Use repetitive loops without helper functions or
encapsulated behavior.
Optimized Approach: Use Python built-in iteration utilities, generator
expressions, and helper functions to keep loops concise and explicit.
Time Complexity: O(n) for single-pass loops, O(n*m) for nested loops, and O(k)
for generator-based iteration over k elements.
Space Complexity: O(n) for new result collections, O(1) for in-place operations
when appropriate.
Step-by-step Dry Run:
    result = sum_values([1, 2, 3])
    total = 0
    total = 1 + 2 + 3
    return 6
Edge Cases: empty iterables, negative step sizes, early termination with
break, infinite while loops, and non-iterable inputs.
Common Mistakes: off-by-one errors, failing to update loop variables, using
mutable defaults, and confusing `break` with `continue`.
Follow-up Interview Questions:
    1. When do you choose `for` loops over `while` loops?
    2. How does `enumerate()` improve loop readability?
    3. What is the iterator protocol in Python?
Alternative Approaches: Use comprehensions for simple transformations, generator
functions for lazy evaluation, or built-in methods like `sum()` and `any()`.
Expected Output: The script prints examples for basic iteration, filtering,
nested multiplication tables, and iterator-based processing.
Key Takeaways: Understanding loops and iteration is foundational for data
processing and algorithm implementation.
"""

from __future__ import annotations

from typing import Iterable, Iterator, List, Sequence, Tuple


def sum_values(values: Iterable[int]) -> int:
    """Compute the sum of integer values using a for loop."""
    total = 0
    for value in values:
        total += value
    return total


def filter_even_numbers(values: Iterable[int]) -> List[int]:
    """Return a new list containing only even numbers from the input iterable."""
    result: List[int] = []
    for value in values:
        if value % 2 == 0:
            result.append(value)
    return result


def multiplication_table(rows: int, columns: int) -> List[List[int]]:
    """Generate a multiplication table with nested loops."""
    table: List[List[int]] = []
    for row in range(1, rows + 1):
        row_values: List[int] = []
        for column in range(1, columns + 1):
            row_values.append(row * column)
        table.append(row_values)
    return table


def first_true_index(values: Sequence[bool]) -> int:
    """Return the first index with a True value, or -1 if none exists."""
    for index, value in enumerate(values):
        if value:
            return index
    return -1


def iterate_with_generator(values: Iterable[int]) -> Iterator[int]:
    """Yield values multiplied by 2 using a generator for lazy iteration."""
    for value in values:
        yield value * 2


def break_and_continue_demo(values: Iterable[int]) -> Tuple[List[int], int]:
    """Demonstrate break and continue behavior in a loop."""
    processed: List[int] = []
    found_negative_index = -1
    for index, value in enumerate(values):
        if value < 0:
            found_negative_index = index
            break
        if value % 2 != 0:
            continue
        processed.append(value)
    return processed, found_negative_index


def main() -> None:
    """Main function demonstrating loop examples."""
    values = [1, 2, 3, 4, 5]
    sum_result = sum_values(values)
    filtered = filter_even_numbers(values)
    table = multiplication_table(3, 4)
    true_index = first_true_index([False, False, True, False])
    doubled_values = list(iterate_with_generator(values))
    break_continue_result = break_and_continue_demo([2, 4, 5, -1, 6])

    print("Sum of values:", sum_result)
    print("Filtered even numbers:", filtered)
    print("Multiplication table:", table)
    print("First true index:", true_index)
    print("Doubled values using generator:", doubled_values)
    print("Break and continue demo:", break_continue_result)


if __name__ == "__main__":
    main()
