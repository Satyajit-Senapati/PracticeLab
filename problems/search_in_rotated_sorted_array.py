"""search_in_rotated_sorted_array.py

Problem Statement:
Implement a Python module that searches for a target value in a rotated sorted array.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, rotated array analysis, conditional logic,
index mapping
Real-world Use Case: Querying circularly shifted indexes and searching rotated time series data.
Input Description: Function accepts a list of unique integers and a target value.
Output Description: Returns the index of the target or -1 if not found.
Example Inputs and Outputs:
    nums = [4,5,6,7,0,1,2], target = 0 -> 4
Constraints: Use O(log n) time.
Brute Force Approach: Scan all values.
Optimized Approach: Use binary search by determining sorted half.
Time Complexity: O(log n)
Space Complexity: O(1)
Step-by-step Dry Run:
    determine which half is sorted and narrow the search interval accordingly.
Edge Cases: empty array, target at boundaries.
Common Mistakes: using mid comparisons incorrectly or failing when the pivot is at the ends.
Follow-up Interview Questions:
    1. How do duplicates change the approach?
    2. Can you find the rotation pivot first, then search normally?
    3. What if the array is not rotated at all?
Alternative Approaches: Find pivot then binary search in the correct subarray.
Expected Output: The script prints the index of the target for sample input.
Key Takeaways: Rotated sorted array search requires identifying the sorted region each iteration.
"""

from __future__ import annotations

from typing import List


def search(nums: List[int], target: int) -> int:
    """Return the index of target in a rotated sorted array or -1 if not found."""
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def main() -> None:
    nums = [4, 5, 6, 7, 0, 1, 2]
    print("Index of 0:", search(nums, 0))
    print("Index of 3:", search(nums, 3))


if __name__ == "__main__":
    main()
