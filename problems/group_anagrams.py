"""group_anagrams.py

Problem Statement:
Implement a Python module that groups anagrams together from a list of
strings.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hashing, sorting, grouping, dictionary usage,
string normalization
Real-world Use Case: Grouping search queries, finding duplicate listings,
organizing text records, and text clustering.
Input Description: Functions accept a list of strings.
Output Description: Functions return lists of grouped anagram strings.
Example Inputs and Outputs:
    group_anagrams(["eat","tea","tan","ate","nat","bat"]) -> [["eat","tea","ate"],["tan","nat"],["bat"]]
Constraints: Preserve anagram groups efficiently and handle empty strings.
Brute Force Approach: Compare each string against every other string.
Optimized Approach: Use sorted characters or frequency signatures as keys.
Time Complexity: O(n * m log m) for sorting each string.
Space Complexity: O(n * m)
Step-by-step Dry Run:
    words = ["eat","tea","tan","ate","nat","bat"]
    return [["eat","tea","ate"], ["tan","nat"], ["bat"]]
Edge Cases: empty input list, single string, duplicates, and strings with
multiple anagrams.
Common Mistakes: not normalizing case, using wrong dictionary keys, and
returning ungrouped results.
Follow-up Interview Questions:
    1. How can you optimize for a fixed alphabet?
    2. What is the difference between sorting and counting approaches?
    3. How would you preserve input order within groups?
Alternative Approaches: Use character frequency tuples as dictionary keys or
hashing based on letter counts.
Expected Output: The script prints grouped anagram lists for sample input.
Key Takeaways: Use hashing and normalization to group anagrams in linear
pass time aside from sorting overhead.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Tuple


def group_anagrams(words: List[str]) -> List[List[str]]:
    """Group strings that are anagrams of each other."""
    groups: Dict[Tuple[str, ...], List[str]] = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def group_anagrams_by_count(words: List[str]) -> List[List[str]]:
    """Group anagrams using character count signatures."""
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())


def main() -> None:
    """Main function demonstrating anagram grouping."""
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped anagrams:", group_anagrams(words))
    print("Grouped anagrams by count:", group_anagrams_by_count(words))


if __name__ == "__main__":
    main()
