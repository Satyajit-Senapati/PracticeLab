"""combination_sum_iii.py

Problem Statement:
Find all valid combinations of k numbers that add up to n using numbers 1-9.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: backtracking, combination generation.
Real-world Use Case: constrained combination enumeration.
Input Description: Integers k and n.
Output Description: All unique combinations of k numbers summing to n.
Example Inputs and Outputs:
    k=3, n=7 -> [[1,2,4]]
Constraints: Use numbers 1 through 9 without repetition.
Time Complexity: O(9 choose k)
Space Complexity: O(k)
"""

from __future__ import annotations


def combination_sum_3(k: int, n: int) -> list[list[int]]:
    """Return all combinations of k numbers summing to n."""
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int], remaining: int) -> None:
        if len(current) == k:
            if remaining == 0:
                result.append(current.copy())
            return
        for num in range(start, 10):
            if num > remaining:
                break
            current.append(num)
            backtrack(num + 1, current, remaining - num)
            current.pop()

    backtrack(1, [], n)
    return result


def main() -> None:
    print(combination_sum_3(3, 7))
    print(combination_sum_3(3, 9))


if __name__ == "__main__":
    main()
