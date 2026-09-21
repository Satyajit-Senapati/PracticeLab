"""word_break_ii.py

Problem Statement:
Return all possible sentences from a string that can be segmented into a sequence
of dictionary words.

Interview Difficulty: Hard
Commonly Asked By: Google, Amazon
Concepts Tested: recursion, memoization, dynamic programming.
Real-world Use Case: text segmentation and natural language processing.
Input Description: A string s and a list of valid words.
Output Description: All valid sentences formed by spaces inserted between words.
Example Inputs and Outputs:
    s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    -> ["cats and dog","cat sand dog"]
Constraints: Return all sentences in any order.
Time Complexity: exponential in the worst case with memoization.
Space Complexity: O(n * K)
"""

from __future__ import annotations

from functools import lru_cache


def word_break_ii(s: str, word_dict: list[str]) -> list[str]:
    """Return all possible sentences that segment the string into dictionary words."""
    word_set = set(word_dict)

    @lru_cache(maxsize=None)
    def sentences(start: int) -> list[str]:
        if start == len(s):
            return [""]

        result: list[str] = []
        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if prefix in word_set:
                for suffix in sentences(end):
                    if suffix:
                        result.append(prefix + " " + suffix)
                    else:
                        result.append(prefix)
        return result

    return sentences(0)


def main() -> None:
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(word_break_ii(s, word_dict))


if __name__ == "__main__":
    main()
