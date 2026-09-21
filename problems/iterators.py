"""iterators.py

Problem Statement:
Implement a Python module that demonstrates the iterator protocol, custom
iterator classes, and how iterators support sequential access without exposing
internal representation.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: iterators, iterator protocol, __iter__, __next__, lazy
iteration, custom sequence objects, resource-safe iteration
Real-world Use Case: Building custom data readers, streaming ETL sources,
wrapping file or network resources, and implementing domain-specific
iterable collections.
Input Description: Functions and classes accept iterables, numeric limits, and
custom sequence values to demonstrate iterator behavior.
Output Description: The module returns iterator objects, iterated results, and
custom class instances that yield values in sequence.
Example Inputs and Outputs:
    list(NumberSequence(3)) -> [0, 1, 2]
    take(iterator, 2) -> [0, 1]
    enumerate_values(["a", "b"]) -> [(0, "a"), (1, "b")]
Constraints: Use Python iterator protocol correctly, avoid storing all data in
memory, and keep iterator state encapsulated within custom classes.
Brute Force Approach: Use lists or other materialized collections instead of
lazy iteration.
Optimized Approach: Implement __iter__ and __next__ cleanly, and use helper
functions for iterator consumption.
Time Complexity: O(n) to iterate n items.
Space Complexity: O(1) for iterator state, O(n) only if results are materialized.
Step-by-step Dry Run:
    sequence = NumberSequence(2)
    iter_obj = iter(sequence)
    next(iter_obj) -> 0
    next(iter_obj) -> 1
    StopIteration raised on next(iter_obj)
Edge Cases: exhausted iterators, reusing single-use iterators, infinite
iterators, and handling StopIteration correctly.
Common Mistakes: returning self from __iter__ without resetting state when
stateful behavior is unexpected, raising StopIteration prematurely, and
confusing iterators with iterables.
Follow-up Interview Questions:
    1. What is the difference between an iterable and an iterator?
    2. Why does Python use StopIteration to signal the end of iteration?
    3. How can you make an object both iterable and an iterator?
Alternative Approaches: Use generator functions for simpler iterator
implementation, or wrap iterables with built-in iterator tools from `itertools`.
Expected Output: The script prints examples of custom and built-in iterator
usage, showing lazy consumption and resource-safe iteration.
Key Takeaways: Iterators provide a standard protocol for lazy sequence
access, enabling memory-efficient and composable data processing.
"""

from __future__ import annotations

from typing import Iterable, Iterator, List, Optional, Sequence, Tuple


class NumberSequence(Iterator[int]):
    """Custom iterator that yields numbers from 0 to limit - 1."""

    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._current = 0

    def __iter__(self) -> NumberSequence:
        return self

    def __next__(self) -> int:
        if self._current >= self._limit:
            raise StopIteration
        value = self._current
        self._current += 1
        return value


def take(iterator: Iterator[int], count: int) -> List[int]:
    """Consume up to count items from an iterator and return them as a list."""
    results: List[int] = []
    for _ in range(count):
        try:
            results.append(next(iterator))
        except StopIteration:
            break
    return results


def enumerate_values(values: Sequence[str]) -> List[Tuple[int, str]]:
    """Return index-value pairs from a sequence using enumerate."""
    return [(index, value) for index, value in enumerate(values)]


def iterator_sum(values: Iterable[int]) -> int:
    """Sum values from any iterable using an iterator."""
    iterator = iter(values)
    total = 0
    for value in iterator:
        total += value
    return total


def main() -> None:
    """Main function demonstrating iterator examples."""
    sequence = NumberSequence(5)
    sequence_items = take(sequence, 3)
    remaining_items = take(sequence, 5)
    enumerated = enumerate_values(["alpha", "beta", "gamma"])
    total = iterator_sum([1, 2, 3, 4, 5])

    print("First three items of NumberSequence:", sequence_items)
    print("Remaining items after partial consumption:", remaining_items)
    print("Enumerated values:", enumerated)
    print("Sum of iterator-based values:", total)


if __name__ == "__main__":
    main()
