"""closest_binary_search_tree_value.py

Problem Statement:
Implement a Python module that finds the value in a binary search tree that is closest to a target.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST traversal, numeric comparison, recursion,
search space pruning
Real-world Use Case: Nearest neighbor search in tree-based indexes, and approximate query results.
Input Description: Function accepts the root of a BST and a target float value.
Output Description: Returns the BST value closest to the target.
Example Inputs and Outputs:
    root = [4,2,5,1,3], target = 3.714286 -> 4
Constraints: Use O(h) average time.
Brute Force Approach: Traverse the whole tree and track the closest value.
Optimized Approach: Use BST ordering to move left or right based on the target.
Time Complexity: O(h)
Space Complexity: O(h)
Step-by-step Dry Run:
    compare current node to target, update closest, then move to left or right child.
Edge Cases: empty tree, target exactly equal to a node value.
Common Mistakes: not updating closest before descending or ignoring float closeness.
Follow-up Interview Questions:
    1. Can you find the k closest values instead?
    2. What if the tree is not a BST?
    3. How to handle repeated values?
Alternative Approaches: Use inorder traversal and binary search on sorted values.
Expected Output: The script prints the closest tree value for a sample target.
Key Takeaways: BST ordering lets you narrow candidate values efficiently.
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


def closest_value(root: Optional[TreeNode], target: float) -> Optional[int]:
    """Return the value in the BST closest to the target."""
    closest = None
    closest_diff = float("inf")
    current = root

    while current:
        diff = abs(current.val - target)
        if diff < closest_diff:
            closest_diff = diff
            closest = current.val

        if target < current.val:
            current = current.left
        else:
            current = current.right

    return closest


def main() -> None:
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(5))
    print("Closest value to 3.7:", closest_value(root, 3.7))


if __name__ == "__main__":
    main()
