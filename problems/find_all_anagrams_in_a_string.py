"""find_all_anagrams_in_a_string.py

Problem Statement:
Find all start indices of p's anagrams in s.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: sliding window, frequency counting, string matching.
Real-world Use Case: substring pattern detection and text search.
Input Description: Strings s and p.
Output Description: A list of starting indices of p's anagrams in s.
Example Inputs and Outputs:
    s = "cbaebabacd", p = "abc" -> [0, 6]
Constraints: Use O(n) time with fixed alphabet size.
Time Complexity: O(n)
Space Complexity: O(1) for character counts.
"""

from __future__ import annotations


def find_anagrams(s: str, p: str) -> list[int]:
    """Return starting indices of p's anagrams in s."""
    if len(p) > len(s):
        return []

    target = [0] * 26
    window = [0] * 26
    for ch in p:
        target[ord(ch) - ord('a')] += 1
    for ch in s[: len(p)]:
        window[ord(ch) - ord('a')] += 1

    result: list[int] = []
    if window == target:
        result.append(0)

    for i in range(len(p), len(s)):
        window[ord(s[i]) - ord('a')] += 1
        window[ord(s[i - len(p)]) - ord('a')] -= 1
        if window == target:
            result.append(i - len(p) + 1)

    return result


def main() -> None:
    examples = [
        ("cbaebabacd", "abc"),
        ("abab", "ab"),
        ("af", "be"),
    ]
    for s, p in examples:
        print(f"{s}, {p} -> {find_anagrams(s, p)}")


if __name__ == "__main__":
    main()
