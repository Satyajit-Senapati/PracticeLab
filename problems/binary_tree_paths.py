"""binary_tree_paths.py

Problem Statement:
Implement a Python module that returns all root-to-leaf paths in a binary tree.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, recursion, path building, depth-first search
Real-world Use Case: Extracting paths in hierarchical data, debug tracing,
and tree serialization.
Input Description: Functions accept the root of a binary tree.
Output Description: Functions return a list of strings representing root-to-leaf paths.
Example Inputs and Outputs:
    [1,2,3,null,5] -> ["1->2->5","1->3"]
Constraints: Use O(n) time and O(h) space.
Brute Force Approach: Explore every path from root to leaf.
Optimized Approach: Build paths incrementally during DFS.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    traverse tree, append path at leaf nodes.
Edge Cases: empty tree, single node tree.
Common Mistakes: not copying path state, missing leaf conditions.
Follow-up Interview Questions:
    1. How do you adapt this for node values of other types?
    2. Can you return paths as lists instead of strings?
    3. How would you do this iteratively?
Alternative Approaches: Use DFS with explicit stack.
Expected Output: The script prints root-to-leaf paths for sample trees.
Key Takeaways: DFS builds path strings naturally during tree traversal.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """Return all root-to-leaf paths in the tree."""
    if root is None:
        return []

    paths: List[str] = []

    def dfs(node: TreeNode, current_path: str) -> None:
        if node.left is None and node.right is None:
            paths.append(current_path)
            return
        if node.left:
            dfs(node.left, f"{current_path}->{node.left.val}")
        if node.right:
            dfs(node.right, f"{current_path}->{node.right.val}")

    dfs(root, str(root.val))
    return paths


def main() -> None:
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3))
    print(binary_tree_paths(root))


if __name__ == "__main__":
    main()
