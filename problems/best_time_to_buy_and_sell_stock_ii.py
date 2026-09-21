"""best_time_to_buy_and_sell_stock_ii.py

Problem Statement:
Implement a Python module that computes the maximum profit from as many stock transactions as desired.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: greedy profits, local peaks, sum of positive differences,
multiple transactions
Real-world Use Case: Unlimited trade profit extraction in stock analysis and simplified trading strategy.
Input Description: Function accepts a list of stock prices.
Output Description: Returns the maximum total profit from multiple buy/sell transactions.
Example Inputs and Outputs:
    prices = [7,1,5,3,6,4] -> 7
Constraints: You must sell before you buy again.
Brute Force Approach: Try all transaction combinations.
Optimized Approach: Sum all positive day-to-day gains.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    add price difference whenever a later price is higher than the previous.
Edge Cases: always decreasing prices yield 0 profit.
Common Mistakes: missing adjacent gains or overlapping transactions.
Follow-up Interview Questions:
    1. How to handle transaction fees?
    2. What if there is a cooldown period?
    3. How to limit to at most k transactions?
Alternative Approaches: Use DP for fee/cooldown variants.
Expected Output: The script prints the max profit for sample inputs.
Key Takeaways: Summing positive rises captures all valid unlimited transactions.
"""

from __future__ import annotations

from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def main() -> None:
    print('Max profit II:', max_profit([7, 1, 5, 3, 6, 4]))
    print('Max profit II:', max_profit([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
