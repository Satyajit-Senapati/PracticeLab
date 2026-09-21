"""path_sum_iii.py

Problem Statement:
Implement a Python module that counts the number of paths in a binary tree whose
sum equals a target value. Paths do not need to start at the root or end at a leaf.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: prefix sums, tree traversal, hash maps,
path counting
Real-world Use Case: Counting target-weighted paths in hierarchical data,
analytics on tree-structured inputs.
Input Description: Function accepts the root of a binary tree and a target sum.
Output Description: Returns the number of paths with the target sum.
Example Inputs and Outputs:
    root = [10,5,-3,3,2,null,11,3,-2,null,1], target = 8 -> 3
Constraints: Use O(n) time with prefix sum tracking.
Brute Force Approach: Explore all start/end pairs O(n^2).
Optimized Approach: Use DFS and a prefix-sum frequency map.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    track cumulative sum, count previous prefix sums that yield target.
Edge Cases: negative values and overlapping paths.
Common Mistakes: not decrementing map counts during backtracking, missing root-starting paths.
Follow-up Interview Questions:
    1. Can you adapt for only downward paths starting at root?
    2. How does prefix sum help reduce complexity?
    3. What if values are very large?
Alternative Approaches: Use recursion with an explicit path list.
Expected Output: The script prints the number of valid paths for a sample tree.
Key Takeaways: Prefix sums let you count target subpaths efficiently during DFS.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    """Return the number of paths that sum to target_sum."""
    prefix_sums: Dict[int, int] = {0: 1}
    count = 0

    def dfs(node: Optional[TreeNode], current_sum: int) -> None:
        nonlocal count
        if not node:
            return

        current_sum += node.val
        count += prefix_sums.get(current_sum - target_sum, 0)
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

        prefix_sums[current_sum] -= 1

    dfs(root, 0)
    return count


def main() -> None:
    root = TreeNode(
        10,
        left=TreeNode(5, left=TreeNode(3, left=TreeNode(3), right=TreeNode(-2)), right=TreeNode(2, right=TreeNode(1))),
        right=TreeNode(-3, right=TreeNode(11)),
    )
    print("Number of paths summing to 8:", path_sum(root, 8))


if __name__ == "__main__":
    main()
