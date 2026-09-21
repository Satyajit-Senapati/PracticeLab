"""path_sum.py

Problem Statement:
Implement a Python module that checks whether the binary tree has a root-to-leaf path with a given sum.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, recursion, path accumulation,
leaf detection
Real-world Use Case: Evaluating weighted decision paths and cumulative constraints in trees.
Input Description: Functions accept the root of a binary tree and an integer sum.
Output Description: Functions return True if such a path exists.
Example Inputs and Outputs:
    [5,4,8,11,null,13,4,7,2,null,null,null,1], sum=22 -> True
Constraints: Use O(n) time and O(h) space.
Brute Force Approach: Explore every root-to-leaf path and accumulate sums.
Optimized Approach: Subtract node values as recursion descends.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    subtract node values from target and check leaf equality.
Edge Cases: empty tree, negative values, single-node tree.
Common Mistakes: checking non-leaf nodes, not passing remaining sum correctly.
Follow-up Interview Questions:
    1. How do you return the actual path instead of a boolean?
    2. Can you solve this iteratively with a stack?
    3. What if path can start and end anywhere in the tree?
Alternative Approaches: Use DFS with an explicit stack.
Expected Output: The script prints path sum checks for sample trees.
Key Takeaways: Root-to-leaf path sum is naturally solved by recursive subtraction.
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


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """Return True if there is a root-to-leaf path with the given sum."""
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target_sum
    return (
        has_path_sum(root.left, target_sum - root.val)
        or has_path_sum(root.right, target_sum - root.val)
    )


def main() -> None:
    root = TreeNode(
        5,
        left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
        right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))),
    )
    print(has_path_sum(root, 22))


if __name__ == "__main__":
    main()
