"""validate_binary_search_tree.py

Problem Statement:
Implement a Python module to validate whether a binary tree is a binary search tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree validation, recursion, bounds checking, inorder traversal,
strict ordering
Real-world Use Case: Ensuring tree integrity before query execution or indexing,
validating deserialized tree structures.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns True if the tree is a valid BST, otherwise False.
Example Inputs and Outputs:
    root = [2,1,3] -> True
    root = [5,1,4,null,null,3,6] -> False
Constraints: Use O(n) time and O(h) space.
Brute Force Approach: Flatten inorder and compare sorted order.
Optimized Approach: Use recursive bounds to validate subtree values.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    validate left subtree with upper bound, right subtree with lower bound.
Edge Cases: repeated values and invalid subtree boundaries.
Common Mistakes: allowing equal values in left or right subtree and failing strict inequalities.
Follow-up Interview Questions:
    1. Can you validate iteratively?
    2. How does duplicate handling change the bounds?
    3. Why is inorder traversal enough for BST validation?
Alternative Approaches: Use inorder traversal and compare to previous value.
Expected Output: The script prints validation results for sample trees.
Key Takeaways: BST validity requires all left descendants less than root and all right descendants greater than root.
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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Validate a binary tree as a BST using lower and upper bounds."""

    def helper(node: Optional[TreeNode], lower: float, upper: float) -> bool:
        if node is None:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

    return helper(root, float("-inf"), float("inf"))


def main() -> None:
    valid_root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    invalid_root = TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
    print("Valid BST:", is_valid_bst(valid_root))
    print("Invalid BST:", is_valid_bst(invalid_root))


if __name__ == "__main__":
    main()
