"""lambda_functions.py

Problem Statement:
Implement a Python module that demonstrates lambda functions and their use
cases, including mapping, filtering, sorting, and higher-order function
composition.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: lambda expressions, anonymous functions, closures,
higher-order functions, map/filter/reduce semantics, functional programming
Real-world Use Case: Writing concise transformation logic, applying custom
sorting keys, processing data streams, and defining inline callbacks for
ETL or event-driven systems.
Input Description: Functions accept iterables, numeric and string values, and
optional predicate or transformation functions.
Output Description: Functions return transformed lists, filtered results,
sorted values, and aggregated outputs from lambda-based processing.
Example Inputs and Outputs:
    square_numbers([1, 2, 3]) -> [1, 4, 9]
    filter_positive([-1, 0, 5]) -> [5]
    sort_by_length(["apple", "fig"]) -> ["fig", "apple"]
Constraints: Use lambda expressions for concise inline logic, avoid complex
nested lambdas, and ensure readability with descriptive function names.
Brute Force Approach: Create named helper functions for every small
transformation.
Optimized Approach: Use lambda functions where they improve clarity and
minimize boilerplate while delegating complex logic to named functions.
Time Complexity: O(n) for mapping and filtering operations, O(n log n) for
sorting.
Space Complexity: O(n) for output collections.
Step-by-step Dry Run:
    result = square_numbers([2, 3])
    mapped_values = [4, 9]
    return [4, 9]
Edge Cases: empty iterables, mixed type values, invalid predicate functions,
and lambda side effects.
Common Mistakes: overusing lambdas for readability, capturing mutable outer
state inadvertently, and forgetting return values in higher-order constructs.
Follow-up Interview Questions:
    1. When should you use a lambda versus a named function?
    2. How do lambdas capture variables from the surrounding scope?
    3. What are the limitations of lambda expressions in Python?
Alternative Approaches: Use list comprehensions, generator expressions, or
named helper functions for more complex operations.
Expected Output: The script prints examples of lambda-based mapping,
filtering, sorting, and reduce-style aggregation.
Key Takeaways: Use lambda functions judiciously for simple inline behavior and
keep code maintainable by preferring named functions when logic grows.
"""

from __future__ import annotations

from functools import reduce
from typing import Callable, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def square_numbers(values: Iterable[int]) -> List[int]:
    """Return a list of squared integer values using a lambda expression."""
    return list(map(lambda item: item * item, values))


def filter_positive(values: Iterable[int]) -> List[int]:
    """Filter input values and return only positive numbers."""
    return list(filter(lambda item: item > 0, values))


def sort_by_length(values: Sequence[str]) -> List[str]:
    """Sort strings by length using a lambda key."""
    return sorted(values, key=lambda item: len(item))


def apply_transform(values: Iterable[T], transform: Callable[[T], U]) -> List[U]:
    """Apply a transformation function to each item in the iterable."""
    return [transform(item) for item in values]


def reduce_to_sum(values: Iterable[int]) -> int:
    """Aggregate a collection of integers into their sum using reduce."""
    return reduce(lambda total, item: total + item, values, 0)


def conditional_map(values: Iterable[int]) -> List[int]:
    """Map values to their squares only when they are even."""
    return [item * item for item in values if (lambda x: x % 2 == 0)(item)]


def main() -> None:
    """Main entry point demonstrating lambda function patterns."""
    squared = square_numbers([1, 2, 3, 4])
    positives = filter_positive([-2, 0, 5, 8])
    sorted_words = sort_by_length(["banana", "kiwi", "apple"])
    transformed = apply_transform([1, 2, 3], lambda item: item + 1)
    summed = reduce_to_sum([1, 2, 3, 4])
    conditional_result = conditional_map([1, 2, 3, 4, 5, 6])

    print("Squared values:", squared)
    print("Positive values:", positives)
    print("Sorted by length:", sorted_words)
    print("Transformed values:", transformed)
    print("Reduced sum:", summed)
    print("Conditional mapped values:", conditional_result)


if __name__ == "__main__":
    main()
