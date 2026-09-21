"""best_time_to_buy_and_sell_stock.py

Problem Statement:
Implement a Python module that computes the maximum profit from a single stock transaction.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: one-pass scanning, greedy approach, min tracking,
profit maximization
Real-world Use Case: Single-buy single-sell profit analysis and simplest stock trade planning.
Input Description: Function accepts a list of stock prices.
Output Description: Returns the maximum profit from one buy and one sell.
Example Inputs and Outputs:
    prices = [7,1,5,3,6,4] -> 5
Constraints: Sell must occur after buy.
Brute Force Approach: Compare all pairs of prices.
Optimized Approach: Track the minimum price and maximum profit while iterating.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    update min_price and compute profit at each price.
Edge Cases: decreasing prices yield 0 profit.
Common Mistakes: selling before buying or using negative profit.
Follow-up Interview Questions:
    1. How to support multiple transactions?
    2. What if there is a transaction fee?
    3. How to maximize profit with at most k transactions?
Alternative Approaches: Use dynamic programming for extended versions.
Expected Output: The script prints the max profit for a sample input.
Key Takeaways: A single pass with min tracking gives the optimal result.
"""

from __future__ import annotations

from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit


def main() -> None:
    print('Max profit:', max_profit([7, 1, 5, 3, 6, 4]))
    print('Max profit:', max_profit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    main()
