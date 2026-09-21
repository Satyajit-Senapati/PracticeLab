"""binary_tree_max_depth.py

Problem Statement:
Implement a Python module that finds the maximum depth of a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree recursion, depth-first search, tree height,
recursive base cases
Real-world Use Case: Computing tree height for balancing, serialization depth,
and hierarchical analysis.
Input Description: Functions accept the root of a binary tree.
Output Description: Functions return the maximum depth (height) as an integer.
Example Inputs and Outputs:
    max_depth(tree root) -> 3
Constraints: Use O(n) time and O(h) recursion space.
Brute Force Approach: None beyond visiting every node.
Optimized Approach: Use recursion to compute depth in one traversal.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    depth(left) = 2, depth(right) = 1
    return 1 + max(2, 1) = 3
Edge Cases: empty tree and single-node tree.
Common Mistakes: off-by-one errors and not using max across subtrees.
Follow-up Interview Questions:
    1. How would you compute minimum depth?
    2. Can this be done iteratively with a queue?
    3. How does tree height relate to node count?
Alternative Approaches: Use BFS level-order traversal to compute depth.
Expected Output: The script prints max depths for sample trees.
Key Takeaways: Depth-first recursion naturally computes tree height.
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
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def main() -> None:
    """Main function demonstrating binary tree max depth."""
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )
    print("Max depth:", max_depth(root))


if __name__ == "__main__":
    main()
