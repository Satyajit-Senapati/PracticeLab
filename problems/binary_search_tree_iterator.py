"""binary_search_tree_iterator.py

Problem Statement:
Implement a Python module that provides an iterator over a binary search tree in ascending order.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: iterative inorder traversal, stack management, lazy evaluation,
BST ordering
Real-world Use Case: Ordered iteration over indexed data, streaming results,
and query cursors.
Input Description: Functions accept the root of a BST.
Output Description: The iterator provides has_next and next methods.
Example Inputs and Outputs:
    BST with values [7,3,15,9,20] yields 3, 7, 9, 15, 20 sequentially.
Constraints: Use O(h) space where h is tree height.
Brute Force Approach: Flatten the BST to a sorted list up front.
Optimized Approach: Use a stack to traverse nodes lazily.
Time Complexity: amortized O(1) per next call.
Space Complexity: O(h)
Step-by-step Dry Run:
    push left side, pop node, push right subtree's left side.
Edge Cases: empty tree and single-node tree.
Common Mistakes: not pushing right subtree left chain, using recursion and storing all values.
Follow-up Interview Questions:
    1. How would you implement reverse in-order traversal?
    2. Can you support delete operations while iterating?
    3. What is the amortized complexity argument?
Alternative Approaches: Use generators and yield values lazily.
Expected Output: The script prints inorder BST traversal via iterator.
Key Takeaways: A stack-based iterator achieves ordered traversal without materializing the full list.
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


class BSTIterator:
    """Iterator for a binary search tree that returns values in ascending order."""

    def __init__(self, root: Optional[TreeNode]) -> None:
        self.stack: List[TreeNode] = []
        self._push_left_branch(root)

    def _push_left_branch(self, node: Optional[TreeNode]) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        value = node.val
        self._push_left_branch(node.right)
        return value

    def has_next(self) -> bool:
        return bool(self.stack)


def main() -> None:
    root = TreeNode(
        7,
        left=TreeNode(3),
        right=TreeNode(15, left=TreeNode(9), right=TreeNode(20)),
    )
    iterator = BSTIterator(root)
    values: List[int] = []
    while iterator.has_next():
        values.append(iterator.next())
    print(values)


if __name__ == "__main__":
    main()
