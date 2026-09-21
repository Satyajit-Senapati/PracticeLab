"""combination_sum_ii.py

Problem Statement:
Implement a Python module that finds unique combinations where each candidate number may only be used once.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, sorting, duplicate pruning, combination generation
Real-world Use Case: Selecting unique item sets subject to a target budget.
Input Description: Function accepts a list of candidate numbers and a target sum.
Output Description: Returns a list of unique combinations where each number is used at most once.
Example Inputs and Outputs:
    candidates = [10,1,2,7,6,1,5], target = 8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]
Constraints: Candidates may include duplicates; combinations must remain unique.
Brute Force Approach: Explore all subsets and filter by sum.
Optimized Approach: Sort input and skip duplicates while backtracking.
Time Complexity: Exponential in n.
Space Complexity: O(n)
Step-by-step Dry Run:
    recursively choose or skip each candidate, avoid using the same value at the same depth twice.
Edge Cases: empty input and target zero.
Common Mistakes: generating duplicate combinations and not sorting candidates.
Follow-up Interview Questions:
    1. How to adapt this for unlimited uses of each candidate?
    2. Can you use memoization to reduce repeated work?
    3. What if numbers are negative?
Alternative Approaches: Use iterative subset generation with duplicate checks.
Expected Output: The script prints unique combinations for a sample input.
Key Takeaways: Sorting and duplicate skipping are crucial in combination generation.
"""
