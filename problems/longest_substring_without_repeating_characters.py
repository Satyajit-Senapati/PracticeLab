"""longest_substring_without_repeating_characters.py

Problem Statement:
Find the length of the longest substring without repeating characters.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: sliding window, hash maps, string processing.
Real-world Use Case: substring analysis and input validation.
Input Description: A string s.
Output Description: The length of the longest substring without duplicates.
Example Inputs and Outputs:
    "abcabcbb" -> 3
Constraints: Use O(n) time with sliding window.
Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""

from __future__ import annotations


def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring without repeating characters."""
    last_seen: dict[str, int] = {}
    start = 0
    max_length = 0

    for index, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = index
        max_length = max(max_length, index - start + 1)

    return max_length


def main() -> None:
    examples = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
    ]
    for s in examples:
        print(f"{s} -> {length_of_longest_substring(s)}")


if __name__ == "__main__":
    main()
