"""count_of_smaller_numbers_after_self.py

Problem Statement:
For each element in an integer array, count the number of smaller elements to its right.

Interview Difficulty: Hard
Commonly Asked By: Google, Facebook, Amazon
Concepts Tested: binary indexed trees, merge sort counting, order statistics.
Real-world Use Case: ranking, inversion counting, and stock analysis.
Input Description: A list of integers.
Output Description: A list of counts where each count corresponds to smaller elements after that index.
Example Inputs and Outputs:
    [5,2,6,1] -> [2,1,1,0]
Constraints: Use O(n log n) time.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from __future__ import annotations

import bisect


def count_smaller(nums: list[int]) -> list[int]:
    """Return counts of smaller numbers after each element."""
    result: list[int] = []
    sorted_suffix: list[int] = []

    for num in reversed(nums):
        index = bisect.bisect_left(sorted_suffix, num)
        result.append(index)
        bisect.insort_left(sorted_suffix, num)

    return list(reversed(result))


def main() -> None:
    examples = [
        [5, 2, 6, 1],
        [1, 1, 1, 1],
        [3, 2, 2, 6, 1],
    ]
    for nums in examples:
        print(nums, "->", count_smaller(nums))


if __name__ == "__main__":
    main()
