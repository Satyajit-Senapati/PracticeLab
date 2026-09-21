"""rotate_string.py

Problem Statement:
Rotate a string in place by moving the first k characters to the end.

Interview Difficulty: Easy
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: string manipulation, slicing, rotation.
Real-world Use Case: cyclic shifts in text processing and buffer management.
Input Description: A string s and an integer k.
Output Description: The rotated string.
Example Inputs and Outputs:
    "abcdefg", 2 -> "cdefgab"
Constraints: Use O(n) time and O(n) space or in-place with extra care.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def rotate_string(s: str, k: int) -> str:
    """Return the string rotated left by k positions."""
    if not s:
        return s
    k %= len(s)
    return s[k:] + s[:k]


def main() -> None:
    examples = [
        ("abcdefg", 2),
        ("hello", 5),
        ("rotation", 3),
        ("", 4),
    ]
    for s, k in examples:
        print(f"{s} rotated by {k} -> {rotate_string(s, k)}")


if __name__ == "__main__":
    main()
