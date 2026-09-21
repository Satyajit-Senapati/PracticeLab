"""maximum_depth_of_binary_tree.py

Problem Statement:
Implement a Python module that finds the maximum depth of a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, tree depth calculation, DFS,
maximum path length
Real-world Use Case: Determining tree height for layout, scheduling, or complexity analysis.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns the maximum number of nodes from root to the deepest leaf.
Example Inputs and Outputs:
    root = [3,9,20,null,null,15,7] -> 3
Constraints: A simple O(n) traversal is sufficient.
Brute Force Approach: Explore all paths and compute depths individually.
Optimized Approach: Use recursion to compute max depth of subtrees.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    return 1 + max(depth(left), depth(right)) for each node.
Edge Cases: empty tree and single-node tree.
Common Mistakes: forgetting to handle None node base case.
Follow-up Interview Questions:
    1. How to compute depth iteratively?
    2. What is the difference between depth and height?
    3. How does tree balance affect maximum depth?
Alternative Approaches: Use BFS and count levels.
Expected Output: The script prints the maximum depth for a sample tree.
Key Takeaways: Maximum depth is the height of the tree and can be computed recursively.
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


def max_depth(root: Optional[TreeNode]) -> int:
    """Return the maximum depth of the binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def main() -> None:
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print("Maximum depth:", max_depth(root))


if __name__ == "__main__":
    main()
