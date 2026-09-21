"""word_break.py

Problem Statement:
Implement a Python module that determines whether a string can be segmented
into a space-separated sequence of dictionary words.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, memoization, substring matching,
string decomposition
Real-world Use Case: Natural language processing, spell checking, input
validation, and tokenization.
Input Description: Functions accept a string and a list of dictionary words.
Output Description: Functions return True if the string can be segmented,
otherwise False.
Example Inputs and Outputs:
    word_break("leetcode", ["leet", "code"]) -> True
    word_break("applepenapple", ["apple", "pen"]) -> True
Constraints: Use O(n^2) time in the DP solution and O(n) space.
Brute Force Approach: Explore all segmentations recursively.
Optimized Approach: Use dynamic programming or memoized recursion.
Time Complexity: O(n^2)
Space Complexity: O(n)
Step-by-step Dry Run:
    s = "leetcode", word_dict = ["leet","code"]
    return True
Edge Cases: empty string, unreachable string tail, and repeated words.
Common Mistakes: failing to memoize, using wrong substring indices, and not
checking all partition points.
Follow-up Interview Questions:
    1. How would you return one valid segmentation?
    2. How does this relate to the knapsack problem?
    3. Can you optimize using a trie?
Alternative Approaches: Use recursion with memoization or BFS over positions.
Expected Output: The script prints segmentation results for sample strings.
Key Takeaways: DP over string positions is a reliable way to solve segmentation problems.
"""

from __future__ import annotations

from typing import List, Set


def word_break(s: str, word_dict: List[str]) -> bool:
    """Return True if the string can be segmented into dictionary words."""
    word_set: Set[str] = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[-1]


def main() -> None:
    """Main function demonstrating word break segmentation."""
    examples = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ]
    for s, word_dict in examples:
        print(s, "->", word_break(s, word_dict))


if __name__ == "__main__":
    main()
