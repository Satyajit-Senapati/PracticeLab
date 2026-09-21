"""lowest_common_ancestor.py

Problem Statement:
Implement a Python module to find the lowest common ancestor of two nodes in a binary tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, recursion, binary tree structure, ancestor relationships
Real-world Use Case: Hierarchical queries, family trees, organizational charts, and filesystem ancestry.
Input Description: Functions accept the root of a binary tree and two target nodes.
Output Description: Functions return the lowest common ancestor node.
Example Inputs and Outputs:
    lca(root, p, q) -> Node with value 3 for appropriate tree
Constraints: Use O(n) time and O(h) recursion space for tree traversal.
Brute Force Approach: Collect ancestors for each node and compare.
Optimized Approach: Use recursive DFS to find LCA in a single pass.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    traverse left and right subtrees for nodes p and q
    return the lowest common node that sees both children
Edge Cases: one node is ancestor of the other, root is LCA, and nodes not present.
Common Mistakes: misunderstanding the recursive return conditions, not handling missing nodes, and accidentally returning the first common ancestor instead of lowest.
Follow-up Interview Questions:
    1. How would you handle a binary search tree variant?
    2. Can you find LCA when nodes include parent pointers?
    3. What if nodes are guaranteed to exist or may be missing?
Alternative Approaches: Use parent-pointer maps or reduction from ancestor sets.
Expected Output: The script builds a sample tree and prints the LCA result.
Key Takeaways: Recursive DFS can identify the lowest common ancestor with clean state propagation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    """Binary tree node with integer value and optional children."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Return the lowest common ancestor of nodes p and q."""
    if root is None or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right


def main() -> None:
    """Main function demonstrating lowest common ancestor."""
    root = TreeNode(
        3,
        left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
        right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)),
    )
    p = root.left
    q = root.right
    ancestor = lowest_common_ancestor(root, p, q)
    print("LCA of", p.val, "and", q.val, "is", ancestor.val if ancestor else None)


if __name__ == "__main__":
    main()
