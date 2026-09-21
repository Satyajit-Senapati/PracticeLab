"""path_sum_ii.py

Problem Statement:
Implement a Python module that finds all root-to-leaf paths in a binary tree where the sum of node values equals a target.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, backtracking, path accumulation,
root-to-leaf exploration
Real-world Use Case: Path-based filtering, route sum checks, and decision tree evaluations.
Input Description: Function accepts the root of a binary tree and a target sum.
Output Description: Returns a list of paths where each path is a list of node values.
Example Inputs and Outputs:
    root = [5,4,8,11,null,13,4,7,2,null,null,5,1], target = 22 -> [[5,4,11,2],[5,8,4,5]]
Constraints: Use backtracking to build paths and prune invalid branches.
Brute Force Approach: Explore all root-to-leaf paths and compute sums after.
Optimized Approach: Track current sum and path during DFS.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    traverse left and right children, update current path and sum, append valid leaf paths.
Edge Cases: empty tree and no matching paths.
Common Mistakes: not copying the path list when adding results, missing leaf-only condition.
Follow-up Interview Questions:
    1. How does this change for path sum to any node, not just leaf?
    2. Can you solve iteratively?
    3. What if node values can be negative?
Alternative Approaches: Use recursion or stack with path state.
Expected Output: The script prints all valid root-to-leaf paths for a sample tree.
Key Takeaways: Backtracking efficiently generates valid root-to-leaf paths.
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


def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """Return all root-to-leaf paths where the sum equals target_sum."""
    results: List[List[int]] = []
    path: List[int] = []

    def dfs(node: Optional[TreeNode], current_sum: int) -> None:
        if not node:
            return

        path.append(node.val)
        current_sum += node.val

        if not node.left and not node.right and current_sum == target_sum:
            results.append(path.copy())
        else:
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        path.pop()

    dfs(root, 0)
    return results


def main() -> None:
    root = TreeNode(
        5,
        left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
        right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, left=TreeNode(5), right=TreeNode(1))),
    )
    print("Paths with sum 22:", path_sum(root, 22))


if __name__ == "__main__":
    main()
