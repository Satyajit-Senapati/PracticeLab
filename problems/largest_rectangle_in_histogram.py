"""largest_rectangle_in_histogram.py

Problem Statement:
Implement a Python module that finds the largest rectangle area in a histogram.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack-based computation, monotonic stacks, area calculation,
array traversal
Real-world Use Case: Layout engines, skyline analysis, and maximum-area
queries in histograms.
Input Description: Functions accept a list of non-negative integers representing
bar heights.
Output Description: Functions return the largest rectangle area.
Example Inputs and Outputs:
    largest_rectangle([2,1,5,6,2,3]) -> 10
Constraints: Use O(n) time and O(n) space with a monotonic stack.
Brute Force Approach: Check every rectangle range with nested loops.
Optimized Approach: Use a stack to compute nearest smaller bars.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    heights = [2,1,5,6,2,3]
    return 10
Edge Cases: empty histogram, single bar, and monotonically increasing or
decreasing bars.
Common Mistakes: incorrect stack indexing, missing sentinel values, and not
clearing bars correctly.
Follow-up Interview Questions:
    1. How does the monotonic stack work in this problem?
    2. Can this be adapted to maximal rectangle in a matrix?
    3. What if heights are floating point values?
Alternative Approaches: Use divide and conquer with O(n log n) time.
Expected Output: The script prints largest rectangle areas for sample histograms.
Key Takeaways: A monotonic stack enables linear-time maximal rectangle area computation.
"""

from __future__ import annotations

from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    """Return the largest rectangle area in the histogram."""
    stack: List[int] = []
    max_area = 0
    padded_heights = heights + [0]

    for index, height in enumerate(padded_heights):
        while stack and padded_heights[stack[-1]] > height:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, padded_heights[top] * width)
        stack.append(index)

    return max_area


def main() -> None:
    """Main function demonstrating largest rectangle in histogram."""
    examples = [
        [2, 1, 5, 6, 2, 3],
        [2, 4],
        [1, 1, 1, 1],
    ]
    for heights in examples:
        print(heights, "->", largest_rectangle_area(heights))


if __name__ == "__main__":
    main()
