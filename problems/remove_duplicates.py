"""remove_duplicates.py

Problem Statement:
Implement a Python module that removes duplicates from a list while preserving
the order of first occurrences.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: order preservation, hashing, list traversal, duplicate
removal
Real-world Use Case: Deduplicating records, cleaning data streams, and
preprocessing input lists for analytics.
Input Description: Functions accept a list of hashable values.
Output Description: Functions return a list containing unique items in original
order.
Example Inputs and Outputs:
    remove_duplicates([1, 2, 2, 3, 1]) -> [1, 2, 3]
Constraints: Preserve order, use O(n) time, and avoid duplicates in the output.
Brute Force Approach: Compare each item against every other item.
Optimized Approach: Use a set to track seen items.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    values = [1, 2, 2, 3]
    seen = set()
    output = [1, 2, 3]
Edge Cases: empty list, all duplicates, and already unique lists.
Common Mistakes: using `set()` directly on the list and losing ordering.
Follow-up Interview Questions:
    1. How would you preserve order with unhashable items?
    2. Can duplicates be removed in place?
    3. How does this change for a stream of values?
Alternative Approaches: Use `dict.fromkeys()` for hashable items or an
ordered set and manual tracking for generic types.
Expected Output: The script prints deduplicated lists for sample inputs.
Key Takeaways: Use a set to filter duplicates while preserving first occurrences.
"""

from __future__ import annotations

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def remove_duplicates(values: Iterable[T]) -> List[T]:
    """Return a list with duplicates removed while preserving original order."""
    seen: set[T] = set()
    result: List[T] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def main() -> None:
    """Main function demonstrating duplicate removal."""
    examples = [
        [1, 2, 2, 3, 1],
        ["a", "b", "a", "c"],
        [1, 1, 1],
    ]
    for values in examples:
        print(values, "->", remove_duplicates(values))


if __name__ == "__main__":
    main()
