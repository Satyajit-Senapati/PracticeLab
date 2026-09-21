"""minimum_depth_of_binary_tree.py

Problem Statement:
Implement a Python module that finds the minimum depth of a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, BFS, depth measurement,
leaf node definition
Real-world Use Case: Estimating shallowest access point in hierarchical data or computing minimum path lengths.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns the minimum number of nodes from the root to the nearest leaf.
Example Inputs and Outputs:
    root = [3,9,20,null,null,15,7] -> 2
Constraints: Use BFS for optimal depth discovery.
Brute Force Approach: DFS all paths and track minimum leaf depth.
Optimized Approach: BFS stops at the first leaf encountered.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    traverse level by level until a leaf node is found.
Edge Cases: empty tree and single-node tree.
Common Mistakes: treating null child as leaf or not handling missing subtree correctly.
Follow-up Interview Questions:
    1. How to compute maximum depth instead?
    2. Does DFS or BFS change complexity?
    3. What defines a leaf in this problem?
Alternative Approaches: Use recursive DFS with min depth update.
Expected Output: The script prints the minimum depth for a sample tree.
Key Takeaways: Breadth-first search finds minimum depth efficiently.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def min_depth(root: Optional[TreeNode]) -> int:
    """Return the minimum depth of the binary tree."""
    if not root:
        return 0

    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


def main() -> None:
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print("Minimum depth:", min_depth(root))


if __name__ == "__main__":
    main()
