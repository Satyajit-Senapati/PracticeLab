"""delete_node_in_bst.py

Problem Statement:
Implement a Python module that deletes a node with a given value from a binary search tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST deletion cases, recursion, tree restructuring,
successor/predecessor handling
Real-world Use Case: Removing entries from ordered indices, maintaining balanced search structures, and database operations.
Input Description: Functions accept the root of a BST and a value to delete.
Output Description: Returns the root of the BST after deletion.
Example Inputs and Outputs:
    root = [5,3,6,2,4,null,7], key = 3 -> [5,4,6,2,null,null,7]
Constraints: Maintain BST properties.
Brute Force Approach: Rebuild the tree without the deleted value.
Optimized Approach: Traverse to the node and handle 0, 1, or 2 children cases.
Time Complexity: O(h)
Space Complexity: O(h) recursion stack
Step-by-step Dry Run:
    find node, if two children replace with inorder successor and delete successor.
Edge Cases: deleting root, leaf nodes, and nodes with one child.
Common Mistakes: wrong successor replacement, incorrect subtree reattachment, and failing on duplicate values.
Follow-up Interview Questions:
    1. How do deletion cases differ for AVL/Red-Black trees?
    2. Can you implement using predecessor instead of successor?
    3. What is the time complexity worst case?
Alternative Approaches: Use iterative traversal with parent pointer.
Expected Output: The script prints inorder traversal before and after deletion.
Key Takeaways: BST deletion requires careful handling of child cases and successor replacement.
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


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Delete a node with the given key from the BST."""
    if root is None:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)

    return root


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


def main() -> None:
    root = TreeNode(
        5,
        left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)),
        right=TreeNode(6, right=TreeNode(7)),
    )
    print("Before deletion:", inorder_traversal(root))
    root = delete_node(root, 3)
    print("After deletion:", inorder_traversal(root))


if __name__ == "__main__":
    main()
