"""map_filter_reduce.py

Problem Statement:
Implement a Python module that demonstrates map, filter, and reduce operations,
showing how to transform and aggregate collections using functional programming
techniques.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: functional programming, map/filter/reduce, lambda
expressions, iterators, immutability, aggregation, data transformation
Real-world Use Case: Processing event streams, transforming dataset rows,
filtering invalid records, and summarizing metrics in data engineering
pipelines.
Input Description: Functions accept iterables of numbers or strings, and
optional callable transformations or predicates.
Output Description: Functions return transformed collections, filtered results,
and aggregated values representing summary statistics.
Example Inputs and Outputs:
    square_values([1, 2, 3]) -> [1, 4, 9]
    filter_even([1, 2, 3, 4]) -> [2, 4]
    sum_values([1, 2, 3]) -> 6
Constraints: Use pure functions, avoid mutating input iterables, apply
meaningful type hints, and keep the code concise while preserving readability.
Brute Force Approach: Write loops for all transformations and aggregations.
Optimized Approach: Use built-in `map`, `filter`, and `functools.reduce`
for expressive and maintainable code.
Time Complexity: O(n) for map and filter operations, O(n) for reduce
aggregation.
Space Complexity: O(n) for transformed lists, O(1) for accumulator values.
Step-by-step Dry Run:
    values = [1, 2, 3]
    result = list(map(lambda x: x * 2, values))
    return [2, 4, 6]
Edge Cases: empty iterables, single-element collections, non-numeric values for
aggregation, and predicates that always return False.
Common Mistakes: using `reduce` without an initializer, mutating inputs in map
or filter callbacks, and mixing map/filter semantics.
Follow-up Interview Questions:
    1. When should you choose `map`/`filter` over list comprehensions?
    2. What are the benefits and drawbacks of functional programming in Python?
    3. How do iterators and generators improve memory efficiency?
Alternative Approaches: Use list comprehensions, generator expressions, or
explicit loops when readability is paramount.
Expected Output: The script prints example results from mapping, filtering, and
reducing operations.
Key Takeaways: `map`, `filter`, and `reduce` are powerful tools for functional
collection processing when used appropriately.
"""

from __future__ import annotations

from functools import reduce
from typing import Callable, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def square_values(values: Iterable[int]) -> List[int]:
    """Return the square of each integer in the input iterable."""
    return list(map(lambda value: value * value, values))


def filter_even(values: Iterable[int]) -> List[int]:
    """Return only even integers from the input iterable."""
    return list(filter(lambda value: value % 2 == 0, values))


def filter_non_empty(strings: Iterable[str]) -> List[str]:
    """Return only non-empty strings from the input iterable."""
    return list(filter(lambda value: bool(value.strip()), strings))


def apply_transform(values: Iterable[T], transform: Callable[[T], U]) -> List[U]:
    """Apply a transformation function to each value in the iterable."""
    return list(map(transform, values))


def sum_values(values: Iterable[int]) -> int:
    """Return the sum of integer values using reduce."""
    return reduce(lambda accumulator, value: accumulator + value, values, 0)


def product_values(values: Iterable[int]) -> int:
    """Return the product of integer values using reduce."""
    return reduce(lambda accumulator, value: accumulator * value, values, 1)


def count_matching(values: Iterable[T], predicate: Callable[[T], bool]) -> int:
    """Count values that satisfy the provided predicate."""
    filtered = filter(predicate, values)
    return sum(1 for _ in filtered)


def main() -> None:
    """Main function demonstrating map, filter, and reduce use cases."""
    values = [1, 2, 3, 4, 5]
    squared = square_values(values)
    evens = filter_even(values)
    non_empty = filter_non_empty(["apple", "", "banana", "  ", "cherry"])
    transformed = apply_transform(values, lambda value: value + 1)
    total = sum_values(values)
    product = product_values([1, 2, 3, 4])
    count_large = count_matching(values, lambda value: value > 3)

    print("Squared values:", squared)
    print("Even values:", evens)
    print("Non-empty strings:", non_empty)
    print("Transformed values:", transformed)
    print("Sum of values:", total)
    print("Product of values:", product)
    print("Count of values > 3:", count_large)


if __name__ == "__main__":
    main()
