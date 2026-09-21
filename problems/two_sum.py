"""two_sum.py

Problem Statement:
Implement a Python module that solves the Two Sum problem: find two indices
whose values add up to a target sum.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hash maps, dictionaries, one-pass scanning, indexing,
edge-case handling
Real-world Use Case: Finding matching pairs in financial transactions,
recommender systems, and data matching tasks.
Input Description: Functions accept a list of integers and a target integer.
Output Description: Functions return a tuple of indices of the two numbers or
None when no valid pair exists.
Example Inputs and Outputs:
    two_sum([2, 7, 11, 15], 9) -> (0, 1)
    two_sum([3, 2, 4], 6) -> (1, 2)
Constraints: Use a dictionary for O(n) time complexity and avoid returning the
same element twice.
Brute Force Approach: Check every pair with nested loops.
Optimized Approach: Use a hash map to track seen values and their indices.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    values = [2, 7, 11, 15], target = 9
    seen = {}
    i=0, value=2, complement=7: store 2
    i=1, value=7, complement=2: found pair (0, 1)
Edge Cases: empty list, no pair found, duplicate values, and negative numbers.
Common Mistakes: not storing indices, checking the same element twice, and
returning values instead of indices.
Follow-up Interview Questions:
    1. How would you modify this for a sorted array?
    2. What if multiple pairs are valid?
    3. How can you find all unique pairs?
Alternative Approaches: Use sorting with two pointers or a brute-force nested
loop when n is small.
Expected Output: The script prints sample Two Sum results for example inputs.
Key Takeaways: Use a hash map to reduce Two Sum from O(n^2) to O(n).
"""

from __future__ import annotations

from typing import List, Optional, Tuple


def two_sum(values: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices of two numbers that add up to the target."""
    seen: dict[int, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None


def main() -> None:
    """Main function demonstrating two sum examples."""
    examples = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    for values, target in examples:
        print(values, target, "->", two_sum(values, target))


if __name__ == "__main__":
    main()
