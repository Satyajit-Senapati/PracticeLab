"""sort_colors.py

Problem Statement:
Implement a Python module that sorts an array containing 0s, 1s, and 2s in-place.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: two-pointer technique, in-place swapping, partitioning,
linear-time sorting
Real-world Use Case: Bucket sorting, categorizing items, and multi-way
partitioning in streaming data.
Input Description: Functions accept a list of integers containing only 0, 1,
and 2.
Output Description: Functions modify the list in-place to group values as
[0, 0, ..., 1, 1, ..., 2, 2, ...].
Example Inputs and Outputs:
    sort_colors([2,0,2,1,1,0]) -> [0,0,1,1,2,2]
Constraints: Use O(n) time and O(1) space; do not use built-in sorting.
Brute Force Approach: Count each value and write them back.
Optimized Approach: Use Dutch National Flag algorithm with three pointers.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    nums = [2,0,2,1,1,0]
    left=0, mid=0, right=5
    return [0,0,1,1,2,2]
Edge Cases: empty list, already sorted array, and all identical values.
Common Mistakes: incorrect pointer updates, swapping with wrong values, and
not handling 1s properly.
Follow-up Interview Questions:
    1. How would you generalize this to k colors?
    2. What invariant does the Dutch National Flag algorithm maintain?
    3. Can you solve this without counting sort?
Alternative Approaches: Use counting and reconstruction for clarity.
Expected Output: The script prints sorted arrays for sample inputs.
Key Takeaways: Three-way partitioning sorts the array in linear time and constant space.
"""

from __future__ import annotations

from typing import List


def sort_colors(nums: List[int]) -> None:
    """Sort the list of colors represented by 0, 1, and 2 in-place."""
    left = 0
    mid = 0
    right = len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1


def main() -> None:
    """Main function demonstrating sort colors."""
    examples = [
        [2, 0, 2, 1, 1, 0],
        [2, 2, 1, 0, 1, 0],
        [0, 1, 2, 0, 1, 2],
    ]
    for nums in examples:
        sort_colors(nums)
        print(nums)


if __name__ == "__main__":
    main()
