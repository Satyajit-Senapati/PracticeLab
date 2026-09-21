"""subsets.py

Problem Statement:
Implement a Python module that generates all subsets (the power set) of a list
of integers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, recursion, bitmasking, set generation
Real-world Use Case: Feature selection, combination generation, and search
space exploration.
Input Description: Functions accept a list of integers.
Output Description: Functions return a list of all subsets.
Example Inputs and Outputs:
    subsets([1,2,3]) -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Constraints: Use O(2^n) time and space to generate all subsets.
Brute Force Approach: Use bitmasks or recursion to enumerate all subset
choices.
Optimized Approach: Use backtracking to build subsets incrementally.
Time Complexity: O(n * 2^n)
Space Complexity: O(n * 2^n)
Step-by-step Dry Run:
    choose 1 or skip 1, then choose 2 or skip 2, then choose 3 or skip 3
    return all subset combinations
Edge Cases: empty list and single element list.
Common Mistakes: not copying the current subset before appending, and using
incorrect recursion bounds.
Follow-up Interview Questions:
    1. How would you generate subsets iteratively?
    2. Can you handle duplicates and return unique subsets?
    3. What is the relationship between subsets and bitmasks?
Alternative Approaches: Use Python itertools.combinations for production use.
Expected Output: The script prints all subsets for sample inputs.
Key Takeaways: Backtracking cleanly enumerates the power set with minimal state management.
"""

from __future__ import annotations

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Return all subsets of the input list."""
    results: List[List[int]] = []
    current: List[int] = []

    def backtrack(start: int) -> None:
        results.append(current[:])
        for index in range(start, len(nums)):
            current.append(nums[index])
            backtrack(index + 1)
            current.pop()

    backtrack(0)
    return results


def main() -> None:
    """Main function demonstrating subset generation."""
    examples = [
        [1, 2, 3],
        [0],
        [],
    ]
    for nums in examples:
        print(nums, "->", subsets(nums))


if __name__ == "__main__":
    main()
