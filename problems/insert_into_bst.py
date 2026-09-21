"""insert_into_bst.py

Problem Statement:
Implement a Python module that inserts a value into a binary search tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST insertion, recursion, tree node placement,
and maintaining sorted order.
Real-world Use Case: Adding records to ordered tree-based indices or search structures.
Input Description: Functions accept the root of a BST and a value to insert.
Output Description: Returns the root of the BST with the new value inserted.
Example Inputs and Outputs:
    root = [4,2,7,1,3], val = 5 -> [4,2,7,1,3,5]
Constraints: Maintain BST invariant.
Brute Force Approach: Rebuild tree after insertion.
Optimized Approach: Traverse left or right until a null child is found and attach a new node.
Time Complexity: O(h)
Space Complexity: O(h) recursion stack
Step-by-step Dry Run:
    if val < node.val, insert left; else insert right. Return root.
Edge Cases: empty tree.
Common Mistakes: inserting duplicate values incorrectly, forgetting to return node references.
Follow-up Interview Questions:
    1. How to handle duplicate values in BST?
    2. Can you implement iteratively?
    3. What is the worst-case height of the tree?
Alternative Approaches: iterative traversal with explicit parent pointer.
Expected Output: The script prints inorder traversal after insertion.
Key Takeaways: BST insertion is straightforward if the property is preserved.
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


def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """Insert a value into the BST and return the root."""
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


def main() -> None:
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
    root = insert_into_bst(root, 5)
    print("Inorder after insert:", inorder_traversal(root))


if __name__ == "__main__":
    main()
