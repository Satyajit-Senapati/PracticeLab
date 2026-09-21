"""binary_tree_right_side_view.py

Problem Statement:
Implement a Python module that returns the right side view of a binary tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BFS traversal, level processing, tree view extraction,
queue usage
Real-world Use Case: Visibility computation in hierarchical structures and rendering side views.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns values visible from the right side at each depth.
Example Inputs and Outputs:
    root = [1,2,3,null,5,null,4] -> [1,3,4]
Constraints: Use O(n) time and O(n) space.
Brute Force Approach: Use DFS and track max depth visited from the right.
Optimized Approach: Use BFS and take the last node value at each level.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    traverse level by level and record the final value of each level.
Edge Cases: empty tree and single-node tree.
Common Mistakes: recording the first node instead of the last at each level.
Follow-up Interview Questions:
    1. How to compute the left side view instead?
    2. Can you compute it with DFS instead of BFS?
    3. What is the view from the top?
Alternative Approaches: DFS with right-first traversal and depth tracking.
Expected Output: The script prints the right side view values for a sample tree.
Key Takeaways: The right side view is the rightmost node of each depth level.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """Return the values visible from the right side of the tree."""
    if not root:
        return []

    view: List[int] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return view


def main() -> None:
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, right=TreeNode(4)))
    print("Right side view:", right_side_view(root))


if __name__ == "__main__":
    main()
