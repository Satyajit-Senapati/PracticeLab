"""minimum_window_substring.py

Problem Statement:
Implement a Python module that returns the smallest window in a string that
contains all characters of another string.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: sliding window, two pointers, hash maps, substring coverage
Real-world Use Case: search query matching, document analysis, and text
extraction.
Input Description: Functions accept a source string and a target string.
Output Description: Functions return the minimum window substring or an empty
string if no such window exists.
Example Inputs and Outputs:
    min_window("ADOBECODEBANC", "ABC") -> "BANC"
Constraints: Use O(n + m) time with a sliding window and character frequency
tracking.
Brute Force Approach: Check every possible substring.
Optimized Approach: Use two pointers with a frequency counter to expand and
contract the window.
Time Complexity: O(n + m)
Space Complexity: O(m)
Step-by-step Dry Run:
    s = "ADOBECODEBANC", t = "ABC"
    return "BANC"
Edge Cases: empty source, target longer than source, and no valid window.
Common Mistakes: not shrinking the window correctly, mishandling frequency
counts, and forgetting required character matches.
Follow-up Interview Questions:
    1. How can you optimize memory for large character sets?
    2. What if the characters must appear in order?
    3. Can you adapt this for Unicode strings?
Alternative Approaches: Use custom counters or char arrays for fixed alphabets.
Expected Output: The script prints minimum windows for sample string pairs.
Key Takeaways: Use sliding-window frequency matching to locate minimal substrings.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Dict


def min_window(s: str, t: str) -> str:
    """Return the minimum window in s that contains all characters of t."""
    if not s or not t or len(t) > len(s):
        return ""

    required: Dict[str, int] = Counter(t)
    window_counts: Dict[str, int] = defaultdict(int)
    required_matches = len(required)
    formed = 0
    left = 0
    right = 0
    min_length = float("inf")
    min_window_start = 0

    while right < len(s):
        character = s[right]
        window_counts[character] += 1

        if character in required and window_counts[character] == required[character]:
            formed += 1

        while left <= right and formed == required_matches:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window_start = left

            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in required and window_counts[left_char] < required[left_char]:
                formed -= 1
            left += 1

        right += 1

    return "" if min_length == float("inf") else s[min_window_start : min_window_start + min_length]


def main() -> None:
    """Main function demonstrating minimum window substring."""
    examples = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
    ]
    for s, t in examples:
        print(f"s={s}, t={t} -> {min_window(s, t)!r}")


if __name__ == "__main__":
    main()
