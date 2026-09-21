"""lowest_common_ancestor_bst.py

Problem Statement:
Implement a Python module that finds the lowest common ancestor in a binary search tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: binary search tree properties, recursion, ancestor search,
value comparisons
Real-world Use Case: Taxonomy navigation, hierarchical queries, and BST-based indexing.
Input Description: Functions accept the root of a BST and two target nodes.
Output Description: Functions return the lowest common ancestor node.
Example Inputs and Outputs:
    root = [6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 -> 6
    p=2, q=4 -> 2
Constraints: Use O(h) time where h is tree height.
Brute Force Approach: Search ancestor paths and compare.
Optimized Approach: Use BST ordering to traverse from root downwards.
Time Complexity: O(h)
Space Complexity: O(h) recursion stack
Step-by-step Dry Run:
    if both values less than root -> go left; if both greater -> go right; else return root.
Edge Cases: one node is ancestor of the other, root is ancestor, and p or q equals root.
Common Mistakes: ignoring BST ordering, returning before checking both children, and using inorder traversal.
Follow-up Interview Questions:
    1. How does this differ from LCA in an arbitrary binary tree?
    2. Can you implement iteratively?
    3. What if the tree is not a BST?
Alternative Approaches: Use parent pointers or full ancestor path comparison.
Expected Output: The script prints LCA values for sample BST inputs.
Key Takeaways: BST ordering reduces LCA search to a single path traversal.
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


def lowest_common_ancestor_bst(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Return the lowest common ancestor of p and q in a BST."""
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
    return None


def main() -> None:
    root = TreeNode(
        6,
        left=TreeNode(2, left=TreeNode(0), right=TreeNode(4, left=TreeNode(3), right=TreeNode(5))),
        right=TreeNode(8, left=TreeNode(7), right=TreeNode(9)),
    )
    p = root.left
    q = root.right
    lca = lowest_common_ancestor_bst(root, p, q)
    print("LCA value:", lca.val if lca else None)


if __name__ == "__main__":
    main()
