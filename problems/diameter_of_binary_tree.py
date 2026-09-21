"""diameter_of_binary_tree.py

Problem Statement:
Implement a Python module that computes the diameter of a binary tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, tree depth calculation, path length,
post-order traversal
Real-world Use Case: Finding the longest path through hierarchical structures,
measuring communication latency in network trees.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns the length of the longest path between any two nodes.
Example Inputs and Outputs:
    root = [1,2,3,4,5] -> 3
Constraints: Path length is measured in number of edges.
Brute Force Approach: Check all node pairs; O(n^2).
Optimized Approach: Use DFS to calculate max depth and update diameter.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    compute left/right heights, update diameter with left_height + right_height.
Edge Cases: empty tree and single-node tree.
Common Mistakes: returning depth instead of diameter or not using global state.
Follow-up Interview Questions:
    1. How to compute diameter iteratively?
    2. What is the diameter of a skewed tree?
    3. How does diameter differ from height?
Alternative Approaches: Use dynamic programming with memoization.
Expected Output: The script prints the diameter for a sample binary tree.
Key Takeaways: Diameter can be found during a single traversal by combining subtree heights.
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


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """Return the diameter of the binary tree."""
    diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return diameter


def main() -> None:
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
    print("Diameter:", diameter_of_binary_tree(root))


if __name__ == "__main__":
    main()
