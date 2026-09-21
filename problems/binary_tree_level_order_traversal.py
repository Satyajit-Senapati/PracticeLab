"""binary_tree_level_order_traversal.py

Problem Statement:
Implement a Python module that performs level-order traversal of a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: breadth-first traversal, queue usage, tree levels,
output grouping
Real-world Use Case: Breadth-first search on hierarchical structures,
level-based processing, and tree serialization.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns a list of node values grouped by tree depth.
Example Inputs and Outputs:
    root = [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
Constraints: Use O(n) time and O(n) space.
Brute Force Approach: Recursively collect nodes by depth with repeated traversal.
Optimized Approach: Use a queue for BFS and record level sizes.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    enqueue root, process each level sized batch, append child values.
Edge Cases: empty tree and single-node tree.
Common Mistakes: using recursion incorrectly or losing level boundaries.
Follow-up Interview Questions:
    1. How to print tree in zigzag order?
    2. Can you implement with DFS and depth tracking?
    3. What if nodes include null markers?
Alternative Approaches: Use two queues or current/next level lists.
Expected Output: The script prints level order groups for a sample tree.
Key Takeaways: BFS naturally groups nodes by increasing depth.
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


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Return the level order traversal of the tree as a list of levels."""
    if not root:
        return []

    result: List[List[int]] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_values: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_values)

    return result


def main() -> None:
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print("Level order:", level_order(root))


if __name__ == "__main__":
    main()
