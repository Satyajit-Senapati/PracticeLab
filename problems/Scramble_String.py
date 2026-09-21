"""Scramble_String.py

Problem Statement:
Determine whether one string is a scramble of another using recursive partitioning.

Interview Difficulty: Hard
Commonly Asked By: Facebook, Google
Concepts Tested: recursion, memoization, string partitioning.
Real-world Use Case: approximate string matching and structural transformations.
Input Description: Two strings s1 and s2 of equal length.
Output Description: True if s2 is a scramble of s1.
Example Inputs and Outputs:
    s1 = "great", s2 = "rgeat" -> True
Constraints: Strings have equal length and contain lowercase letters.
Time Complexity: O(n^4) with memoization.
Space Complexity: O(n^3)
"""

from __future__ import annotations

from functools import lru_cache


def is_scramble(s1: str, s2: str) -> bool:
    """Return True if s2 is a scramble of s1."""
    @lru_cache(maxsize=None)
    def check(a: str, b: str) -> bool:
        if a == b:
            return True
        if sorted(a) != sorted(b):
            return False

        n = len(a)
        for i in range(1, n):
            if (check(a[:i], b[:i]) and check(a[i:], b[i:])):
                return True
            if (check(a[:i], b[n - i:]) and check(a[i:], b[:n - i])):
                return True
        return False

    return check(s1, s2)


def main() -> None:
    print(is_scramble("great", "rgeat"))
    print(is_scramble("abcde", "caebd"))


if __name__ == "__main__":
    main()
