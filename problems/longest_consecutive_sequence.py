"""longest_consecutive_sequence.py

Problem Statement:
Implement a Python module that finds the length of the longest consecutive sequence in an unsorted integer array.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hash set usage, sequence expansion, OR time complexity,
value neighbor search
Real-world Use Case: Finding longest streaks in event timestamps, sorted identifiers, or numeric logs.
Input Description: Function accepts an unsorted list of integers.
Output Description: Returns the length of the longest consecutive integer sequence.
Example Inputs and Outputs:
    nums = [100,4,200,1,3,2] -> 4
Constraints: Use O(n) time and O(n) space.
Brute Force Approach: Sort the array then scan for consecutive runs.
Optimized Approach: Use a hash set and only expand sequences from smallest starters.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    add values to set, then for each value not preceded by val-1, expand forward.
Edge Cases: empty list and single value.
Common Mistakes: expanding from every value instead of only sequence starts.
Follow-up Interview Questions:
    1. Can you do it in-place while preserving O(n) time?
    2. How does this change if duplicates are allowed?
    3. How would you return the actual sequence rather than length?
Alternative Approaches: Sort then count consecutive runs in O(n log n).
Expected Output: The script prints the longest consecutive sequence length for sample input.
Key Takeaways: Starting from the smallest value in each sequence avoids redundant work.
"""

from __future__ import annotations

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """Return the length of the longest consecutive sequence."""
    values = set(nums)
    longest = 0

    for num in values:
        if num - 1 not in values:
            length = 1
            while num + length in values:
                length += 1
            longest = max(longest, length)

    return longest


def main() -> None:
    print("Longest consecutive length:", longest_consecutive([100, 4, 200, 1, 3, 2]))


if __name__ == "__main__":
    main()
