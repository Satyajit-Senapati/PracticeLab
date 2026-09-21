"""minimum_cost_climbing_stairs.py

Problem Statement:
Implement a Python module that computes the minimum cost to climb stairs.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, state transition, bottom-up iteration,
minimum path cost
Real-world Use Case: Minimum energy or cost path in sequential processes and tiered pricing.
Input Description: Function accepts a list of stair costs.
Output Description: Returns the minimum cost to reach the top step.
Example Inputs and Outputs:
    cost = [10,15,20] -> 15
Constraints: You can start at step 0 or step 1 and climb one or two steps.
Brute Force Approach: Recursively compute cost for every path.
Optimized Approach: Use DP with two variables for previous costs.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    dp[i] = cost[i] + min(dp[i-1], dp[i-2]); answer is min(dp[n-1], dp[n-2]).
Edge Cases: two-step arrays and empty cost lists.
Common Mistakes: forgetting to allow starting at either step 0 or 1.
Follow-up Interview Questions:
    1. How does this change with variable step sizes?
    2. Can you reconstruct the chosen path?
    3. What if there is a cost to step off the top?
Alternative Approaches: Use recursion with memoization.
Expected Output: The script prints the minimum climbing cost for a sample list.
Key Takeaways: This is a simple DP problem with constant space possible.
"""

from __future__ import annotations

from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    n = len(cost)
    if n < 2:
        return 0
    first, second = cost[0], cost[1]
    for i in range(2, n):
        current = cost[i] + min(first, second)
        first, second = second, current
    return min(first, second)


def main() -> None:
    print("Minimum cost climbing stairs:", min_cost_climbing_stairs([10, 15, 20]))


if __name__ == "__main__":
    main()
