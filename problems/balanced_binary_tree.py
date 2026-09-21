"""balanced_binary_tree.py

Problem Statement:
Implement a Python module that checks whether a binary tree is height-balanced.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree recursion, height computation, balance factor,
optimized pruning
Real-world Use Case: Validating tree balance for search performance and
memory efficiency.
Input Description: Functions accept the root of a binary tree.
Output Description: Functions return True if the tree is balanced.
Example Inputs and Outputs:
    [3,9,20,null,null,15,7] -> True
    [1,2,2,3,3,null,null,4,4] -> False
Constraints: Use O(n) time by computing heights in one pass.
Brute Force Approach: Compute height at every node separately.
Optimized Approach: Use recursion to return height or failure sentinel.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    recursively return subtree heights and check difference <= 1.
Edge Cases: empty tree, single node tree.
Common Mistakes: recomputing subtree heights repeatedly and missing None nodes.
Follow-up Interview Questions:
    1. How do you ensure the algorithm is O(n) rather than O(n^2)?
    2. Can you adapt this to AVL tree insertion checks?
    3. What is the balance definition for an n-ary tree?
Alternative Approaches: Use memoization, though direct recursion is simplest.
Expected Output: The script prints balance checks for sample trees.
Key Takeaways: Balance detection is efficient when height is computed bottom-up.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Return True if the binary tree is height-balanced."""
    def check(node: Optional[TreeNode]) -> Tuple[bool, int]:
        if node is None:
            return True, 0
        left_balanced, left_height = check(node.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = check(node.right)
        if not right_balanced:
            return False, 0
        return abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)

    balanced, _ = check(root)
    return balanced


def main() -> None:
    root1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    root2 = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)), right=TreeNode(2))
    print(is_balanced(root1))
    print(is_balanced(root2))


if __name__ == "__main__":
    main()
