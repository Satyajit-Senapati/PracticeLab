"""search_a_2d_matrix.py

Problem Statement:
Implement a Python module that searches for a target value in a 2D matrix
where each row is sorted and the first element of each row is greater than
the last element of the previous row.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: matrix search, binary search, row/column indexing,
space-efficient traversal
Real-world Use Case: Searching sorted grid data, image scanning, and spatial
indexing.
Input Description: Functions accept a 2D list of integers and a target.
Output Description: Functions return True if the target exists, False otherwise.
Example Inputs and Outputs:
    search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) -> True
Constraints: Use O(log(m*n)) time with constant extra space.
Brute Force Approach: Scan every element.
Optimized Approach: Use binary search on the flattened index space.
Time Complexity: O(log(m*n))
Space Complexity: O(1)
Step-by-step Dry Run:
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    return True
Edge Cases: empty matrix, single-row matrix, target not present, and
single-element matrix.
Common Mistakes: incorrect index conversion, invalid mid calculation, and
not handling empty matrices.
Follow-up Interview Questions:
    1. How would you search a matrix sorted row-wise and column-wise?
    2. What if rows are sorted but columns are not?
    3. Can you avoid flattening the matrix in memory?
Alternative Approaches: Use row binary search then binary search inside the row.
Expected Output: The script prints search results for sample matrices.
Key Takeaways: Index math enables binary search across a logically flattened 2D matrix.
"""

from __future__ import annotations

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Return True if target exists in the sorted 2D matrix."""
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row_index = mid // cols
        col_index = mid % cols
        value = matrix[row_index][col_index]

        if value == target:
            return True
        if value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def main() -> None:
    """Main function demonstrating 2D matrix search."""
    examples = [
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            3,
        ),
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            13,
        ),
        ([[1]], 1),
    ]
    for matrix, target in examples:
        print(matrix, "target=", target, "->", search_matrix(matrix, target))


if __name__ == "__main__":
    main()
