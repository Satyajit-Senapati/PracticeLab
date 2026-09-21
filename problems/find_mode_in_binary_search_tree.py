"""find_mode_in_binary_search_tree.py

Problem Statement:
Implement a Python module that finds the mode(s) (most frequent element(s)) in a binary search tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BST traversal, frequency counting, state tracking,
handling duplicates
Real-world Use Case: Identifying most common values in sorted hierarchical data,
analytics on search-tree distributions.
Input Description: Function accepts the root of a BST.
Output Description: Returns a list of values that appear most frequently.
Example Inputs and Outputs:
    root = [1,null,2,2] -> [2]
Constraints: Use O(n) time and O(1) extra space if possible with inorder traversal.
Brute Force Approach: Flatten values and count frequencies with a dictionary.
Optimized Approach: Use inorder traversal to count consecutive duplicate values.
Time Complexity: O(n)
Space Complexity: O(h) recursion stack
Step-by-step Dry Run:
    traverse inorder, track current value count, update modes when count matches or exceeds max.
Edge Cases: empty tree and all unique values.
Common Mistakes: resetting counts incorrectly or using extra space unnecessarily.
Follow-up Interview Questions:
    1. How do duplicate values affect BST traversal?
    2. Can you do this without extra memory for counts?
    3. What if the tree is not a BST?
Alternative Approaches: Use a hashtable on all values.
Expected Output: The script prints the mode(s) for a sample BST.
Key Takeaways: Inorder traversal of BST groups duplicates consecutively, enabling efficient mode detection.
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


def find_mode(root: Optional[TreeNode]) -> List[int]:
    """Return the mode(s) of the BST."""
    modes: List[int] = []
    max_count = 0
    current_count = 0
    prev_value: Optional[int] = None

    def update_modes(value: int) -> None:
        nonlocal max_count, current_count
        if current_count > max_count:
            max_count = current_count
            modes.clear()
            modes.append(value)
        elif current_count == max_count:
            modes.append(value)

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal prev_value, current_count
        if not node:
            return

        inorder(node.left)

        if prev_value is None or prev_value != node.val:
            current_count = 1
        else:
            current_count += 1

        prev_value = node.val
        update_modes(node.val)

        inorder(node.right)

    inorder(root)
    return modes


def main() -> None:
    root = TreeNode(1, right=TreeNode(2, left=TreeNode(2)))
    print("Modes:", find_mode(root))


if __name__ == "__main__":
    main()
