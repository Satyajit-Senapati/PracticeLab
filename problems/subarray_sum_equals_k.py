from __future__ import annotations

from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    freq: dict[int, int] = defaultdict(int)
    freq[0] = 1

    for num in nums:
        prefix_sum += num
        count += freq[prefix_sum - k]
        freq[prefix_sum] += 1

    return count


def main() -> None:
    print('Subarrays sum to 2:', subarray_sum([1, 1, 1], 2))
    print('Subarrays sum to 3:', subarray_sum([1, 2, 3], 3))


if __name__ == '__main__':
    main()
"""subarray_sum_equals_k.py

Problem Statement:
Implement a Python module that counts the number of continuous subarrays whose sum equals k.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: prefix sum, hash map, subarray sums,
sum counting
Real-world Use Case: Counting specific-sum segments in financial time series, sensor readings, or event logs.
Input Description: Function accepts a list of integers and an integer k.
Output Description: Returns the number of continuous subarrays summing to k.
Example Inputs and Outputs:
    nums = [1,1,1], k = 2 -> 2
Constraints: Use O(n) time and O(n) space.
Brute Force Approach: Check all subarrays O(n^2).
Optimized Approach: Track prefix sum frequencies in a map.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    accumulate sum, count occurrences of sum-k previously seen.
Edge Cases: zero and negative numbers.
Common Mistakes: forgetting to count current prefix equal to k.
Follow-up Interview Questions:
    1. How to adapt for exact product instead of sum?
    2. What if only non-empty subarrays are allowed? (same answer)
    3. Can duplicates affect the counting method?
Alternative Approaches: Use cumulative sums with nested loops.
Expected Output: The script prints the number of subarrays summing to k for sample input.
Key Takeaways: Prefix sums plus frequency map gives linear-time subarray count.
"""
