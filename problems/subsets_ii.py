"""subsets_ii.py

Problem Statement:
Return all possible subsets of an integer array that may contain duplicates,
without duplicate subset lists.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: backtracking, sorting, duplicate pruning.
Real-world Use Case: combination generation with repeated items.
Input Description: A list of integers that may contain duplicates.
Output Description: A list of unique subsets.
Example Inputs and Outputs:
    [1,2,2] -> [[],[1],[2],[1,2],[2,2],[1,2,2]]
Constraints: Avoid duplicate subset results.
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

from __future__ import annotations


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """Return all unique subsets from the input list."""
    nums.sort()
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int]) -> None:
        result.append(current.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


def main() -> None:
    print(subsets_with_dup([1, 2, 2]))
    print(subsets_with_dup([2, 1, 2, 2]))


if __name__ == "__main__":
    main()
