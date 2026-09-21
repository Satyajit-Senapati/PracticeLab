"""majority_element.py

Problem Statement:
Find the majority element in a list of integers, where the majority element appears more than n/2 times.

Interview Difficulty: Easy
Commonly Asked By: Google, Microsoft, Amazon
Concepts Tested: Boyer-Moore Voting Algorithm, counting.
Real-world Use Case: identifying frequently occurring items in data streams.
Input Description: A list of integers.
Output Description: The majority element.
Example Inputs and Outputs:
    [3,2,3] -> 3
Constraints: Assume the majority element always exists.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def majority_element(nums: list[int]) -> int:
    """Return the element that appears more than half the time."""
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


def main() -> None:
    examples = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]
    for nums in examples:
        print(nums, "->", majority_element(nums))


if __name__ == "__main__":
    main()
