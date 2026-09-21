"""longest_palindrome.py

Problem Statement:
Implement a Python module that finds the longest palindromic substring in a
string using center expansion.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string manipulation, palindrome detection, dynamic expansion,
edge-case handling, algorithm design
Real-world Use Case: Detecting symmetric patterns in text, DNA sequences,
and substring search within text processing workflows.
Input Description: Functions accept a single string.
Output Description: Functions return the longest palindromic substring.
Example Inputs and Outputs:
    longest_palindrome("babad") -> "bab" or "aba"
    longest_palindrome("cbbd") -> "bb"
Constraints: Use an efficient O(n^2) center expansion solution, handle empty
strings, and preserve exact input substrings.
Brute Force Approach: Check every substring for palindrome status.
Optimized Approach: Expand around each potential palindrome center.
Time Complexity: O(n^2)
Space Complexity: O(1)
Step-by-step Dry Run:
    value = "babad"
    longest = "bab"
    return "bab"
Edge Cases: empty string, one-character string, repeated characters, and
multiple equal-length palindromes.
Common Mistakes: ignoring even-length palindromes, overlapping center logic,
and off-by-one errors in substring slicing.
Follow-up Interview Questions:
    1. How does the center expansion algorithm work?
    2. Can this be solved in O(n) time?
    3. How would you handle very large inputs?
Alternative Approaches: Use dynamic programming, Manacher’s algorithm, or
suffix tree approaches for more advanced solutions.
Expected Output: The script prints the longest palindromic substrings for sample
inputs.
Key Takeaways: Expand around each center and account for both odd and even
palindromes.
"""

from __future__ import annotations

from typing import Tuple


def _expand_around_center(text: str, left: int, right: int) -> Tuple[int, int]:
    """Expand around the given center and return the palindrome bounds."""
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return left + 1, right


def longest_palindrome(text: str) -> str:
    """Return the longest palindromic substring."""
    if not text:
        return ""

    start, end = 0, 1
    for index in range(len(text)):
        left1, right1 = _expand_around_center(text, index, index)
        left2, right2 = _expand_around_center(text, index, index + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return text[start:end]


def main() -> None:
    """Main function demonstrating longest palindrome substring examples."""
    examples = ["babad", "cbbd", "a", "racecar", "forgeeksskeegfor"]
    for example in examples:
        print(example, "->", longest_palindrome(example))


if __name__ == "__main__":
    main()
