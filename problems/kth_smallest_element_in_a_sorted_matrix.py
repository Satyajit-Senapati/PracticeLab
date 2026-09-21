"""kth_smallest_element_in_a_sorted_matrix.py

Problem Statement:
Implement a Python module that finds the kth smallest element in a sorted matrix.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, matrix properties, row/column ordering,
search space pruning
Real-world Use Case: Ranking values in matrix-structured datasets, map queries, and matrix analytics.
Input Description: Function accepts an n x n matrix with each row and column sorted,
and an integer k.
Output Description: Returns the kth smallest element in the matrix.
Example Inputs and Outputs:
    matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 -> 13
Constraints: Use O(n log m) time or O(k log n) with a min-heap.
Brute Force Approach: Flatten and sort all values.
Optimized Approach: Use binary search on the value range with counting.
Time Complexity: O(n log(max-min))
Space Complexity: O(1)
Step-by-step Dry Run:
    binary search over possible values and count how many are <= mid each row.
Edge Cases: k = 1 and k = n*n.
Common Mistakes: using row count incorrectly or not handling duplicates.
Follow-up Interview Questions:
    1. How to use a heap instead of binary search?
    2. What if the matrix is not square?
    3. Can you find kth largest instead?
Alternative Approaches: Use a min-heap seeded with one element per row.
Expected Output: The script prints the kth smallest value for a sample matrix.
Key Takeaways: Sorted matrix structure enables counting-based binary search.
"""

from __future__ import annotations

from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    """Return the kth smallest element in a sorted matrix."""
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]

    def count_less_equal(mid: int) -> int:
        count = 0
        for row in matrix:
            left, right = 0, n
            while left < right:
                mid_index = (left + right) // 2
                if row[mid_index] <= mid:
                    left = mid_index + 1
                else:
                    right = mid_index
            count += left
        return count

    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low


def main() -> None:
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    print("8th smallest:", kth_smallest(matrix, 8))


if __name__ == "__main__":
    main()
