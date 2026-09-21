"""binary_tree_traversal.py

Problem Statement:
Implement a Python module that performs pre-order, in-order, and post-order
traversals of a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, recursion, stack simulation, tree data
structures
Real-world Use Case: Expression evaluation, tree serialization, syntax
analysis, and hierarchical data processing.
Input Description: Functions accept the root of a binary tree.
Output Description: Functions return traversal orders as lists.
Example Inputs and Outputs:
    pre_order(root) -> [1, 2, 4, 5, 3]
    in_order(root) -> [4, 2, 5, 1, 3]
    post_order(root) -> [4, 5, 2, 3, 1]
Constraints: Use O(n) time and O(h) space for recursion or explicit stacks.
Brute Force Approach: None required for traversal; use recursive depth-first search.
Optimized Approach: Use recursion or iterative stacks per traversal order.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    traverse root 1, left subtree, right subtree
    return correct order list
Edge Cases: empty tree, single-node tree, and skewed trees.
Common Mistakes: incorrect recursion order, dropping nodes, and misplacing
left/right subtree traversal.
Follow-up Interview Questions:
    1. How do traversal orders differ for binary search trees?
    2. Can you implement these iteratively?
    3. What traversal gives sorted output on a BST?
Alternative Approaches: Use iterative stack-based traversal instead of recursion.
Expected Output: The script prints all three traversal orders for a sample tree.
Key Takeaways: Traversal orders are foundational for binary tree algorithms.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def pre_order(root: Optional[TreeNode]) -> List[int]:
    """Return the pre-order traversal of the tree."""
    if root is None:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)


def in_order(root: Optional[TreeNode]) -> List[int]:
    """Return the in-order traversal of the tree."""
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


def post_order(root: Optional[TreeNode]) -> List[int]:
    """Return the post-order traversal of the tree."""
    if root is None:
        return []
    return post_order(root.left) + post_order(root.right) + [root.val]


def main() -> None:
    """Main function demonstrating binary tree traversals."""
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )

    print("Pre-order:", pre_order(root))
    print("In-order:", in_order(root))
    print("Post-order:", post_order(root))


if __name__ == "__main__":
    main()
