"""coin_change.py

Problem Statement:
Implement a Python module that finds the fewest number of coins needed to make up a target amount.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, unbounded knapsack, bottom-up computation,
minimum coin change
Real-world Use Case: Payment systems, resource allocation, and currency conversion.
Input Description: Function accepts a list of coin denominations and a target amount.
Output Description: Returns the minimum number of coins needed or -1 if impossible.
Example Inputs and Outputs:
    coins = [1,2,5], amount = 11 -> 3
Constraints: Use O(amount * n) time.
Brute Force Approach: Recursively try all coin combinations.
Optimized Approach: Use DP array to build solutions from 0 to amount.
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
Step-by-step Dry Run:
    initialize dp with amount+1 sentinel, dp[0] = 0, update dp[j] using coins.
Edge Cases: amount = 0 and unreachable amount.
Common Mistakes: not initializing unreachable state correctly or using greedy incorrectly.
Follow-up Interview Questions:
    1. How would you return the actual coins used?
    2. What if coin denominations are unlimited but sorted?
    3. Can greedy ever work here?
Alternative Approaches: Use BFS on amounts.
Expected Output: The script prints minimal coins needed for a sample input.
Key Takeaways: DP solves the change problem optimally when coins are unlimited.
"""

from __future__ import annotations

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1


def main() -> None:
    print("Fewest coins for 11:", coin_change([1, 2, 5], 11))


if __name__ == "__main__":
    main()
