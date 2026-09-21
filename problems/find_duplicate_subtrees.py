"""find_duplicate_subtrees.py

Problem Statement:
Implement a Python module that finds all duplicate subtrees in a binary tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree serialization, hashing, subtree identification,
postorder traversal
Real-world Use Case: Detecting repeated patterns in hierarchical data and optimizing redundancy.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns a list of subtree roots that appear more than once.
Example Inputs and Outputs:
    root = [1,2,3,4,null,2,4,null,null,4] -> subtrees rooted at 2 and 4.
Constraints: Use O(n^2) worst-case time if many duplicate shapes,
but average O(n) with efficient serialization.
Brute Force Approach: Compare all subtree pairs.
Optimized Approach: Serialize subtrees and count occurrences in a map.
Time Complexity: O(n^2) worst-case, average O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    postorder serialize each subtree, count serialization frequency, add roots for duplicates.
Edge Cases: empty tree, all unique nodes.
Common Mistakes: adding the same duplicate subtree root multiple times.
Follow-up Interview Questions:
    1. How to avoid collisions in subtree serialization?
    2. Can you use structural hashing instead?
    3. What if subtree equality is expensive?
Alternative Approaches: Use tuple representation of subtree structure.
Expected Output: The script prints the values of duplicate subtree roots.
Key Takeaways: Duplicate subtrees can be detected by normalized subtree representation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[TreeNode]:
    """Return duplicate subtree roots."""
    trees: Dict[Tuple[int, Optional[int], Optional[int]], int] = {}
    duplicates: List[TreeNode] = []

    def lookup(node: Optional[TreeNode]) -> Optional[int]:
        if not node:
            return None
        left_id = lookup(node.left)
        right_id = lookup(node.right)
        tree_id = (node.val, left_id, right_id)
        trees[tree_id] = trees.get(tree_id, 0) + 1
        if trees[tree_id] == 2:
            duplicates.append(node)
        return hash(tree_id)

    lookup(root)
    return duplicates


def main() -> None:
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4)),
        right=TreeNode(3, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(4)),
    )
    duplicates = find_duplicate_subtrees(root)
    print("Duplicate subtree roots:", [node.val for node in duplicates])


if __name__ == "__main__":
    main()
