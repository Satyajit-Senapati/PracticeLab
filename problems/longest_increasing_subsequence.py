"""longest_increasing_subsequence.py

Problem Statement:
Implement a Python module that finds the length of the longest strictly
increasing subsequence in an array.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, binary search, patience sorting,
subsequence vs. substring
Real-world Use Case: Sequence analysis, stock trading, pattern discovery, and
data trend detection.
Input Description: Functions accept a list of integers.
Output Description: Functions return the length of the longest increasing
subsequence.
Example Inputs and Outputs:
    length_of_lis([10,9,2,5,3,7,101,18]) -> 4
Constraints: Use O(n log n) time and O(n) space for the optimized solution.
Brute Force Approach: Check all subsequences using bitmasks.
Optimized Approach: Use dynamic programming with binary search on tail values.
Time Complexity: O(n log n)
Space Complexity: O(n)
Step-by-step Dry Run:
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    return 4
Edge Cases: empty list, single element list, and decreasing sequences.
Common Mistakes: confusing subsequences with subarrays, using O(n^2)
dynamic programming when O(n log n) is expected, and not handling duplicate
values.
Follow-up Interview Questions:
    1. How do you reconstruct the actual subsequence?
    2. Why does the patience sorting approach work?
    3. What if non-strictly increasing subsequences were allowed?
Alternative Approaches: O(n^2) DP can be used for smaller input sizes.
Expected Output: The script prints LIS lengths for sample arrays.
Key Takeaways: Binary search over tail values yields optimal LIS length
computation.
"""

from __future__ import annotations

import bisect
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    if not nums:
        return 0

    tails: List[int] = []
    for num in nums:
        index = bisect.bisect_left(tails, num)
        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num
    return len(tails)


def main() -> None:
    """Main function demonstrating LIS computation."""
    examples = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
    ]
    for nums in examples:
        print(nums, "-> LIS length", length_of_lis(nums))


if __name__ == "__main__":
    main()
