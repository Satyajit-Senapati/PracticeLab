"""kth_largest_element.py

Problem Statement:
Implement a Python module that finds the k-th largest element in an unsorted list.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: selection algorithms, heap usage, partitioning,
quickselect
Real-world Use Case: Order statistics, leaderboard rankings, and percentile
analytics.
Input Description: Functions accept a list of integers and an integer k.
Output Description: Functions return the k-th largest element.
Example Inputs and Outputs:
    find_kth_largest([3,2,1,5,6,4], 2) -> 5
Constraints: Use O(n) average time for Quickselect or O(n log k) using a heap.
Brute Force Approach: Sort the list and index from the end.
Optimized Approach: Use a heap or Quickselect partitioning.
Time Complexity: O(n) average
Space Complexity: O(1) extra space for Quickselect or O(k) for heap.
Step-by-step Dry Run:
    nums = [3,2,1,5,6,4], k = 2
    return 5
Edge Cases: k equals 1, k equals len(nums), and duplicate values.
Common Mistakes: off-by-one errors, sorting the wrong direction, and
misinterpreting k as zero-based.
Follow-up Interview Questions:
    1. How does Quickselect compare to sorting for this problem?
    2. Can you find the k-th smallest instead?
    3. What happens on duplicate values?
Alternative Approaches: Use heapq.nlargest for a concise solution.
Expected Output: The script prints k-th largest elements for sample inputs.
Key Takeaways: Selection can be done faster than full sorting for fixed k.
"""

from __future__ import annotations

import heapq
from typing import List


def find_kth_largest_heap(nums: List[int], k: int) -> int:
    """Return the k-th largest element using a min-heap."""
    return heapq.nlargest(k, nums)[-1]


def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """Return the k-th largest element using Quickselect."""
    target = len(nums) - k

    def partition(left: int, right: int) -> int:
        pivot = nums[right]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index

    left, right = 0, len(nums) - 1
    while left <= right:
        pivot_index = partition(left, right)
        if pivot_index == target:
            return nums[pivot_index]
        if pivot_index < target:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

    raise ValueError("k is out of bounds")


def main() -> None:
    """Main function demonstrating k-th largest element selection."""
    examples = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([1], 1),
    ]
    for nums, k in examples:
        print(nums, "k=", k, "-> heap:", find_kth_largest_heap(nums, k), "quickselect:", find_kth_largest_quickselect(nums[:], k))


if __name__ == "__main__":
    main()
