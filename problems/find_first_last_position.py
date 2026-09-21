"""find_first_last_position.py

Problem Statement:
Implement a Python module that finds the first and last positions of a
target value in a sorted list.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, boundary search, sorted arrays, edge-case
analysis
Real-world Use Case: Search result spans, range queries, and indexed
value retrieval in sorted datasets.
Input Description: Functions accept a sorted list of integers and a target
value.
Output Description: Functions return a pair of indices [first, last] or [-1,
-1] if the target is not present.
Example Inputs and Outputs:
    search_range([5,7,7,8,8,10], 8) -> [3, 4]
Constraints: Use O(log n) time. Handle multiple occurrences.
Brute Force Approach: Scan the list and record the first and last positions.
Optimized Approach: Use binary search for both left and right boundaries.
Time Complexity: O(log n)
Space Complexity: O(1)
Step-by-step Dry Run:
    nums = [5,7,7,8,8,10], target = 8
    return [3, 4]
Edge Cases: empty list, no occurrences, single-element list, and all
matches.
Common Mistakes: using the same binary search for both bounds, off-by-one
errors, and returning wrong boundaries.
Follow-up Interview Questions:
    1. What changes for left-closed right-open intervals?
    2. How can you generalize this to find the first element >= target?
    3. Why is binary search still optimal here?
Alternative Approaches: Use linear scan for small arrays or unsorted data.
Expected Output: The script prints first and last positions for sample inputs.
Key Takeaways: Binary search can locate boundaries efficiently in sorted data.
"""

from __future__ import annotations

from typing import List


def _find_bound(nums: List[int], target: int, find_first: bool) -> int:
    left = 0
    right = len(nums) - 1
    bound = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            bound = mid
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return bound


def search_range(nums: List[int], target: int) -> List[int]:
    """Return the first and last position of target in sorted nums."""
    return [_find_bound(nums, target, True), _find_bound(nums, target, False)]


def main() -> None:
    """Main function demonstrating first and last position search."""
    examples = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([], 1),
    ]
    for nums, target in examples:
        print(nums, "target=", target, "->", search_range(nums, target))


if __name__ == "__main__":
    main()
