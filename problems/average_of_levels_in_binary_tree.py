"""average_of_levels_in_binary_tree.py

Problem Statement:
Implement a Python module that computes the average value of nodes at each level
in a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: breadth-first traversal, level aggregation, arithmetic mean,
queue usage
Real-world Use Case: Level-based statistics, hierarchical summarization, and
aggregating tree metrics.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns a list of averages for each depth level.
Example Inputs and Outputs:
    root = [3,9,20,null,null,15,7] -> [3.0, 14.5, 11.0]
Constraints: Use O(n) time and O(n) space.
Brute Force Approach: Collect all nodes by level in separate lists.
Optimized Approach: Track level sums and counts during BFS.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    traverse each level with a queue, compute average = sum/count.
Edge Cases: empty tree and one-node tree.
Common Mistakes: integer division in Python 2 or forgetting float conversion.
Follow-up Interview Questions:
    1. How to compute median instead of average?
    2. Can you compute min/max per level too?
    3. How would this work with weighted nodes?
Alternative Approaches: Use DFS with depth tracking and count/sum arrays.
Expected Output: The script prints level averages for a sample tree.
Key Takeaways: BFS is natural for level-wise aggregation.
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


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    """Return the average value of nodes at each tree level."""
    if not root:
        return []

    averages: List[float] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        averages.append(level_sum / level_size)

    return averages


def main() -> None:
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print("Level averages:", average_of_levels(root))


if __name__ == "__main__":
    main()
