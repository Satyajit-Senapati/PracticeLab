"""invert_binary_tree.py

Problem Statement:
Implement a Python module that inverts a binary tree (mirror image transformation).

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, tree traversal, swapping child nodes,
structural transformation
Real-world Use Case: Tree reflection operations, mirroring hierarchical data,
and image processing analogies.
Input Description: Function accepts the root of a binary tree.
Output Description: Returns the root of the inverted tree.
Example Inputs and Outputs:
    root = [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
Constraints: Use O(n) time and O(h) space.
Brute Force Approach: Create a new mirrored tree node-by-node.
Optimized Approach: Swap left and right children in-place recursively.
Time Complexity: O(n)
Space Complexity: O(h)
Step-by-step Dry Run:
    swap children at each node, recurse into left and right subtrees.
Edge Cases: empty tree and single-node tree.
Common Mistakes: not returning the root or swapping incorrectly.
Follow-up Interview Questions:
    1. Can you invert the tree iteratively?
    2. How would you test tree symmetry after inversion?
    3. Does inversion preserve BST ordering? (No.)
Alternative Approaches: Use BFS with a queue and swap children level by level.
Expected Output: The script prints level order output of the inverted tree.
Key Takeaways: Inversion flips left and right child pointers at every node.
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


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree and return its root."""
    if not root:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
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
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))
    inverted = invert_tree(root)
    print("Inverted level order:", level_order(inverted))


if __name__ == "__main__":
    main()
