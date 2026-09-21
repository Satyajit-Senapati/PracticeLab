"""maximum_subarray.py

Problem Statement:
Implement a Python module that finds the maximum contiguous subarray sum using
Kadane's algorithm.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, local/global maxima, array traversal,
edge-case handling
Real-world Use Case: Financial analysis, signal processing, and detecting
strongest continuous patterns in time series data.
Input Description: Functions accept a list of integers.
Output Description: Functions return the maximum subarray sum.
Example Inputs and Outputs:
    maximum_subarray([−2, 1, −3, 4, −1, 2, 1, −5, 4]) -> 6
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Check all subarrays with nested loops.
Optimized Approach: Use Kadane's algorithm to accumulate local maximum sums.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    return 6
Edge Cases: empty list, all negative values, and single-element lists.
Common Mistakes: resetting current sum incorrectly, ignoring all-negative
arrays, and using extra nested loops.
Follow-up Interview Questions:
    1. How can you recover the subarray boundaries?
    2. Can this algorithm be extended for 2D arrays?
    3. How does Kadane's algorithm relate to dynamic programming?
Alternative Approaches: Use prefix sums or divide and conquer for educational
purposes.
Expected Output: The script prints the maximum subarray sums for sample arrays.
Key Takeaways: Kadane's algorithm finds the maximum contiguous sum in linear
time.
"""

from __future__ import annotations

from typing import List


def maximum_subarray(values: List[int]) -> int:
    """Return the maximum contiguous subarray sum using Kadane's algorithm."""
    if not values:
        return 0

    max_current = values[0]
    max_global = values[0]

    for value in values[1:]:
        max_current = max(value, max_current + value)
        max_global = max(max_global, max_current)

    return max_global


def main() -> None:
    """Main function demonstrating maximum subarray examples."""
    examples = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, -2, 5],
        [-3, -2, -1, -4],
    ]
    for values in examples:
        print(values, "->", maximum_subarray(values))


if __name__ == "__main__":
    main()
