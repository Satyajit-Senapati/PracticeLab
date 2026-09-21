"""circular_array_loop.py

Problem Statement:
Given an array of integers, determine if there is a cycle in the array where
all numbers in the cycle are either all positive or all negative.

Interview Difficulty: Medium
Commonly Asked By: Google, Facebook, Amazon
Concepts Tested: cycle detection, two pointers, modular indexing.
Real-world Use Case: detecting infinite loops in circular buffer navigation.
Input Description: A list of integers.
Output Description: True if a valid cycle exists.
Example Inputs and Outputs:
    [2,-1,1,2,2] -> True
    [-1,2] -> False
Constraints: Cycle must be longer than 1 and maintain direction.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def next_index(nums: list[int], current: int) -> int:
    """Compute the next index in the circular array."""
    n = len(nums)
    return (current + nums[current]) % n


def circular_array_loop(nums: list[int]) -> bool:
    """Return True if there is a valid cycle in the circular array."""
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            continue

        slow = i
        fast = i
        direction = nums[i] > 0

        while True:
            slow = next_index(nums, slow)
            fast = next_index(nums, fast)
            fast = next_index(nums, fast)
            if nums[slow] == 0 or nums[fast] == 0:
                break
            if (nums[slow] > 0) != direction or (nums[fast] > 0) != direction:
                break
            if slow == fast:
                if slow == next_index(nums, slow):
                    break
                return True

        marker = i
        while nums[marker] != 0 and (nums[marker] > 0) == direction:
            next_pos = next_index(nums, marker)
            nums[marker] = 0
            marker = next_pos

    return False


def main() -> None:
    examples = [
        [2, -1, 1, 2, 2],
        [-1, 2],
        [-2, 1, -1, -2, -2],
        [1, 1, 2],
    ]
    for nums in examples:
        print(f"{nums} -> {circular_array_loop(nums.copy())}")


if __name__ == "__main__":
    main()
