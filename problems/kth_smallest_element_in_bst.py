"""kth_smallest_element_in_bst.py

Problem Statement:
Implement a Python module that finds the kth smallest element in a binary search tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST inorder traversal, recursion, iterative traversal,
order statistics
Real-world Use Case: Ranking queries, finding percentile values from indexed data, and search-tree analytics.
Input Description: Function accepts the root of a BST and an integer k.
Output Description: Returns the kth smallest value in the BST.
Example Inputs and Outputs:
    root = [3,1,4,null,2], k = 1 -> 1
Constraints: Use O(h + k) time and O(h) space.
Brute Force Approach: Flatten the tree values and index into the sorted list.
Optimized Approach: Stop inorder traversal as soon as kth smallest is found.
Time Complexity: O(h + k)
Space Complexity: O(h)
Step-by-step Dry Run:
    perform inorder traversal, decrement k until zero, then return current node value.
Edge Cases: k equals tree size, empty nodes, invalid k.
Common Mistakes: confusing kth smallest with kth largest, traversing entire tree unnecessarily.
Follow-up Interview Questions:
    1. Can you solve it iteratively with a stack?
    2. How would you support dynamic insert/delete operations?
    3. What if duplicates are allowed in the BST?
Alternative Approaches: Augment node counts or use order-statistic tree information.
Expected Output: The script prints the kth smallest value for a sample BST.
Key Takeaways: Inorder traversal of a BST yields values in ascending order.
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


def kth_smallest(root: Optional[TreeNode], k: int) -> Optional[int]:
    """Return the kth smallest element in the BST."""
    stack: list[TreeNode] = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right

    return None


def main() -> None:
    root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    print("1st smallest:", kth_smallest(root, 1))
    print("2nd smallest:", kth_smallest(root, 2))
    print("3rd smallest:", kth_smallest(root, 3))


if __name__ == "__main__":
    main()
