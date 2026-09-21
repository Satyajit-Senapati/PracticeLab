"""trapping_rain_water.py

Problem Statement:
Implement a Python module that computes the amount of rainwater trapped
between elevation bars.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: two-pointer technique, elevation profiles, boundary-based
aggregation, array traversal
Real-world Use Case: Modeling water accumulation in terrain analysis, flow
management, and hydrology simulations.
Input Description: Functions accept a list of non-negative integers
representing elevation heights.
Output Description: Functions return the total trapped water volume.
Example Inputs and Outputs:
    trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Compute trapped water at each position using left and
right maxima arrays.
Optimized Approach: Use a two-pointer scan with left and right boundaries.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    trapped = 6
    return 6
Edge Cases: empty elevation list, flat terrain, strictly rising or falling
elevations.
Common Mistakes: wrong pointer movement, using top-down maxima arrays with
extra space, and incorrect trapped water calculation per index.
Follow-up Interview Questions:
    1. How does the two-pointer strategy work here?
    2. Can you solve this using dynamic programming?
    3. How would you extend this to 2D terrain?
Alternative Approaches: Use precomputed left and right maxima arrays or
stack-based solutions.
Expected Output: The script prints trapped water totals for sample elevation
profiles.
Key Takeaways: Two-pointer scanning yields an optimal O(n) solution for this
classic problem.
"""

from __future__ import annotations

from typing import List


def trap(heights: List[int]) -> int:
    """Return the total water trapped between elevation bars."""
    left = 0
    right = len(heights) - 1
    left_max = 0
    right_max = 0
    trapped = 0

    while left < right:
        if heights[left] < heights[right]:
            left_max = max(left_max, heights[left])
            trapped += max(0, left_max - heights[left])
            left += 1
        else:
            right_max = max(right_max, heights[right])
            trapped += max(0, right_max - heights[right])
            right -= 1

    return trapped


def main() -> None:
    """Main function demonstrating rain water trapping."""
    examples = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [1, 2, 3, 4, 5],
    ]
    for heights in examples:
        print(heights, "->", trap(heights))


if __name__ == "__main__":
    main()
