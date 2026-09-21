"""three_sum.py

Problem Statement:
Implement a Python module that finds all unique triplets in an array that sum
to zero.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: sorting, two-pointer technique, duplicate handling,
array traversal, edge-case handling
Real-world Use Case: Finding balanced combinations in financial data,
correlation grouping, and subset-sum pattern discovery.
Input Description: Functions accept a list of integers.
Output Description: Functions return a list of unique triplets that sum to zero.
Example Inputs and Outputs:
    three_sum([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]]
Constraints: Avoid duplicate triplets, maintain O(n^2) time complexity, and
handle edge cases effectively.
Brute Force Approach: Check every triplet with nested loops.
Optimized Approach: Sort the array and use a two-pointer scan for each element.
Time Complexity: O(n^2)
Space Complexity: O(k) for output triplets.
Step-by-step Dry Run:
    sorted_list = [-4, -1, -1, 0, 1, 2]
    i=0, left=1, right=5 -> found [-1,-1,2]
    i=1, left=2, right=5 -> found [-1,0,1]
Edge Cases: empty list, fewer than three numbers, all zeros, and duplicate
values.
Common Mistakes: not skipping duplicates, failing to sort input, and returning
duplicate triplets.
Follow-up Interview Questions:
    1. Can you adapt this for a target sum other than zero?
    2. Why does sorting help with duplicate removal?
    3. How would you find all unique quadruplets?
Alternative Approaches: Use hashing for one-pass complements or brute-force
for small input sizes.
Expected Output: The script prints unique zero-sum triplets for sample input.
Key Takeaways: Sort and use two pointers to find unique triplets efficiently.
"""

from __future__ import annotations

from typing import List


def three_sum(values: List[int]) -> List[List[int]]:
    """Return all unique triplets that sum to zero."""
    values.sort()
    triplets: List[List[int]] = []

    for i in range(len(values) - 2):
        if i > 0 and values[i] == values[i - 1]:
            continue

        left, right = i + 1, len(values) - 1
        while left < right:
            total = values[i] + values[left] + values[right]
            if total == 0:
                triplets.append([values[i], values[left], values[right]])
                left += 1
                right -= 1
                while left < right and values[left] == values[left - 1]:
                    left += 1
                while left < right and values[right] == values[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets


def main() -> None:
    """Main function demonstrating Three Sum examples."""
    examples = [
        [-1, 0, 1, 2, -1, -4],
        [0, 0, 0, 0],
        [1, 2, -2, -1],
    ]
    for values in examples:
        print(values, "->", three_sum(values.copy()))


if __name__ == "__main__":
    main()
