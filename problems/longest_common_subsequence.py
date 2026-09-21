from __future__ import annotations

from typing import List


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


def main() -> None:
    print('LCS length:', longest_common_subsequence('abcde', 'ace'))
    print('LCS length:', longest_common_subsequence('abc', 'abc'))


if __name__ == '__main__':
    main()
"""longest_common_subsequence.py

Problem Statement:
Implement a Python module that computes the length of the longest common subsequence of two strings.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, 2D DP table, sequence comparison,
string matching
Real-world Use Case: Text diffing, version control merge tools, and biological sequence alignment.
Input Description: Function accepts two strings.
Output Description: Returns the length of the longest common subsequence.
Example Inputs and Outputs:
    text1 = "abcde", text2 = "ace" -> 3
Constraints: Use O(n*m) time and space.
Brute Force Approach: Explore all subsequence pairs.
Optimized Approach: Use a DP grid to compute LCS lengths iteratively.
Time Complexity: O(n*m)
Space Complexity: O(n*m)
Step-by-step Dry Run:
    dp[i][j] stores LCS length for prefixes of lengths i and j.
Edge Cases: empty strings.
Common Mistakes: confusing subsequence with substring.
Follow-up Interview Questions:
    1. How can you reduce space to O(min(n,m))?
    2. How does LCS differ from longest common substring?
    3. Can you reconstruct the subsequence itself?
Alternative Approaches: Use memoized recursion.
Expected Output: The script prints the LCS length for sample strings.
Key Takeaways: LCS is a classic 2D DP application for sequence alignment.
"""
