"""top_k_frequent_elements.py

Problem Statement:
Implement a Python module that returns the k most frequent elements from a
list of integers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hashing, frequency counting, sorting, heap operations,
complexity analysis
Real-world Use Case: Recommender systems, trending event detection, and data
analytics.
Input Description: Functions accept a list of integers and an integer k.
Output Description: Functions return a list of the k most frequent elements.
Example Inputs and Outputs:
    top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2]
Constraints: Optimize for performance; focus on frequency counts and selection.
Brute Force Approach: Count frequency and sort all elements.
Optimized Approach: Use a heap or bucket sort for frequency selection.
Time Complexity: O(n log k) using a heap.
Space Complexity: O(n)
Step-by-step Dry Run:
    nums = [1,1,1,2,2,3], k=2
    return [1, 2]
Edge Cases: k equals list length, single element lists, and multiple elements
with the same frequency.
Common Mistakes: failing to handle k == 0, preserving output size, and using
inefficient sorting for large n.
Follow-up Interview Questions:
    1. How can bucket sort improve this solution?
    2. What if the input contains strings instead of integers?
    3. How do you handle ties in frequency?
Alternative Approaches: Use bucket sort for O(n) time if value ranges permit.
Expected Output: The script prints top k frequent elements for sample inputs.
Key Takeaways: Frequency counting plus an appropriate selection strategy
solves this efficiently.
"""

from __future__ import annotations

import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent elements from the list."""
    if k <= 0:
        return []

    frequency = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, frequency.items(), key=lambda pair: pair[1])]


def main() -> None:
    """Main function demonstrating top k frequent elements."""
    examples = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([4, 4, 4, 2, 2, 3, 3, 3], 2),
    ]
    for nums, k in examples:
        print(nums, "k=", k, "->", top_k_frequent(nums, k))


if __name__ == "__main__":
    main()
