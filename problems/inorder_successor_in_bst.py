"""inorder_successor_in_bst.py

Problem Statement:
Implement a Python module that finds the inorder successor of a given node in a BST.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST property, inorder traversal, parent/child relationships,
search ordering
Real-world Use Case: Finding the next record in sorted tree indices and cursor movement in BST-backed data stores.
Input Description: Function accepts the root of a BST and the target node.
Output Description: Returns the node that appears next in inorder traversal.
Example Inputs and Outputs:
    root = [5,3,6,2,4,null,null,1], p = 3 -> 4
Constraints: Use O(h) time and O(1) extra space.
Brute Force Approach: Generate inorder list and locate the successor.
Optimized Approach: Use BST traversal and node relationships.
Time Complexity: O(h)
Space Complexity: O(1)
Step-by-step Dry Run:
    if node has right child, successor is leftmost node in right subtree; otherwise walk from root.
Edge Cases: node with no successor and node is maximum value.
Common Mistakes: assuming parent pointer exists or returning wrong child path.
Follow-up Interview Questions:
    1. How to compute predecessor similarly?
    2. What if nodes have parent pointers?
    3. Can you find successor in a general binary tree?
Alternative Approaches: Use a stack for inorder until successor found.
Expected Output: The script prints the successor node value for a sample BST.
Key Takeaways: Inorder successor depends on right subtree or ancestor relations.
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


def inorder_successor(root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
    """Return the inorder successor of node p in the BST."""
    if p.right:
        successor = p.right
        while successor.left:
            successor = successor.left
        return successor

    successor: Optional[TreeNode] = None
    current = root
    while current:
        if p.val < current.val:
            successor = current
            current = current.left
        elif p.val > current.val:
            current = current.right
        else:
            break
    return successor


def main() -> None:
    root = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))
    node = root.left
    successor = inorder_successor(root, node)
    print("Successor of 3:", successor.val if successor else None)


if __name__ == "__main__":
    main()
