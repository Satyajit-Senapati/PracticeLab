"""substring_search.py

Problem Statement:
Implement a Python module that finds the first occurrence of a substring in a
string using the Knuth-Morris-Pratt algorithm and a simple brute-force fallback.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: substring search, pattern matching, prefix function,
KMP algorithm, string scanning
Real-world Use Case: Searching for patterns in logs, text processing,
search indexing, and data validation workflows.
Input Description: Functions accept a haystack string and a needle string.
Output Description: Functions return the starting index of the first occurrence
or -1 if the substring is not found.
Example Inputs and Outputs:
    find_substring("hello", "ll") -> 2
    find_substring("aaaaa", "bba") -> -1
Constraints: Use O(n + m) time search for the KMP implementation, handle empty
needles, and preserve correct index semantics.
Brute Force Approach: Check every possible starting index.
Optimized Approach: Use the KMP prefix function for efficient pattern search.
Time Complexity: O(n + m)
Space Complexity: O(m)
Step-by-step Dry Run:
    haystack = "abcxabcdabxabcdabcdabcy"
    needle = "abcdabcy"
    return 15
Edge Cases: empty needle, empty haystack, needle longer than haystack,
and repeated patterns.
Common Mistakes: incorrect prefix table construction, off-by-one errors,
and failing to handle empty needle.
Follow-up Interview Questions:
    1. How does KMP improve over brute force?
    2. What is the prefix function used for?
    3. Can you implement this with Boyer-Moore or Rabin-Karp?
Alternative Approaches: Use Python’s built-in `find()` for practical use,
Boyer-Moore for large alphabets, or Rabin-Karp for multiple pattern search.
Expected Output: The script prints substring search results for sample input.
Key Takeaways: Use KMP for efficient deterministic substring search with good
worst-case performance.
"""

from __future__ import annotations

from typing import List


def build_kmp_prefix_table(pattern: str) -> List[int]:
    """Build the prefix table for the KMP algorithm."""
    prefix_table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            prefix_table[i] = j
    return prefix_table


def find_substring(haystack: str, needle: str) -> int:
    """Return the first index of needle in haystack using KMP, or -1."""
    if not needle:
        return 0
    if not haystack or len(needle) > len(haystack):
        return -1

    prefix_table = build_kmp_prefix_table(needle)
    j = 0
    for i, char in enumerate(haystack):
        while j > 0 and char != needle[j]:
            j = prefix_table[j - 1]
        if char == needle[j]:
            j += 1
            if j == len(needle):
                return i - j + 1
    return -1


def find_substring_bruteforce(haystack: str, needle: str) -> int:
    """Return the first index of needle in haystack using brute force."""
    if not needle:
        return 0
    if not haystack or len(needle) > len(haystack):
        return -1

    for start in range(len(haystack) - len(needle) + 1):
        if haystack[start:start + len(needle)] == needle:
            return start
    return -1


def main() -> None:
    """Main function demonstrating substring search."""
    pairs = [
        ("hello", "ll"),
        ("aaaaa", "bba"),
        ("abcxabcdabxabcdabcdabcy", "abcdabcy"),
    ]
    for haystack, needle in pairs:
        print(haystack, needle, "->", find_substring(haystack, needle))
        print(haystack, needle, "brute force ->", find_substring_bruteforce(haystack, needle))


if __name__ == "__main__":
    main()
