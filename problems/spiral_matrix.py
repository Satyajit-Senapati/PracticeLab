"""spiral_matrix.py

Problem Statement:
Return all elements of a matrix in spiral order.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Facebook, Microsoft
Concepts Tested: matrix traversal, boundary management, loop invariants.
Real-world Use Case: reading 2D data in a directional scan order.
Input Description: A 2D list of integers.
Output Description: A list of integers in spiral order.
Example Inputs and Outputs:
    [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
Constraints: Traverse each element exactly once.
Time Complexity: O(m*n)
Space Complexity: O(m*n) for the output list.
"""

from __future__ import annotations


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return the matrix elements in spiral order."""
    if not matrix or not matrix[0]:
        return []

    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def main() -> None:
    """Main function demonstrating spiral order traversal."""
    examples = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[]],
    ]
    for matrix in examples:
        print(matrix, "->", spiral_order(matrix))


if __name__ == "__main__":
    main()
