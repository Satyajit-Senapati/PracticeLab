"""find_peak_element.py

Problem Statement:
Implement a Python module that finds a peak element in an array where an
element is greater than its neighbors.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, array properties, problem constraints,
algorithmic reasoning
Real-world Use Case: Signal processing, local maxima detection, and
optimization in search tasks.
Input Description: Functions accept a list of integers.
Output Description: Functions return an index of any peak element.
Example Inputs and Outputs:
    find_peak_element([1,2,3,1]) -> 2
Constraints: Use O(log n) time. The array may contain multiple valid peaks.
Brute Force Approach: Scan and compare all neighbors.
Optimized Approach: Use binary search leveraging the guarantee of a peak.
Time Complexity: O(log n)
Space Complexity: O(1)
Step-by-step Dry Run:
    nums = [1, 2, 3, 1]
    returns index 2 or any valid peak index
Edge Cases: array length 1, strictly increasing arrays, and strictly
decreasing arrays.
Common Mistakes: using incorrect binary search bounds, failing to compare
neighbors, and not returning a valid peak.
Follow-up Interview Questions:
    1. Why does the binary search guarantee a peak?
    2. How can this be extended for multiple peaks?
    3. What are the differences between linear and binary search here?
Alternative Approaches: Linear scan yields O(n) time; binary search is
preferred for logarithmic time.
Expected Output: The script prints peak indices for sample arrays.
Key Takeaways: Binary search can find a peak element without checking every
position.
"""

from __future__ import annotations

from typing import List


def find_peak_element(nums: List[int]) -> int:
    """Return an index of any peak element in the array."""
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


def main() -> None:
    """Main function demonstrating peak element finding."""
    examples = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [5],
    ]
    for nums in examples:
        print(nums, "-> peak at index", find_peak_element(nums))


if __name__ == "__main__":
    main()
