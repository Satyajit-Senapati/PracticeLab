"""three_sum_closest.py

Problem Statement:
Find three integers in an array whose sum is closest to a target value.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: sorting, two-pointer technique.
Real-world Use Case: optimization and closest-fit calculations.
Input Description: A list of integers and a target integer.
Output Description: The sum of three integers closest to the target.
Example Inputs and Outputs:
    [-1,2,1,-4], target = 1 -> 2
Constraints: Use O(n^2) time.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from __future__ import annotations


def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest - target):
                closest = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return closest


def main() -> None:
    print(three_sum_closest([-1, 2, 1, -4], 1))
    print(three_sum_closest([0, 0, 0], 1))


if __name__ == "__main__":
    main()
