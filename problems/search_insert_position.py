"""search_insert_position.py

Problem Statement:
Implement a Python module that returns the index where a target should be
inserted into a sorted list to maintain sorted order.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, sorted arrays, insertion index, edge-case
analysis
Real-world Use Case: Ordered list insertion, search engine ranking,
priority scheduling, and placement algorithms.
Input Description: Functions accept a sorted list of integers and a target.
Output Description: Functions return the index where the target should be
inserted.
Example Inputs and Outputs:
    search_insert([1,3,5,6], 5) -> 2
    search_insert([1,3,5,6], 2) -> 1
Constraints: Use O(log n) time. Maintain sorted order.
Brute Force Approach: Scan and compare values until the insertion point.
Optimized Approach: Use binary search to find the leftmost insertion index.
Time Complexity: O(log n)
Space Complexity: O(1)
Step-by-step Dry Run:
    nums = [1, 3, 5, 6], target = 2
    return 1
Edge Cases: empty list, target smaller than all elements, target larger than
all elements.
Common Mistakes: off-by-one errors, incorrect mid updates, and not returning
leftmost index.
Follow-up Interview Questions:
    1. How would this change for duplicates if you wanted first insertion
       position?
    2. How does bisect_left differ from bisect_right?
    3. Can this be used to find lower and upper bounds?
Alternative Approaches: Use Python's bisect module for a concise solution.
Expected Output: The script prints insertion positions for sample inputs.
Key Takeaways: Binary search yields the correct insert position in logarithmic
time.
"""

from __future__ import annotations

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """Return the index where target should be inserted into the sorted list."""
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def main() -> None:
    """Main function demonstrating search insert position."""
    examples = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([], 1),
    ]
    for nums, target in examples:
        print(nums, "target=", target, "->", search_insert(nums, target))


if __name__ == "__main__":
    main()
