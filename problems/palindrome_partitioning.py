"""palindrome_partitioning.py

Problem Statement:
Implement a Python module that returns all palindrome partitioning combinations of a string.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, palindrome checking, recursion,
string partitioning
Real-world Use Case: Text segmentation, palindrome-based grouping, and search problem generation.
Input Description: Function accepts a string.
Output Description: Returns a list of lists of strings where each partition is a palindrome.
Example Inputs and Outputs:
    s = "aab" -> [["a","a","b"],["aa","b"]]
Constraints: Explore all partitions using DFS.
Brute Force Approach: Generate all partitions and filter palindromes.
Optimized Approach: Backtrack while validating palindrome prefixes.
Time Complexity: O(n * 2^n)
Space Complexity: O(n)
Step-by-step Dry Run:
    recursively partition string, append current partition when end reached.
Edge Cases: empty string and all identical characters.
Common Mistakes: not copying the current path list before recursion.
Follow-up Interview Questions:
    1. How to return the minimum palindrome partition count?
    2. Can you use DP to speed up palindrome checks?
    3. What is the time complexity?
Alternative Approaches: Use DP table for palindrome substrings.
Expected Output: The script prints all palindrome partitions for a sample string.
Key Takeaways: Backtracking generates valid partitions effectively when combined with palindrome pruning.
"""

from __future__ import annotations

from typing import List


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def partition(s: str) -> List[List[str]]:
    result: List[List[str]] = []
    current: List[str] = []

    def backtrack(start: int) -> None:
        if start == len(s):
            result.append(current.copy())
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end)
                current.pop()

    backtrack(0)
    return result


def main() -> None:
    print('Partitions for aab:', partition('aab'))


if __name__ == '__main__':
    main()
