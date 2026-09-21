"""sum_root_to_leaf_numbers.py

Problem Statement:
Given a binary tree containing digits 0-9, return the total sum of all
root-to-leaf numbers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Google, Microsoft
Concepts Tested: tree traversal, recursion, path accumulation.
Real-world Use Case: evaluating hierarchical numeric codes.
Input Description: The root of a binary tree.
Output Description: The sum of numbers formed by root-to-leaf paths.
Example Inputs and Outputs:
    [1,2,3] -> 25 (12 + 13)
    [4,9,0,5,1] -> 1026 (495 + 491 + 40)
Constraints: Tree nodes contain digits only.
Time Complexity: O(n)
Space Complexity: O(h) recursion stack.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def sum_numbers(root: Optional[TreeNode]) -> int:
    """Return the sum of all numbers formed from root-to-leaf paths."""
    def dfs(node: Optional[TreeNode], current: int) -> int:
        if node is None:
            return 0
        current = current * 10 + node.val
        if not node.left and not node.right:
            return current
        return dfs(node.left, current) + dfs(node.right, current)

    return dfs(root, 0)


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    child_index = 1
    for node in nodes:
        if node is not None:
            if child_index < len(nodes):
                node.left = nodes[child_index]
                child_index += 1
            if child_index < len(nodes):
                node.right = nodes[child_index]
                child_index += 1
    return nodes[0]


def main() -> None:
    examples = [
        [1, 2, 3],
        [4, 9, 0, 5, 1],
    ]
    for values in examples:
        root = build_tree(values)
        print(values, "->", sum_numbers(root))


if __name__ == "__main__":
    main()
