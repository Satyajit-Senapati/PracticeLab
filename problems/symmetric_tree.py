"""symmetric_tree.py

Problem Statement:
Implement a Python module that checks whether a binary tree is symmetric.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree recursion, symmetry check, mirror traversal,
structural comparison
Real-world Use Case: Validation of mirrored hierarchical data and UI layout trees.
Input Description: Functions accept the root of a binary tree.
Output Description: Functions return True if the tree is symmetric, otherwise False.
Example Inputs and Outputs:
    [1,2,2,3,4,4,3] -> True
    [1,2,2,null,3,null,3] -> False
Constraints: Use O(n) time and O(h) space.
Brute Force Approach: Compare left and right subtree structures.
Optimized Approach: Recursively compare mirror nodes.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    compare left.left with right.right and left.right with right.left.
Edge Cases: empty tree, single node.
Common Mistakes: comparing values without mirror structure, forgetting to handle None nodes.
Follow-up Interview Questions:
    1. Can you solve this iteratively with a queue?
    2. How does the algorithm scale for unbalanced trees?
    3. What if the tree nodes contain non-primitive data?
Alternative Approaches: Use BFS to compare mirrored pairs.
Expected Output: The script prints symmetry checks for sample trees.
Key Takeaways: Symmetry is a mirror comparison of left and right subtrees.
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


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """Return True if the binary tree is symmetric."""
    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (
            left.val == right.val
            and is_mirror(left.left, right.right)
            and is_mirror(left.right, right.left)
        )

    return is_mirror(root.left, root.right) if root else True


def main() -> None:
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    print(is_symmetric(root))


if __name__ == "__main__":
    main()
