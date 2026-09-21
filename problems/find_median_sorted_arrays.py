"""find_median_sorted_arrays.py

Problem Statement:
Implement a Python module that finds the median of two sorted arrays.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, array partitioning, median selection,
edge-case handling
Real-world Use Case: Statistical analysis on merged datasets, sensor fusion,
and online analytics.
Input Description: Functions accept two sorted lists of integers.
Output Description: Functions return the median value as a float.
Example Inputs and Outputs:
    find_median_sorted_arrays([1,3], [2]) -> 2.0
    find_median_sorted_arrays([1,2], [3,4]) -> 2.5
Constraints: Use O(log(min(m,n))) time and constant extra space.
Brute Force Approach: Merge both arrays and compute median.
Optimized Approach: Use binary search to partition arrays correctly.
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
Step-by-step Dry Run:
    nums1=[1,3], nums2=[2]
    return 2.0
Edge Cases: empty arrays, different lengths, and one array much larger.
Common Mistakes: wrong partitioning logic, handling odd/even total length,
and not using the smaller array for binary search.
Follow-up Interview Questions:
    1. Why partition on the smaller array?
    2. How does this relate to median of a single sorted array?
    3. Can this method be adapted for more than two arrays?
Alternative Approaches: Merge into one array in O(m+n) time for simpler
implementation.
Expected Output: The script prints median values for sample inputs.
Key Takeaways: Careful partitioning yields an optimal median-of-two-sorted-arrays
solution.
"""

from __future__ import annotations

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """Return the median of two sorted arrays."""
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float("inf") if partition_x == x else nums1[partition_x]

        max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float("inf") if partition_y == y else nums2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
            return float(max(max_left_x, max_left_y))
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1

    raise ValueError("Input arrays are not sorted or invalid.")


def main() -> None:
    """Main function demonstrating median of two sorted arrays."""
    examples = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([], [1]),
    ]
    for nums1, nums2 in examples:
        print(nums1, nums2, "->", find_median_sorted_arrays(nums1, nums2))


if __name__ == "__main__":
    main()
