"""construct_binary_tree_from_preorder_inorder.py

Problem Statement:
Implement a Python module that reconstructs a binary tree from preorder and inorder traversal lists.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: recursion, tree construction, traversal relationships,
index mapping
Real-world Use Case: Rehydrating tree structure from traversal outputs,
parsing expression trees, and restoring serialized trees.
Input Description: Functions accept a preorder list and an inorder list.
Output Description: Functions return the reconstructed binary tree root.
Example Inputs and Outputs:
    preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] -> reconstructed tree root
Constraints: Use O(n) time with a value-index map.
Brute Force Approach: Search for root positions in inorder within recursion.
Optimized Approach: Use a hash map for inorder indices and traverse preorder sequentially.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    root = preorder[0], split inorder at root index, recursively build left and right.
Edge Cases: empty lists, single-node tree.
Common Mistakes: incorrect index boundaries, rebuilding from invalid input, and forgetting to increment preorder index.
Follow-up Interview Questions:
    1. How do preorder and inorder determine the tree uniquely?
    2. Can you construct from inorder and postorder instead?
    3. What if the tree contains duplicate values?
Alternative Approaches: Use iterative stack-based reconstruction.
Expected Output: The script prints preorder and inorder traversal of the reconstructed tree.
Key Takeaways: Preorder gives root order, inorder gives left/right partitioning.
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


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Build a binary tree from preorder and inorder traversal lists."""
    if not preorder or not inorder:
        return None

    inorder_index_map: Dict[int, int] = {value: idx for idx, value in enumerate(inorder)}
    preorder_index = 0

    def helper(left: int, right: int) -> Optional[TreeNode]:
        nonlocal preorder_index
        if left > right:
            return None

        root_value = preorder[preorder_index]
        root = TreeNode(root_value)
        preorder_index += 1

        inorder_index = inorder_index_map[root_value]
        root.left = helper(left, inorder_index - 1)
        root.right = helper(inorder_index + 1, right)
        return root

    return helper(0, len(inorder) - 1)


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def main() -> None:
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = build_tree(preorder, inorder)
    print("Preorder:", preorder_traversal(root))
    print("Inorder:", inorder_traversal(root))


if __name__ == "__main__":
    main()
