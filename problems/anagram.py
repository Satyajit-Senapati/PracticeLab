"""anagram.py

Problem Statement:
Implement a Python module that checks whether pairs of strings are anagrams,
including normalization and use of frequency counts.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string normalization, sorting, frequency counting,
edge-case handling, text comparison
Real-world Use Case: Detecting duplicate content, matching user input,
verifying search synonyms, and processing text records in ETL workflows.
Input Description: Functions accept two strings and optional normalization flags.
Output Description: Functions return boolean results indicating anagram
status.
Example Inputs and Outputs:
    is_anagram("listen", "silent") -> True
    is_anagram("triangle", "integral") -> True
    is_anagram("hello", "world") -> False
Constraints: Handle empty strings, ignore whitespace and punctuation
optionally, and preserve case-insensitive comparisons.
Brute Force Approach: Generate all permutations of one string and compare.
Optimized Approach: Normalize and compare sorted strings or character counts.
Time Complexity: O(n log n) for sorting and O(n) for frequency counting.
Space Complexity: O(n) for normalized strings or count dictionaries.
Step-by-step Dry Run:
    first = "listen"
    second = "silent"
    return True
Edge Cases: different lengths, empty strings, non-alphanumeric characters,
and case variations.
Common Mistakes: using permutations, ignoring whitespace, and performing
case-sensitive comparisons accidentally.
Follow-up Interview Questions:
    1. Which approach is faster: sorting or counting?
    2. How do you handle Unicode characters in anagram checks?
    3. Can you detect anagrams for large inputs efficiently?
Alternative Approaches: Use sorted strings, Counter frequency maps, or
hashing strategies for performance.
Expected Output: The script prints anagram check results for sample inputs.
Key Takeaways: Normalize text and compare frequency information rather than
using exponential permutation approaches.
"""

from __future__ import annotations

import re
from collections import Counter


def normalize_text(text: str, ignore_non_alphanumeric: bool = True) -> str:
    """Normalize text for anagram checking."""
    normalized = text.lower().strip()
    if ignore_non_alphanumeric:
        normalized = re.sub(r"[^a-z0-9]", "", normalized)
    return normalized


def is_anagram(first: str, second: str, ignore_non_alphanumeric: bool = True) -> bool:
    """Return True if the two strings are anagrams."""
    normalized_first = normalize_text(first, ignore_non_alphanumeric)
    normalized_second = normalize_text(second, ignore_non_alphanumeric)
    if len(normalized_first) != len(normalized_second):
        return False
    return Counter(normalized_first) == Counter(normalized_second)


def is_anagram_sorted(first: str, second: str, ignore_non_alphanumeric: bool = True) -> bool:
    """Return True if the two strings are anagrams using sorting."""
    normalized_first = normalize_text(first, ignore_non_alphanumeric)
    normalized_second = normalize_text(second, ignore_non_alphanumeric)
    return sorted(normalized_first) == sorted(normalized_second)


def main() -> None:
    """Main function demonstrating anagram checks."""
    examples = [
        ("listen", "silent"),
        ("triangle", "integral"),
        ("hello", "world"),
    ]
    for first, second in examples:
        print(first, second, "->", is_anagram(first, second))
        print(first, second, "sorted ->", is_anagram_sorted(first, second))


if __name__ == "__main__":
    main()
