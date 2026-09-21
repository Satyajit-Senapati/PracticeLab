"""minimum_absolute_difference_in_bst.py

Problem Statement:
Implement a Python module that finds the minimum absolute difference between values
of any two nodes in a binary search tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: inorder traversal, sorted sequence properties, tree traversal,
min difference calculation
Real-world Use Case: Finding the closest pair in ordered numeric data stored in a BST.
Input Description: Function accepts the root of a BST.
Output Description: Returns an integer representing the minimum absolute difference.
Example Inputs and Outputs:
    root = [4,2,6,1,3] -> 1
Constraints: Use BST inorder traversal to generate sorted node values.
Brute Force Approach: Compare all pairs O(n^2).
Optimized Approach: Use inorder traversal and compare adjacent values.
Time Complexity: O(n)
Space Complexity: O(h) recursion stack
Step-by-step Dry Run:
    perform inorder traversal and track previous value difference with current.
Edge Cases: tree with only two nodes.
Common Mistakes: comparing non-adjacent values, not handling None previous node.
Follow-up Interview Questions:
    1. Can this be done iteratively?
    2. What if the tree is not a BST?
    3. How to handle duplicates if allowed?
Alternative Approaches: flatten values in a list then scan adjacent differences.
Expected Output: The script prints the minimum absolute difference for a sample BST.
Key Takeaways: Inorder traversal yields sorted values for BSTs, so minimum difference is adjacent.
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


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    """Return the minimum absolute difference between values of any two nodes in a BST."""
    prev_value: Optional[int] = None
    min_diff = float("inf")

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal prev_value, min_diff
        if not node:
            return

        inorder(node.left)
        if prev_value is not None:
            min_diff = min(min_diff, node.val - prev_value)
        prev_value = node.val
        inorder(node.right)

    inorder(root)
    return int(min_diff)


def main() -> None:
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(6))
    print("Minimum absolute difference:", get_minimum_difference(root))


if __name__ == "__main__":
    main()
