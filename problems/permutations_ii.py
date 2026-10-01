"""permutations_ii.py

Problem Statement:
Implement a Python module that returns all unique permutations of a list of numbers that may contain duplicates.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, duplicate pruning, permutation generation,
sorting
Real-world Use Case: Generating unique arrangements for sequence planning and combinatorial enumeration.
Input Description: Function accepts a list of integers that may include duplicates.
Output Description: Returns a list of unique permutations.
Example Inputs and Outputs:
    nums = [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]]
Constraints: Avoid duplicate permutation results.
Brute Force Approach: Generate all permutations and deduplicate.
Optimized Approach: Sort input and skip duplicate choices during recursion.
Time Complexity: O(n! / duplicates)
Space Complexity: O(n)
Step-by-step Dry Run:
    recursively add unused numbers, skip repeated values at the same recursion level.
Edge Cases: empty input and all identical numbers.
Common Mistakes: using duplicates more than once or failing to sort input.
Follow-up Interview Questions:
    1. How would you generate permutations iteratively?
    2. Can you generate permutations in lexicographic order?
    3. What if all numbers are unique?
Alternative Approaches: Use next_permutation on sorted sequence.
Expected Output: The script prints all unique permutations for a sample input.
Key Takeaways: Duplicate-aware backtracking generates unique permutations efficiently.
"""

from collections import Counter

def permute_unique(nums: list[int]) -> list[list[int]]:
    """Return unique permutations without changing the input."""
    counts = Counter(nums)
    result = []
    def search(path):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for value in sorted(counts):
            if counts[value]:
                counts[value] -= 1
                path.append(value)
                search(path)
                path.pop()
                counts[value] += 1
    search([])
    return result
