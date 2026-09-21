"""sliding_window_maximum.py

Problem Statement:
Implement a Python module that finds the maximum value in each sliding window
of size k over a list of integers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: deque optimization, sliding window technique, amortized
complexity, and sequence processing
Real-world Use Case: Time series peak detection, signal monitoring, and
windowed analytics.
Input Description: Functions accept a list of integers and window size k.
Output Description: Functions return a list of maximums for each sliding window.
Example Inputs and Outputs:
    max_sliding_window([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
Constraints: Use O(n) time by maintaining a deque of candidate indices.
Brute Force Approach: Compute the maximum for every window using scanning.
Optimized Approach: Use a monotonic deque to keep track of visible maximums.
Time Complexity: O(n)
Space Complexity: O(k)
Step-by-step Dry Run:
    values = [1,3,-1,-3,5,3,6,7], k=3
    result = [3,3,5,5,6,7]
Edge Cases: empty list, k <= 0, k = 1, and k equals list length.
Common Mistakes: failing to pop outdated indices, using incorrect deque order,
and scanning each window explicitly.
Follow-up Interview Questions:
    1. How would you adapt this for minimum values?
    2. Can this be used for dynamic window sizes?
    3. What is the deque invariant maintained here?
Alternative Approaches: Use priority queue with lazy deletion, but with higher complexity.
Expected Output: The script prints sliding window maximums for sample inputs.
Key Takeaways: A monotonic deque yields linear time sliding window maximums.
"""

from __future__ import annotations

from collections import deque
from typing import Deque, List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """Return maximums for each sliding window of size k."""
    if k <= 0 or not nums:
        return []

    result: List[int] = []
    window: Deque[int] = deque()

    for i, value in enumerate(nums):
        while window and window[0] <= i - k:
            window.popleft()
        while window and nums[window[-1]] < value:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


def main() -> None:
    """Main function demonstrating sliding window maximum."""
    examples = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([9, 11], 2),
        ([4, -2], 1),
    ]
    for nums, k in examples:
        print(nums, "k=", k, "->", max_sliding_window(nums, k))


if __name__ == "__main__":
    main()
