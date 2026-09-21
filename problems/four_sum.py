"""four_sum.py

Problem Statement:
Find all unique quadruplets in an array that sum to a target value.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: sorting, two-pointer technique, k-sum.
Real-world Use Case: combinatorial search and multi-value matching.
Input Description: A list of integers and a target integer.
Output Description: A list of unique quadruplets that sum to target.
Example Inputs and Outputs:
    [1,0,-1,0,-2,2], target = 0 -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Constraints: Return unique quadruplets without duplicates.
Time Complexity: O(n^3)
Space Complexity: O(1) additional
"""

from __future__ import annotations


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    return result


def main() -> None:
    print(four_sum([1, 0, -1, 0, -2, 2], 0))
    print(four_sum([2, 2, 2, 2, 2], 8))


if __name__ == "__main__":
    main()
