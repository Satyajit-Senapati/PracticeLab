"""unique_paths.py

Problem Statement:
Implement a Python module that calculates the number of unique paths in a grid from the top-left to the bottom-right cell.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, combinatorics, grid traversal,
path counting
Real-world Use Case: Robot path planning, grid navigation metrics, and combinatorial route counting.
Input Description: Function accepts two integers m and n for grid dimensions.
Output Description: Returns the number of unique paths using only right and down moves.
Example Inputs and Outputs:
    m = 3, n = 7 -> 28
Constraints: Use O(m*n) time and O(min(m,n)) space.
Brute Force Approach: Recursively explore all paths.
Optimized Approach: Use DP with current-row state or combinatorics.
Time Complexity: O(m*n)
Space Complexity: O(n)
Step-by-step Dry Run:
    dp[j] = dp[j] + dp[j-1] for each cell in row-major order.
Edge Cases: m = 1 or n = 1.
Common Mistakes: using 0-index miscounts or 2D array when a 1D array suffices.
Follow-up Interview Questions:
    1. How many paths with obstacles?
    2. Can you derive this using binomial coefficients?
    3. What if diagonal moves are allowed?
Alternative Approaches: Use combinatorial formula C(m+n-2, m-1).
Expected Output: The script prints the number of unique paths for a sample grid.
Key Takeaways: This is a classic DP problem with simple state transition.
"""

from __future__ import annotations

from typing import List


def unique_paths(m: int, n: int) -> int:
    dp: List[int] = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


def main() -> None:
    print("Unique paths 3x7:", unique_paths(3, 7))


if __name__ == "__main__":
    main()
