from __future__ import annotations

from typing import Tuple


def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0

    def expand(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        left1, right1 = expand(i, i)
        left2, right2 = expand(i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end + 1]


def main() -> None:
    print('Longest palindrome:', longest_palindrome('babad'))
    print('Longest palindrome:', longest_palindrome('cbbd'))


if __name__ == '__main__':
    main()
"""longest_palindromic_substring.py

Problem Statement:
Implement a Python module that finds the longest palindromic substring in a given string.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: expand around center, palindrome checking, string scanning,
substring search
Real-world Use Case: Text analysis, pattern matching, and palindrome-based search utilities.
Input Description: Function accepts a string.
Output Description: Returns the longest palindromic substring.
Example Inputs and Outputs:
    s = "babad" -> "bab" or "aba"
Constraints: Use O(n^2) time and O(1) extra space.
Brute Force Approach: Check all substrings for palindromes.
Optimized Approach: Expand around each center to find palindromes.
Time Complexity: O(n^2)
Space Complexity: O(1)
Step-by-step Dry Run:
    for each index, expand around odd and even centers.
Edge Cases: empty string and all identical characters.
Common Mistakes: incorrectly handling even-length palindromes.
Follow-up Interview Questions:
    1. How can Manacher's algorithm improve this?
    2. What if you need the count of all palindromic substrings?
    3. Can you handle Unicode characters?
Alternative Approaches: Use dynamic programming or Manacher's algorithm.
Expected Output: The script prints the longest palindromic substring for sample input.
Key Takeaways: Center expansion is a simple and effective palindrome search technique.
"""
