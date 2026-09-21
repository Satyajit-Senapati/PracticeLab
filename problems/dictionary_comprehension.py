"""dictionary_comprehension.py

Problem Statement:
Implement a Python module that demonstrates dictionary comprehensions for
creating, transforming, and filtering mappings in a concise and readable way.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dictionary comprehensions, mapping construction,
filtering, data transformation, comprehension syntax, immutability
Real-world Use Case: Building lookup tables, aggregating results by key,
transforming metadata dictionaries, and creating configuration maps.
Input Description: Functions accept iterables of keys and values, dictionaries,
and optional predicates for filtering.
Output Description: Functions return dictionaries generated via comprehensions,
with transformed values, filtered entries, or enriched mappings.
Example Inputs and Outputs:
    build_square_map([1, 2, 3]) -> {1: 1, 2: 4, 3: 9}
    filter_non_empty({"a": "", "b": "hello"}) -> {"b": "hello"}
    invert_mapping({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
Constraints: Use dictionary comprehensions for clear transformations, avoid
complex logic inside comprehensions, and preserve readability.
Brute Force Approach: Build dictionaries iteratively with explicit loops.
Optimized Approach: Use dictionary comprehensions for concise construction
while maintaining readability.
Time Complexity: O(n) for single-pass dictionary creation or filtering.
Space Complexity: O(n) for output dictionaries.
Step-by-step Dry Run:
    input_values = [1, 2]
    result = {value: value * value for value in input_values}
    return {1: 1, 2: 4}
Edge Cases: empty inputs, duplicate values when inverting mappings,
filtering out all entries, and non-hashable keys.
Common Mistakes: using non-hashable keys, mutating dictionaries while iterating,
and writing overly complex expressions inside comprehensions.
Follow-up Interview Questions:
    1. When should you use a dictionary comprehension instead of a loop?
    2. How can you safely invert a dictionary with duplicate values?
    3. What are the performance characteristics of dictionary creation in Python?
Alternative Approaches: Use explicit loops or `dict()` with generator
expressions for readability and safe handling of duplicates.
Expected Output: The script prints example results for dictionary creation,
filtering, and transformation.
Key Takeaways: Dictionary comprehensions are powerful for building and
transforming mappings succinctly when the logic remains simple.
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Sequence, TypeVar

K = TypeVar("K")
V = TypeVar("V")
U = TypeVar("U")


def build_square_map(values: Iterable[int]) -> Dict[int, int]:
    """Build a dictionary mapping values to their squares."""
    return {value: value * value for value in values}


def filter_non_empty(values: Dict[str, str]) -> Dict[str, str]:
    """Return only dictionary entries whose values are non-empty strings."""
    return {key: value for key, value in values.items() if value.strip()}


def invert_mapping(mapping: Dict[K, V]) -> Dict[V, K]:
    """Invert a mapping by swapping keys and values."""
    return {value: key for key, value in mapping.items()}


def normalize_keys(values: Dict[str, V]) -> Dict[str, V]:
    """Normalize dictionary keys by stripping whitespace and lowering case."""
    return {key.strip().lower(): value for key, value in values.items()}


def build_frequency_map(items: Sequence[str]) -> Dict[str, int]:
    """Build a frequency map for strings using a dictionary comprehension."""
    return {item: items.count(item) for item in set(items)}


def main() -> None:
    """Main demonstration function for dictionary comprehension patterns."""
    square_map = build_square_map([1, 2, 3, 4])
    filtered = filter_non_empty({"a": "", "b": "hello", "c": "  "})
    inverted = invert_mapping({"a": 1, "b": 2})
    normalized = normalize_keys({"Name": "Alice", "  Age ": 30})
    frequency = build_frequency_map(["apple", "banana", "apple", "cherry"])

    print("Square map:", square_map)
    print("Filtered non-empty dict:", filtered)
    print("Inverted mapping:", inverted)
    print("Normalized keys:", normalized)
    print("Frequency map:", frequency)


if __name__ == "__main__":
    main()
