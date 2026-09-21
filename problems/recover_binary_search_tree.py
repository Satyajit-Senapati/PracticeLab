"""recover_binary_search_tree.py

Problem Statement:
Implement a Python module that recovers a binary search tree where two nodes have been swapped.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: inorder traversal, tree property validation, recursion,
constant space anomaly detection
Real-world Use Case: Repairing corrupted search trees, validation for persistent structures, and debugging tree invariants.
Input Description: Function accepts the root of a BST with exactly two nodes swapped.
Output Description: The function fixes the tree in-place to restore BST ordering.
Example Inputs and Outputs:
    root = [3,1,4,null,null,2] -> fixed tree [2,1,4,null,null,3]
Constraints: Use O(n) time and O(1) auxiliary space if possible.
Brute Force Approach: Collect inorder values, sort, and rewrite nodes.
Optimized Approach: Use inorder traversal to find the two swapped nodes and swap values.
Time Complexity: O(n)
Space Complexity: O(h) recursion stack
Step-by-step Dry Run:
    track prev, first, second during inorder. For the first anomaly set first and prev.
    For the second anomaly set second. Swap their values at the end.
Edge Cases: adjacent swapped nodes and root-child swaps.
Common Mistakes: using value duplicates incorrectly, failing to handle exactly one inversion.
Follow-up Interview Questions:
    1. How can you solve this with Morris traversal?
    2. What if more than two nodes are swapped?
    3. Can you detect swap without modifying the tree?
Alternative Approaches: Use an explicit list of nodes and restore by sorted order.
Expected Output: The script prints inorder traversal before and after recovery.
Key Takeaways: BST inorder should be sorted, and two swapped nodes create at most two inversion points.
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


def recover_tree(root: Optional[TreeNode]) -> None:
    """Recover a BST where two nodes have been swapped by mistake."""
    first: Optional[TreeNode] = None
    second: Optional[TreeNode] = None
    prev: Optional[TreeNode] = None

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal first, second, prev
        if not node:
            return

        inorder(node.left)

        if prev and prev.val > node.val:
            if first is None:
                first = prev
            second = node

        prev = node
        inorder(node.right)

    inorder(root)
    if first and second:
        first.val, second.val = second.val, first.val


def inorder_values(root: Optional[TreeNode]) -> List[int]:
    return inorder_values(root.left) + [root.val] + inorder_values(root.right) if root else []


def main() -> None:
    root = TreeNode(3, left=TreeNode(1), right=TreeNode(4, left=TreeNode(2)))
    print("Before recovery:", inorder_values(root))
    recover_tree(root)
    print("After recovery:", inorder_values(root))


if __name__ == "__main__":
    main()
