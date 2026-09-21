"""binary_search.py

Problem Statement:
Implement a Python module that performs binary search on a sorted list.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search, sorting prerequisites, divide-and-conquer,
logarithmic complexity
Real-world Use Case: Searching sorted datasets, looking up values in ordered
indices, and performance-critical query operations.
Input Description: Functions accept a sorted list of integers and a target.
Output Description: Functions return the index of the target or -1 if not found.
Example Inputs and Outputs:
    binary_search([1,2,3,4,5], 3) -> 2
Constraints: The list must be sorted. Use O(log n) time.
Brute Force Approach: Scan each element linearly.
Optimized Approach: Use binary search to divide the search space by half.
Time Complexity: O(log n)
Space Complexity: O(1)
Step-by-step Dry Run:
    nums = [1, 2, 3, 4, 5], target = 3
    return 2
Edge Cases: empty list, target smaller than all elements, target larger than
all elements.
Common Mistakes: infinite loops due to wrong mid computation, off-by-one
errors, and failing to handle empty arrays.
Follow-up Interview Questions:
    1. What are the iterative and recursive versions?
    2. How does integer overflow affect mid computation in some languages?
    3. Can binary search be applied to other monotonic predicates?
Alternative Approaches: Linear search for unsorted data or small arrays.
Expected Output: The script prints binary search results on sample inputs.
Key Takeaways: Binary search is the canonical O(log n) lookup algorithm.
"""

from __future__ import annotations

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Return the index of target in sorted nums, or -1 if not found."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main() -> None:
    """Main function demonstrating binary search."""
    examples = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 6),
        ([], 1),
    ]
    for nums, target in examples:
        print(nums, "target=", target, "->", binary_search(nums, target))


if __name__ == "__main__":
    main()
