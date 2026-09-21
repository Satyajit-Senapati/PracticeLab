"""binary_tree_maximum_path_sum.py

Problem Statement:
Implement a Python module that finds the maximum path sum in a binary tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, recursion, local/global maxima,
path sum aggregation
Real-world Use Case: Maximum-value path discovery in decision trees or network graphs represented as trees.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns the maximum sum of any path through the tree.
Example Inputs and Outputs:
    root = [1,2,3] -> 6
    root = [-10,9,20,null,null,15,7] -> 42
Constraints: A path may start and end at any node.
Brute Force Approach: Evaluate all node-pair paths O(n^2).
Optimized Approach: Use DFS to compute best downward path and update global max.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    compute left/right max downward path, combine with node value, update global max.
Edge Cases: negative values and single-node tree.
Common Mistakes: forgetting to exclude negative downward paths, using wrong base value for global maximum.
Follow-up Interview Questions:
    1. How would you adapt for non-binary trees?
    2. What if path must be root-to-leaf?
    3. Can you compute the path itself, not just the sum?
Alternative Approaches: Use bottom-up DP from leaves to root.
Expected Output: The script prints the maximum path sum for a sample tree.
Key Takeaways: Maximum path sum is found by combining best child contributions at each node.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Return the maximum path sum in the binary tree."""
    max_sum = float("-inf")

    def max_gain(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        current_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_sum)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return int(max_sum)


def main() -> None:
    root = TreeNode(
        -10,
        left=TreeNode(9),
        right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
    )
    print("Maximum path sum:", max_path_sum(root))


if __name__ == "__main__":
    main()
