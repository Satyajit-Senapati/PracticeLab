"""binary_tree_zigzag_level_order.py

Problem Statement:
Implement a Python module that performs zigzag level order traversal of a binary tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: breadth-first traversal, alternating order, queue usage,
level grouping
Real-world Use Case: Level-based visualization, hierarchical ordering, and alternating scan patterns.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns a list of levels with nodes ordered in zigzag fashion.
Example Inputs and Outputs:
    root = [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]
Constraints: Use O(n) time and O(n) space.
Brute Force Approach: Use BFS then reverse every other level after traversal.
Optimized Approach: Alternate insertion order while building each level.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    process each level from left-to-right or right-to-left based on parity.
Edge Cases: empty tree and single-node tree.
Common Mistakes: reversing the wrong levels or using extra passes.
Follow-up Interview Questions:
    1. How to perform zigzag traversal iteratively with two stacks?
    2. Can you adapt this to n-ary trees?
    3. What if levels must alternate starting from the bottom?
Alternative Approaches: Use DFS with depth parity toggling.
Expected Output: The script prints zigzag-ordered levels for a sample tree.
Key Takeaways: Alternating direction can be handled at each BFS level.
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


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Return the zigzag level order traversal of a binary tree."""
    if not root:
        return []

    results: List[List[int]] = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_values: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level_values.append(node.val)
            else:
                level_values.insert(0, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        results.append(level_values)
        left_to_right = not left_to_right

    return results


def main() -> None:
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print("Zigzag level order:", zigzag_level_order(root))


if __name__ == "__main__":
    main()
