"""contains_duplicate_iii.py

Problem Statement:
Determine whether any value appears more than once within k indices.

Interview Difficulty: Easy
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: sliding window, hash sets.
Real-world Use Case: rate limiting and near-duplicate detection.
Input Description: A list of integers and an integer k.
Output Description: True if any duplicate appears within k distance.
Example Inputs and Outputs:
    [1,2,3,1], k = 3 -> True
Constraints: Use O(n) time and O(min(n,k)) space.
Time Complexity: O(n)
Space Complexity: O(k)
"""

from __future__ import annotations


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    seen: set[int] = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[i - k])
    return False


def main() -> None:
    examples = [
        ([1, 2, 3, 1], 3),
        ([1, 0, 1, 1], 1),
        ([1, 2, 3, 1, 2, 3], 2),
    ]
    for nums, k in examples:
        print(nums, k, "->", contains_nearby_duplicate(nums, k))


if __name__ == "__main__":
    main()
