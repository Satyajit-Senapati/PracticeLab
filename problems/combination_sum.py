"""combination_sum.py

Problem Statement:
Implement a Python module that finds all unique combinations of candidate numbers that sum to a target.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, recursion, combination generation,
pruning duplicates
Real-world Use Case: Resource allocation, budgeting combinations, and subset sum exploration.
Input Description: Function accepts a list of candidate numbers and a target sum.
Output Description: Returns list of unique combinations where candidates can be reused.
Example Inputs and Outputs:
    candidates = [2,3,6,7], target = 7 -> [[7],[2,2,3]]
Constraints: Candidates are positive integers, and combinations should be unique.
Brute Force Approach: Try all candidate multisets.
Optimized Approach: Use backtracking with sorted candidates and pruning.
Time Complexity: Exponential in target and candidate count.
Space Complexity: O(target)
Step-by-step Dry Run:
    recursively choose candidates starting from current index and reduce target.
Edge Cases: no combinations and target zero.
Common Mistakes: generating duplicate combinations and forgetting to sort.
Follow-up Interview Questions:
    1. How to modify for one-time use candidates?
    2. Can you return combinations in sorted order?
    3. What if negative candidates are allowed?
Alternative Approaches: Use DP to build combination sets.
Expected Output: The script prints unique combination sets for a sample input.
Key Takeaways: Backtracking with sorted input avoids duplicate combination generation.
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Use positive candidates repeatedly without mutating the input."""
    if any(value <= 0 for value in candidates):
        raise ValueError("Candidates must be positive.")
    values = sorted(set(candidates))
    result = []
    def search(start, remaining, path):
        if remaining == 0:
            result.append(path.copy())
            return
        for index in range(start, len(values)):
            value = values[index]
            if value > remaining:
                break
            path.append(value)
            search(index, remaining - value, path)
            path.pop()
    if target >= 0:
        search(0, target, [])
    return result
