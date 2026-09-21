"""valid_sudoku.py

Problem Statement:
Implement a Python module that determines whether a partially filled 9x9 Sudoku
board is valid according to Sudoku rules.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: set membership, matrix traversal, constraint validation,
hashing
Real-world Use Case: Puzzle validation, configuration checks, and constraint
satisfaction.
Input Description: Functions accept a 9x9 list representing a Sudoku board.
Output Description: Functions return True if the board is valid, otherwise
False.
Example Inputs and Outputs:
    valid_sudoku(board) -> True
Constraints: Use O(1) space since board size is fixed, and O(81) time.
Brute Force Approach: Validate each row, column, and sub-box separately.
Optimized Approach: Track row, column, and box occupancy in one pass.
Time Complexity: O(1)
Space Complexity: O(1)
Step-by-step Dry Run:
    scan rows, columns, and 3x3 sub-boxes for duplicates
    return True if no duplicate digit appears
Edge Cases: empty board cells represented by ".", invalid digit placement,
and repeated values in a row, column, or box.
Common Mistakes: not combining row/column/box checks in one pass and
duplicating validation state.
Follow-up Interview Questions:
    1. How do you determine the 3x3 box index?
    2. Can you solve a full Sudoku puzzle with DFS backtracking?
    3. What changes if the board size varies?
Alternative Approaches: Use separate validation functions for rows, columns,
and boxes.
Expected Output: The script prints validation results for sample Sudoku boards.
Key Takeaways: One-pass coordinate tracking is sufficient for Sudoku validity.
"""

from __future__ import annotations

from typing import List


def valid_sudoku(board: List[List[str]]) -> bool:
    """Return True if the Sudoku board is valid."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            if value == ".":
                continue
            box_index = (row // 3) * 3 + (col // 3)
            if value in rows[row] or value in cols[col] or value in boxes[box_index]:
                return False
            rows[row].add(value)
            cols[col].add(value)
            boxes[box_index].add(value)

    return True


def main() -> None:
    """Main function demonstrating Sudoku board validation."""
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print("Valid board:", valid_sudoku(board))


if __name__ == "__main__":
    main()
