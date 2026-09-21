"""maximal_rectangle.py

Problem Statement:
Implement a Python module that finds the largest rectangle containing only 1's in a binary matrix.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack, histogram area, dynamic programming, matrix traversal,
monotonic stack
Real-world Use Case: Image processing for largest contiguous regions, layout optimization,
and occupancy grid analysis.
Input Description: Function accepts a matrix of '0' and '1' characters.
Output Description: Returns the area of the largest rectangle containing only '1's.
Example Inputs and Outputs:
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] -> 6
Constraints: Use O(m*n) time.
Brute Force Approach: Check all possible rectangles.
Optimized Approach: Convert each row to histogram heights and solve maximal rectangle in histogram.
Time Complexity: O(m * n)
Space Complexity: O(n)
Step-by-step Dry Run:
    update heights for each row, compute max rectangle in histogram using a stack.
Edge Cases: empty matrix and all zeros.
Common Mistakes: forgetting sentinel bars for stack processing.
Follow-up Interview Questions:
    1. How does this relate to largest rectangle in histogram?
    2. Can you solve it in-place?
    3. What if the matrix uses integers instead of strings?
Alternative Approaches: Use dynamic programming with left/right boundaries.
Expected Output: The script prints the maximal rectangle area for a sample matrix.
Key Takeaways: Histogram reduction and monotonic stack yield the optimal solution.
"""

from __future__ import annotations

from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    stack: List[int] = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


def maximal_rectangle(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0] * n
    max_area = 0

    for row in matrix:
        for j, val in enumerate(row):
            heights[j] = heights[j] + 1 if val == "1" else 0
        max_area = max(max_area, largest_rectangle_area(heights))

    return max_area


def main() -> None:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print("Maximal rectangle area:", maximal_rectangle(matrix))


if __name__ == "__main__":
    main()
