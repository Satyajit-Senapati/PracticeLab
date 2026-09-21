"""longest_common_prefix.py

Problem Statement:
Implement a Python module that finds the longest common prefix among a list of
strings, including edge-case handling and efficient comparison.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string processing, pairwise comparison, edge cases,
iterative reduction, complexity analysis
Real-world Use Case: Autocomplete systems, search query optimization, and
common prefix detection for file paths or configuration keys.
Input Description: Functions accept a list of strings.
Output Description: Functions return the longest common prefix string.
Example Inputs and Outputs:
    longest_common_prefix(["flower", "flow", "flight"]) -> "fl"
    longest_common_prefix(["dog", "racecar", "car"]) -> ""
Constraints: Use efficient iteration, handle empty lists, and avoid unnecessary
repeated substring creation.
Brute Force Approach: Compare every prefix of every string.
Optimized Approach: Compare characters across strings only until mismatch.
Time Complexity: O(n * m) where n is number of strings and m is minimum string
length.
Space Complexity: O(m) for the prefix result.
Step-by-step Dry Run:
    values = ["flower", "flow", "flight"]
    return "fl"
Edge Cases: empty list, one string only, no common prefix, and identical
strings.
Common Mistakes: using the first string as the prefix without checking other
strings and failing to stop at the shortest string length.
Follow-up Interview Questions:
    1. How can you solve this using a trie?
    2. What is the complexity of a pairwise comparison approach?
    3. How does this problem change for a large number of strings?
Alternative Approaches: Use sorting and compare only first and last strings,
build a trie, or use Python’s `zip` over string characters.
Expected Output: The script prints the longest common prefix for sample lists.
Key Takeaways: Compare only as far as the shortest string and stop immediately
when mismatch occurs.
"""

from __future__ import annotations

from typing import List


def longest_common_prefix(strings: List[str]) -> str:
    """Return the longest common prefix among a list of strings."""
    if not strings:
        return ""

    shortest = min(strings, key=len)
    for index, char in enumerate(shortest):
        for other in strings:
            if other[index] != char:
                return shortest[:index]
    return shortest


def longest_common_prefix_zip(strings: List[str]) -> str:
    """Return the longest common prefix using zip to compare columns."""
    if not strings:
        return ""

    prefix_chars: list[str] = []
    for column in zip(*strings):
        if len(set(column)) == 1:
            prefix_chars.append(column[0])
        else:
            break
    return "".join(prefix_chars)


def main() -> None:
    """Main function demonstrating longest common prefix examples."""
    examples = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interview", "internet", "internal"],
    ]
    for strings in examples:
        print(strings, "->", longest_common_prefix(strings))
        print(strings, "zip ->", longest_common_prefix_zip(strings))


if __name__ == "__main__":
    main()
