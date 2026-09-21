"""top_k_frequent_words.py

Problem Statement:
Implement a Python module that returns the k most frequent words from a list.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hashing, heap, sorting, frequency counts,
string ordering
Real-world Use Case: Search query analytics, autocomplete ranking, and text summarization.
Input Description: Function accepts a list of words and an integer k.
Output Description: Returns the k most frequent words sorted by frequency and lexicographically.
Example Inputs and Outputs:
    words = ["i","love","leetcode","i","love","coding"], k = 2 -> ["i","love"]
Constraints: Use O(n log k) time.
Brute Force Approach: Sort all words by frequency and lexicographic order.
Optimized Approach: Use frequency dictionary with a heap or bucket sort.
Time Complexity: O(n log k)
Space Complexity: O(n)
Step-by-step Dry Run:
    count each word, push into a min-heap keyed by frequency and word ordering,
    pop until k remain.
Edge Cases: k equals unique word count or words list empty.
Common Mistakes: incorrect lexicographic tie-breaker.
Follow-up Interview Questions:
    1. How to return top k frequent numbers instead of words?
    2. Can you solve it with bucket sort?
    3. What if k is much smaller than the number of unique words?
Alternative Approaches: Use sorted frequency list.
Expected Output: The script prints the top k frequent words for a sample input.
Key Takeaways: Use a heap to maintain top k frequencies while respecting tie-break rules.
"""

from __future__ import annotations

from heapq import heappush, heappop
from typing import List


def top_k_frequent(words: List[str], k: int) -> List[str]:
    count: dict[str, int] = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    heap: List[tuple[int, str]] = []
    for word, freq in count.items():
        heappush(heap, (-freq, word))

    result: List[str] = []
    for _ in range(min(k, len(heap))):
        result.append(heappop(heap)[1])
    return result


def main() -> None:
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print("Top 2 frequent words:", top_k_frequent(words, 2))


if __name__ == "__main__":
    main()
