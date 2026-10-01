"""search_a_2d_matrix_iii.py

Problem Statement:
Search for a target value in a matrix where each row and each column is sorted ascending,
returning whether the target exists.

Interview Difficulty: Hard
Commonly Asked By: Google, Amazon
Concepts Tested: binary search, matrix traversal, divide-and-conquer.
Real-world Use Case: efficient lookup in sorted 2D data.
Input Description: A 2D list and a target integer.
Output Description: True if the target exists in the matrix.
Example Inputs and Outputs:
    matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 5 -> True
Constraints: The matrix has sorted rows and columns.
Time Complexity: O(m log n) or O(n log m)
Space Complexity: O(1)
"""

from __future__ import annotations


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Return True if the target is found in the sorted matrix."""
    if not matrix or not matrix[0]:
        return False

    # Row ranges can overlap; a failed search in one row does not rule out others.
    return any(row and row[0] <= target <= row[-1] and binary_search(row, target)
               for row in matrix)


def binary_search(row: list[int], target: int) -> bool:
    left, right = 0, len(row) - 1
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == target:
            return True
        if row[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
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
