"""rotate_image.py

Problem Statement:
Rotate a square matrix by 90 degrees clockwise in place.

Interview Difficulty: Easy
Commonly Asked By: Google, Amazon, Microsoft, Apple
Concepts Tested: matrix transformation, in-place modification, transposition,
index mapping
Real-world Use Case: image rotation in computer graphics and layout engines.
Input Description: An n x n matrix of integers.
Output Description: The matrix is modified in place to represent the rotated
output.
Example Inputs and Outputs:
    [[1,2,3],[4,5,6],[7,8,9]] -> [[7,4,1],[8,5,2],[9,6,3]]
Constraints: Modify the matrix with O(1) extra space.
Time Complexity: O(n^2)
Space Complexity: O(1)
Edge Cases: n == 1, low n values, in-place matrix mutation.
"""

from __future__ import annotations


def rotate(matrix: list[list[int]]) -> None:
    """Rotate the matrix 90 degrees clockwise in place."""
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()


def main() -> None:
    """Main function demonstrating matrix rotation."""
    examples = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    ]
    for matrix in examples:
        print("Before:")
        for row in matrix:
            print(row)
        rotate(matrix)
        print("After:")
        for row in matrix:
            print(row)
        print()


if __name__ == "__main__":
    main()
