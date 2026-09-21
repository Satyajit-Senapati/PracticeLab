"""zigzag_conversion.py

Problem Statement:
Convert a string into a zigzag pattern on a given number of rows and read it line by line.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: simulation, string building, pattern traversal.
Real-world Use Case: formatting text for display or encoding.
Input Description: A string s and number of rows numRows.
Output Description: The zigzag-converted string.
Example Inputs and Outputs:
    "PAYPALISHIRING", 3 -> "PAHNAPLSIIGYIR"
Constraints: Handle numRows = 1 correctly.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def convert(s: str, num_rows: int) -> str:
    """Return the zigzag conversion of the string."""
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows: list[str] = ["" for _ in range(num_rows)]
    current_row = 0
    direction = 1

    for char in s:
        rows[current_row] += char
        if current_row == 0:
            direction = 1
        elif current_row == num_rows - 1:
            direction = -1
        current_row += direction

    return "".join(rows)


def main() -> None:
    examples = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
    ]
    for s, rows in examples:
        print(f"{s}, {rows} -> {convert(s, rows)}")


if __name__ == "__main__":
    main()
