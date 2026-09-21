"""permute.py

Problem Statement:
Return all permutations of a list of distinct integers.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: backtracking, recursion, permutation generation.
Real-world Use Case: generating orderings for scheduling or search.
Input Description: A list of distinct integers.
Output Description: A list of all possible permutations.
Example Inputs and Outputs:
    [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Constraints: Return permutations in any order.
Time Complexity: O(n * n!)
Space Complexity: O(n!)
"""

from __future__ import annotations


def permute(nums: list[int]) -> list[list[int]]:
    """Return all permutations of the input list."""
    result: list[list[int]] = []

    def backtrack(current: list[int], remaining: list[int]) -> None:
        if not remaining:
            result.append(current.copy())
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            next_remaining = remaining[:i] + remaining[i + 1:]
            backtrack(current, next_remaining)
            current.pop()

    backtrack([], nums)
    return result


def main() -> None:
    print(permute([1, 2, 3]))
    print(permute([0, 1]))


if __name__ == "__main__":
    main()
