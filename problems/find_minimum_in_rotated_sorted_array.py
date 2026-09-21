"""find_minimum_in_rotated_sorted_array.py

Problem Statement:
Implement a Python module that finds the minimum element in a rotated sorted array.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, rotated array properties, edge-case handling,
search space reduction
Real-world Use Case: Recovering the smallest element in circularly shifted sorted datasets and rotation-aware search.
Input Description: Function accepts a list of unique integers that was rotated.
Output Description: Returns the minimum integer in the rotated array.
Example Inputs and Outputs:
    nums = [3,4,5,1,2] -> 1
Constraints: Use O(log n) time.
Brute Force Approach: Scan all values to find minimum.
Optimized Approach: Binary search on the rotated array by comparing mid to high.
Time Complexity: O(log n)
Space Complexity: O(1)
Step-by-step Dry Run:
    if middle element is greater than high element, move left boundary right; otherwise move high boundary left.
Edge Cases: no rotation and one-element array.
Common Mistakes: not updating boundaries correctly or using linear search.
Follow-up Interview Questions:
    1. How to handle duplicate values?
    2. How does this compare to finding a target in a rotated sorted array?
    3. What is the effect of a fully sorted but unrotated array?
Alternative Approaches: Use linear scan for small arrays.
Expected Output: The script prints the minimum value for a sample rotated array.
Key Takeaways: Rotated sorted arrays allow binary search by inspecting the relation between mid and boundary elements.
"""

from __future__ import annotations

from typing import List


def find_min(nums: List[int]) -> int:
    """Return the minimum element in a rotated sorted array."""
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


def main() -> None:
    nums = [3, 4, 5, 1, 2]
    print("Minimum in rotated sorted array:", find_min(nums))


if __name__ == "__main__":
    main()
