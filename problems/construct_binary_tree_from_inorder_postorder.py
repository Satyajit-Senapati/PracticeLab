"""construct_binary_tree_from_inorder_postorder.py

Problem Statement:
Implement a Python module that reconstructs a binary tree from inorder and postorder traversal lists.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, tree construction, traversal relationships,
index mapping
Real-world Use Case: Tree reconstruction from traversal outputs,
serialization/deserialization, and parsing hierarchical data.
Input Description: Functions accept an inorder list and a postorder list.
Output Description: Functions return the reconstructed binary tree root.
Example Inputs and Outputs:
    inorder = [9,3,15,20,7], postorder = [9,15,7,20,3] -> reconstructed tree root
Constraints: Use O(n) time with a value-index map.
Brute Force Approach: Search for root positions in inorder within recursion.
Optimized Approach: Use a hash map and traverse postorder backwards.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    root = postorder[-1], split inorder at root index, build right then left.
Edge Cases: empty lists, single-node tree.
Common Mistakes: incorrect postorder index decrement, wrong subtree order, and duplicate values.
Follow-up Interview Questions:
    1. How does postorder differ in root position from preorder?
    2. Can you construct from preorder and postorder?
    3. What changes if values repeat?
Alternative Approaches: Use an iterative stack with explicit bounds.
Expected Output: The script prints preorder and inorder traversal of the reconstructed tree.
Key Takeaways: Postorder root appears at the end, inorder partitions left/right.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    """Build a binary tree from inorder and postorder traversal lists."""
    if not inorder or not postorder:
        return None

    inorder_index_map: Dict[int, int] = {value: idx for idx, value in enumerate(inorder)}
    postorder_index = len(postorder) - 1

    def helper(left: int, right: int) -> Optional[TreeNode]:
        nonlocal postorder_index
        if left > right:
            return None

        root_value = postorder[postorder_index]
        root = TreeNode(root_value)
        postorder_index -= 1

        inorder_index = inorder_index_map[root_value]
        root.right = helper(inorder_index + 1, right)
        root.left = helper(left, inorder_index - 1)
        return root

    return helper(0, len(inorder) - 1)


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def main() -> None:
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = build_tree(inorder, postorder)
    print("Preorder:", preorder_traversal(root))
    print("Inorder:", inorder_traversal(root))


if __name__ == "__main__":
    main()
