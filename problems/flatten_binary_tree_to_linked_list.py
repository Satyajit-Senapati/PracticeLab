"""flatten_binary_tree_to_linked_list.py

Problem Statement:
Implement a Python module that flattens a binary tree to a linked list in-place.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, pointer manipulation, in-place transformation,
preorder sequence
Real-world Use Case: Transforming hierarchical tree structures to linear
formats for serialization or traversal.
Input Description: Functions accept the root of a binary tree.
Output Description: Functions modify the tree so that it becomes a right-skewed linked list.
Example Inputs and Outputs:
    [1,2,5,3,4,null,6] -> [1,null,2,null,3,null,4,null,5,null,6]
Constraints: Use O(n) time and O(1) extra space (recursive stack excluded).
Brute Force Approach: Build a list of nodes, then rewire pointers.
Optimized Approach: Use reverse preorder traversal and maintain the next pointer.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    traverse root-right-left, set node.right = previous, node.left = None.
Edge Cases: empty tree, single-node tree, and already right-skewed trees.
Common Mistakes: losing the right subtree, not nullifying left pointers, and incorrect traversal order.
Follow-up Interview Questions:
    1. How does preorder traversal influence the flattened shape?
    2. Can you flatten using an iterative stack?
    3. What is the difference between flattening and converting to an array?
Alternative Approaches: Use a stack or list to capture nodes in preorder.
Expected Output: The script prints the flattened right-skewed tree values for sample inputs.
Key Takeaways: Reverse preorder traversal preserves the required in-place node order.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def flatten(root: Optional[TreeNode]) -> None:
    """Flatten the tree into a linked list in-place."""
    prev: Optional[TreeNode] = None

    def helper(node: Optional[TreeNode]) -> None:
        nonlocal prev
        if node is None:
            return
        helper(node.right)
        helper(node.left)
        node.right = prev
        node.left = None
        prev = node

    helper(root)


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    """Convert the flattened tree to a list of values."""
    result: List[int] = []
    current = root
    while current:
        result.append(current.val)
        current = current.right
    return result


def main() -> None:
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
        right=TreeNode(5, right=TreeNode(6)),
    )
    flatten(root)
    print(tree_to_list(root))


if __name__ == "__main__":
    main()
