"""permutations.py

Problem Statement:
Implement a Python module that generates all permutations of a list of
integers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, recursion, swapping, state exploration
Real-world Use Case: Permutation generation for scheduling, combinatorial
search, and ordering problems.
Input Description: Functions accept a list of integers.
Output Description: Functions return a list of all possible permutations.
Example Inputs and Outputs:
    permute([1,2,3]) -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Constraints: Use O(n!) time and space in the output size.
Brute Force Approach: Build permutations by swapping elements and recursing.
Optimized Approach: Use in-place swapping with backtracking.
Time Complexity: O(n * n!)
Space Complexity: O(n!)
Step-by-step Dry Run:
    choose 1, then permute [2,3]
    choose 2, then permute [3]
    return [1,2,3]
Edge Cases: empty list, single-element lists, and lists with duplicate values
(if duplicates are not filtered).
Common Mistakes: modifying shared state, not backtracking properly, and
appending references to the same list.
Follow-up Interview Questions:
    1. How can you generate permutations in lexicographic order?
    2. What changes if duplicate values are allowed and unique permutations
       are required?
    3. Can you generate permutations iteratively?
Alternative Approaches: Use Python's itertools.permutations for production.
Expected Output: The script prints permutation lists for sample inputs.
Key Takeaways: Backtracking with swapping is a natural way to generate permutations.
"""

from __future__ import annotations

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """Return all permutations of the list of integers."""
    results: List[List[int]] = []

    def backtrack(start: int) -> None:
        if start == len(nums):
            results.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return results


def main() -> None:
    """Main function demonstrating permutation generation."""
    examples = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]
    for nums in examples:
        print(nums, "->", permute(nums))


if __name__ == "__main__":
    main()
