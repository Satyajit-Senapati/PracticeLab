"""contains_duplicate.py

Problem Statement:
Determine whether an array contains any duplicate values.

Interview Difficulty: Easy
Commonly Asked By: Google, Amazon, Microsoft, Apple
Concepts Tested: hash sets, time-space tradeoffs, duplicate detection.
Real-world Use Case: data validation and deduplication.
Input Description: A list of integers.
Output Description: True if any value appears more than once.
Example Inputs and Outputs:
    [1,2,3,1] -> True
Constraints: Aim for O(n) time and O(n) space.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if there are duplicate elements in the list."""
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def main() -> None:
    """Main function demonstrating duplicate detection."""
    examples = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [2, 2, 2, 2],
        [],
    ]
    for nums in examples:
        print(nums, "->", contains_duplicate(nums))


if __name__ == "__main__":
    main()
