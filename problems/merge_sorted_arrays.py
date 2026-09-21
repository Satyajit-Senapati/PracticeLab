"""merge_sorted_arrays.py

Problem Statement:
Implement a Python module that merges two sorted arrays into a single sorted
array.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: merge algorithm, sorted input, two-pointer technique,
array traversal
Real-world Use Case: Merging sorted result sets, combining time series data,
and merging sorted partitions during ETL processing.
Input Description: Functions accept two sorted lists of integers.
Output Description: Functions return a merged sorted list.
Example Inputs and Outputs:
    merge_sorted_arrays([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
Constraints: Assume inputs are already sorted, avoid additional sorting,
and preserve stability for equal elements.
Brute Force Approach: Concatenate and sort both lists.
Optimized Approach: Use a two-pointer merge to combine sorted lists in O(n)
time.
Time Complexity: O(n + m)
Space Complexity: O(n + m)
Step-by-step Dry Run:
    first = [1, 3], second = [2, 4]
    merged = [1, 2, 3, 4]
    return [1, 2, 3, 4]
Edge Cases: one list empty, both lists empty, duplicate values, and varying
lengths.
Common Mistakes: using insert at front of list, re-sorting output, and not
handling leftover elements.
Follow-up Interview Questions:
    1. How does this merge step relate to merge sort?
    2. Can you merge in-place if one array has buffer space?
    3. What is the stable property of this merge?
Alternative Approaches: Use built-in `heapq.merge` or sorted concatenation for
small datasets.
Expected Output: The script prints merged sorted arrays for sample inputs.
Key Takeaways: Merge sorted lists efficiently with a pointer-based scan.
"""

from __future__ import annotations

from typing import List


def merge_sorted_arrays(first: List[int], second: List[int]) -> List[int]:
    """Return a merged sorted list from two sorted input lists."""
    merged: List[int] = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    if i < len(first):
        merged.extend(first[i:])
    if j < len(second):
        merged.extend(second[j:])

    return merged


def main() -> None:
    """Main function demonstrating sorted array merging."""
    examples = [
        ([1, 3, 5], [2, 4, 6]),
        ([], [1, 2, 3]),
        ([1, 2], []),
        ([1, 3, 5], [1, 2, 4]),
    ]
    for first, second in examples:
        print(first, second, "->", merge_sorted_arrays(first, second))


if __name__ == "__main__":
    main()
