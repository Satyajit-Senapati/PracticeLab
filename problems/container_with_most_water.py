"""container_with_most_water.py

Problem Statement:
Implement a Python module that computes the maximum amount of water that can
be contained between two lines in an elevation map.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: two-pointer technique, area calculation, greedy selection,
array traversal
Real-world Use Case: Optimizing container shapes, selecting bounds for
resource allocation, and identifying maximum capacity intervals.
Input Description: Functions accept a list of non-negative integers representing
line heights.
Output Description: Functions return the maximum container area.
Example Inputs and Outputs:
    max_area([1,8,6,2,5,4,8,3,7]) -> 49
Constraints: Use O(n) time and O(1) space, move pointers intelligently, and
handle varying heights.
Brute Force Approach: Check every pair and compute area.
Optimized Approach: Use two pointers moving inward from both ends.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    heights = [1,8,6,2,5,4,8,3,7]
    max_area = 49
    return 49
Edge Cases: empty list, two heights only, and monotonic height lists.
Common Mistakes: moving the wrong pointer, not computing area correctly, and
using extra space unnecessarily.
Follow-up Interview Questions:
    1. Why can we move the shorter pointer?
    2. How does this compare to brute-force complexity?
    3. What if heights are strictly increasing?
Alternative Approaches: Use brute force for small input or binary search for
alternative reasoning.
Expected Output: The script prints maximum container areas for sample inputs.
Key Takeaways: Two-pointer scanning yields an optimal solution for maximum
container area.
"""

from __future__ import annotations

from typing import List


def max_area(heights: List[int]) -> int:
    """Return the maximum area that can be contained by two lines."""
    left = 0
    right = len(heights) - 1
    max_area_value = 0

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        max_area_value = max(max_area_value, height * width)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area_value


def main() -> None:
    """Main function demonstrating container with most water."""
    examples = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [4, 3, 2, 1, 4],
    ]
    for heights in examples:
        print(heights, "->", max_area(heights))


if __name__ == "__main__":
    main()
