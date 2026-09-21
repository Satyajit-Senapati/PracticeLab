"""move_zeroes.py

Problem Statement:
Implement a Python module that moves all zeros in an array to the end while
preserving the order of non-zero elements.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: in-place array modification, two-pointer technique,
array traversal, stability
Real-world Use Case: Normalizing sparse data representations, preparing
feature vectors, and compressing arrays for efficient storage.
Input Description: Functions accept a list of integers.
Output Description: Functions return a list with zeros moved to the end.
Example Inputs and Outputs:
    move_zeroes([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
Constraints: Maintain relative order of non-zero elements, use O(n) time, and
prefer O(1) extra space.
Brute Force Approach: Build a new list and append zeros afterward.
Optimized Approach: Use the two-pointer swap method to move zeros in place.
Time Complexity: O(n)
Space Complexity: O(1) extra space.
Step-by-step Dry Run:
    values = [0, 1, 0, 3, 12]
    result = [1, 3, 12, 0, 0]
    return result
Edge Cases: empty list, no zeros, all zeros, and already ordered arrays.
Common Mistakes: swapping zeros incorrectly, using extra lists unnecessarily,
and not preserving element order.
Follow-up Interview Questions:
    1. How would you move all ones to the end instead?
    2. Can this be done in two passes or one pass?
    3. How do you handle if zeros should remain in the original relative order?
Alternative Approaches: Use list comprehensions with separate zero append,
or in-place two-pointer iteration.
Expected Output: The script prints arrays with zeros moved to the end.
Key Takeaways: Use stable in-place operations to move zero values while
preserving order.
"""

from __future__ import annotations

from typing import List


def move_zeroes(values: List[int]) -> List[int]:
    """Return a new list with zeros moved to the end."""
    non_zero_values = [value for value in values if value != 0]
    zero_count = len(values) - len(non_zero_values)
    return non_zero_values + [0] * zero_count


def move_zeroes_in_place(values: List[int]) -> None:
    """Move zeros to the end in place while preserving order."""
    last_non_zero_index = 0
    for current in range(len(values)):
        if values[current] != 0:
            values[last_non_zero_index], values[current] = values[current], values[last_non_zero_index]
            last_non_zero_index += 1


def main() -> None:
    """Main function demonstrating moving zero values."""
    examples = [
        [0, 1, 0, 3, 12],
        [1, 0, 2, 0, 0, 3],
        [0, 0, 0],
    ]
    for values in examples:
        in_place_values = values.copy()
        move_zeroes_in_place(in_place_values)
        print(values, "->", move_zeroes(values), "in-place ->", in_place_values)


if __name__ == "__main__":
    main()
