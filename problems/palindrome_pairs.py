"""palindrome_pairs.py

Problem Statement:
Find all pairs of indices such that the concatenation of two words is a palindrome.

Interview Difficulty: Hard
Commonly Asked By: Google, Facebook
Concepts Tested: hashing, palindrome checks, string manipulation.
Real-world Use Case: palindrome search and phrase generation.
Input Description: A list of unique words.
Output Description: List of index pairs [i, j] where words[i] + words[j] is a palindrome.
Example Inputs and Outputs:
    ["bat","tab","cat"] -> [[0,1],[1,0]]
Constraints: Words are unique and lower-case.
Time Complexity: O(k^2 * n) where k is number of words and n is length.
Space Complexity: O(k * n)
"""

from __future__ import annotations


def palindrome_pairs(words: list[str]) -> list[list[int]]:
    """Return index pairs that form palindromic concatenations."""
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    lookup = {word[::-1]: i for i, word in enumerate(words)}
    answers: list[list[int]] = []

    for i, word in enumerate(words):
        for cut in range(len(word) + 1):
            prefix, suffix = word[:cut], word[cut:]
            if prefix in lookup and lookup[prefix] != i and is_palindrome(suffix):
                answers.append([i, lookup[prefix]])
            if cut != len(word) and suffix in lookup and lookup[suffix] != i and is_palindrome(prefix):
                answers.append([lookup[suffix], i])

    return answers


def main() -> None:
    print(palindrome_pairs(["bat", "tab", "cat"]))
    print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))


if __name__ == "__main__":
    main()
