"""same_tree.py

Problem Statement:
Implement a Python module that checks whether two binary trees are structurally
identical and have the same node values.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, tree comparison, structural equality,
traversal
Real-world Use Case: Comparing serialized tree structures, verifying tree copies, and checking schema equality.
Input Description: Function accepts the roots of two binary trees.
Output Description: Returns True if both trees are the same, otherwise False.
Example Inputs and Outputs:
    p = [1,2,3], q = [1,2,3] -> True
    p = [1,2], q = [1,null,2] -> False
Constraints: Use O(n) time and O(h) space.
Brute Force Approach: Convert both trees to lists and compare.
Optimized Approach: Recursively compare values and children simultaneously.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    compare values, then left subtrees, then right subtrees.
Edge Cases: one tree empty and the other non-empty.
Common Mistakes: not checking both children or incorrect base cases.
Follow-up Interview Questions:
    1. How to compare trees iteratively?
    2. Can you compare n-ary trees similarly?
    3. What if node values are objects instead of ints?
Alternative Approaches: Use synchronized traversals with stacks.
Expected Output: The script prints equality results for sample trees.
Key Takeaways: Two trees are the same if every corresponding node matches.
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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Return True if two binary trees are the same."""
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def main() -> None:
    tree1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    tree2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    tree3 = TreeNode(1, left=TreeNode(2))
    print("Tree1 and Tree2 same:", is_same_tree(tree1, tree2))
    print("Tree1 and Tree3 same:", is_same_tree(tree1, tree3))


if __name__ == "__main__":
    main()
