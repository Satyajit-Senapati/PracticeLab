"""jump_game_ii.py

Problem Statement:
Implement a Python module that computes the minimum number of jumps to reach the last index.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: greedy interval expansion, BFS-like layer traversal,
minimum steps
Real-world Use Case: Minimum move planning, routing optimization, and resource allocation.
Input Description: Function accepts a list of non-negative integers representing max jump lengths.
Output Description: Returns the minimum number of jumps required to reach the last index.
Example Inputs and Outputs:
    nums = [2,3,1,1,4] -> 2
Constraints: Use O(n) time.
Brute Force Approach: BFS over reachable indexes.
Optimized Approach: Use greedy layer expansion with farthest reach.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    track current end and furthest reach, increment steps when reaching current end.
Edge Cases: single-element array and unreachable scenarios (though input assumes reachable).
Common Mistakes: counting jumps incorrectly or using nested loops.
Follow-up Interview Questions:
    1. How would you reconstruct the jump path?
    2. Can you adapt this to weighted jumps?
    3. What if backward jumps are allowed?
Alternative Approaches: Use BFS with queue of indexes.
Expected Output: The script prints the minimum jumps for a sample input.
Key Takeaways: Greedy interval extension yields the minimum required jumps.
"""

from __future__ import annotations

from typing import List


def jump(nums: List[int]) -> int:
    jumps = 0
    current_end = 0
    furthest = 0
    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = furthest
    return jumps


def main() -> None:
    print("Minimum jumps [2,3,1,1,4]:", jump([2, 3, 1, 1, 4]))


if __name__ == "__main__":
    main()
