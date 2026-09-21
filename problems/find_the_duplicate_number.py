"""find_the_duplicate_number.py

Problem Statement:
Find the duplicate number in an array containing n + 1 integers where each integer is between 1 and n.

Interview Difficulty: Medium
Commonly Asked By: Google, Uber, Microsoft
Concepts Tested: cycle detection, Floyd's tortoise and hare, pigeonhole principle.
Real-world Use Case: finding duplicates in constrained ID sequences.
Input Description: A list of integers with one repeated value.
Output Description: The duplicate integer.
Example Inputs and Outputs:
    [1,3,4,2,2] -> 2
Constraints: Do not modify the array and use O(1) extra space.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def find_duplicate(nums: list[int]) -> int:
    """Return the duplicate number using cycle detection."""
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


def main() -> None:
    examples = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
    ]
    for nums in examples:
        print(nums, "->", find_duplicate(nums))


if __name__ == "__main__":
    main()
