"""kth_largest_element_in_bst.py

Problem Statement:
Implement a Python module that finds the kth largest element in a binary search tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST traversal, reverse inorder order, recursion,
order statistics
Real-world Use Case: Ranking queries, quantile calculation, and retrieval of top-k values from sorted data.
Input Description: Function accepts the root of a BST and an integer k.
Output Description: Returns the kth largest value in the BST.
Example Inputs and Outputs:
    root = [3,1,4,null,2], k = 1 -> 4
Constraints: Use O(h + k) time and O(h) space.
Brute Force Approach: Flatten values and index from the end.
Optimized Approach: Use reverse inorder traversal and stop after k nodes.
Time Complexity: O(h + k)
Space Complexity: O(h)
Step-by-step Dry Run:
    traverse right subtree, visit node, then left subtree, decrement k.
Edge Cases: k equals tree size, invalid k, single-node tree.
Common Mistakes: traversing the entire tree and confusing smallest/largest.
Follow-up Interview Questions:
    1. How would you support duplicates in the BST?
    2. Can you augment the tree with subtree sizes for O(h) queries?
    3. What is the difference between kth smallest and kth largest?
Alternative Approaches: Use an order-statistic tree or a max-heap on all values.
Expected Output: The script prints the kth largest value for sample BST inputs.
Key Takeaways: Reverse inorder on a BST yields descending order.
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


def kth_largest(root: Optional[TreeNode], k: int) -> Optional[int]:
    """Return the kth largest element in the BST."""
    stack: list[TreeNode] = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.right
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.left

    return None


def main() -> None:
    root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    print("1st largest:", kth_largest(root, 1))
    print("2nd largest:", kth_largest(root, 2))
    print("3rd largest:", kth_largest(root, 3))


if __name__ == "__main__":
    main()
