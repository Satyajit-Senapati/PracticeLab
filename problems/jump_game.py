"""jump_game.py

Problem Statement:
Implement a Python module that determines if you can reach the last index in an array.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: greedy algorithms, jump coverage, array traversal,
reachability
Real-world Use Case: Network packet reachability, range coverage, and movement planning.
Input Description: Function accepts a list of non-negative integers representing max jump lengths.
Output Description: Returns True if the last index is reachable, otherwise False.
Example Inputs and Outputs:
    nums = [2,3,1,1,4] -> True
    nums = [3,2,1,0,4] -> False
Constraints: Use O(n) time.
Brute Force Approach: Try all jump combinations recursively.
Optimized Approach: Maintain the farthest reachable index while iterating.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    update reachable = max(reachable, i + nums[i]), return False if i exceeds reachable.
Edge Cases: empty array and single-element array.
Common Mistakes: not checking reachability before using current element.
Follow-up Interview Questions:
    1. How to compute minimum jumps instead?
    2. Can you prove greedy correctness?
    3. What if backward jumps are allowed?
Alternative Approaches: Use BFS on index graph.
Expected Output: The script prints reachability for sample arrays.
Key Takeaways: Greedy coverage tracking can solve jump reachability efficiently.
"""

from __future__ import annotations

from typing import List


def can_jump(nums: List[int]) -> bool:
    reachable = 0
    for i, jump in enumerate(nums):
        if i > reachable:
            return False
        reachable = max(reachable, i + jump)
    return True


def main() -> None:
    print("Can jump [2,3,1,1,4]:", can_jump([2, 3, 1, 1, 4]))
    print("Can jump [3,2,1,0,4]:", can_jump([3, 2, 1, 0, 4]))


if __name__ == "__main__":
    main()
