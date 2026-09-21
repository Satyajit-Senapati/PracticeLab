"""search_a_2d_matrix_ii.py

Problem Statement:
Search for a target value in a matrix where each row and each column is sorted ascending.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: matrix search, two-pointer elimination.
Real-world Use Case: searching sorted grid data and spatial lookup.
Input Description: A 2D list and a target integer.
Output Description: True if target exists in the matrix.
Example Inputs and Outputs:
    matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 5 -> True
Constraints: Use O(m + n) time.
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from __future__ import annotations


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Return True if target is found in the sorted matrix."""
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False


def main() -> None:
    matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17],
    ]
    print(search_matrix(matrix, 5))
    print(search_matrix(matrix, 15))


if __name__ == "__main__":
    main()
