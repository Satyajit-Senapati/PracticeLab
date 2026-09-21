"""rotate_array.py

Problem Statement:
Implement a Python module that rotates an array to the right by a given number
of steps.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: array rotation, modular arithmetic, list slicing,
in-place modification
Real-world Use Case: Circular buffer management, rotating logs, shifting time
series windows, and cyclic data processing.
Input Description: Functions accept a list of integers and a rotation step count.
Output Description: Functions return a rotated list.
Example Inputs and Outputs:
    rotate_array([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
Constraints: Use O(n) time and O(1) extra space for in-place rotation when
possible, handle k larger than length, and preserve relative ordering.
Brute Force Approach: Rotate one step at a time repeatedly.
Optimized Approach: Use slicing or three-step reversal for efficient rotation.
Time Complexity: O(n)
Space Complexity: O(n) for slicing solution, O(1) for in-place reversal.
Step-by-step Dry Run:
    values = [1, 2, 3, 4, 5], k=2
    rotated = [4, 5, 1, 2, 3]
    return rotated
Edge Cases: empty list, k=0, k equal to list length, and negative k values.
Common Mistakes: not reducing k modulo length, in-place slicing incorrectness,
and losing elements during rotation.
Follow-up Interview Questions:
    1. How can this be done in-place with O(1) extra space?
    2. What happens when k is larger than the array length?
    3. How would you rotate left instead of right?
Alternative Approaches: Use deque rotation, slicing, or repeated one-step
rotation for educational purposes.
Expected Output: The script prints rotated arrays for sample inputs.
Key Takeaways: Use modulo arithmetic and efficient slicing or reversal to
rotate arrays.
"""

from __future__ import annotations

from typing import List


def rotate_array(values: List[int], k: int) -> List[int]:
    """Rotate the array to the right by k steps using slicing."""
    if not values:
        return []

    k %= len(values)
    return values[-k:] + values[:-k] if k else values.copy()


def rotate_array_in_place(values: List[int], k: int) -> None:
    """Rotate the array to the right by k steps in place using reversal."""
    n = len(values)
    if n == 0:
        return

    k %= n
    if k == 0:
        return

    values.reverse()
    values[:k] = reversed(values[:k])
    values[k:] = reversed(values[k:])


def main() -> None:
    """Main function demonstrating array rotation."""
    examples = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4], 4),
        ([1, 2, 3], 5),
    ]
    for values, k in examples:
        rotated = rotate_array(values, k)
        in_place_values = values.copy()
        rotate_array_in_place(in_place_values, k)
        print(values, k, "->", rotated, "in-place ->", in_place_values)


if __name__ == "__main__":
    main()
