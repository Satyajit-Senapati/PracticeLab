"""contains_duplicate_ii.py

Problem Statement:
Determine whether any value appears at least twice in the array.

Interview Difficulty: Easy
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: hash sets, duplicate detection.
Real-world Use Case: data validation and frequency checks.
Input Description: A list of integers.
Output Description: True if any value appears twice.
Example Inputs and Outputs:
    [1,2,3,1] -> True
Constraints: Use O(n) time and O(n) space.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def main() -> None:
    examples = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [2, 2, 2, 2],
    ]
    for nums in examples:
        print(nums, "->", contains_duplicate(nums))


if __name__ == "__main__":
    main()
