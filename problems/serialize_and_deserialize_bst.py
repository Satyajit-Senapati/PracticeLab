"""serialize_and_deserialize_bst.py

Problem Statement:
Implement a Python module that serializes and deserializes a binary search tree.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, string encoding, BST property preservation,
serialization/deserialization
Real-world Use Case: Persisting tree-based indices, caching search structures, and
network transfer of tree data.
Input Description: Functions accept a BST root.
Output Description: A string serialization and a reconstructed BST root.
Example Inputs and Outputs:
    root = [2,1,3] -> "2,1,3" and reconstructed tree matching original.
Constraints: Must preserve BST structure and values.
Brute Force Approach: Serialize with level order including null markers.
Optimized Approach: Use preorder serialization and reconstruct using min/max bounds.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    serialize by preorder, deserialize by bounds and index increment.
Edge Cases: empty tree and single-node tree.
Common Mistakes: ignoring BST constraints, misparsing values, and failing on negative numbers.
Follow-up Interview Questions:
    1. How can you extend to a general binary tree?
    2. What are tradeoffs between preorder and level-order serialization?
    3. How do duplicates change the approach?
Alternative Approaches: Use inorder with null markers, or JSON-style lists.
Expected Output: The script prints serialized data and re-serialization of the reconstructed tree.
Key Takeaways: For BST, preorder with bounds is sufficient to reconstruct the tree uniquely.
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


def serialize(root: Optional[TreeNode]) -> str:
    """Serialize a BST to a string using preorder traversal."""
    values: List[str] = []

    def helper(node: Optional[TreeNode]) -> None:
        if not node:
            return
        values.append(str(node.val))
        helper(node.left)
        helper(node.right)

    helper(root)
    return ",".join(values)


def deserialize(data: str) -> Optional[TreeNode]:
    """Deserialize a string into a BST."""
    if not data:
        return None

    values = [int(token) for token in data.split(",")]
    index = 0

    def helper(lower: int, upper: int) -> Optional[TreeNode]:
        nonlocal index
        if index == len(values):
            return None

        value = values[index]
        if value < lower or value > upper:
            return None

        index += 1
        node = TreeNode(value)
        node.left = helper(lower, value)
        node.right = helper(value, upper)
        return node

    return helper(-10**9, 10**9)


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def main() -> None:
    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    serialized = serialize(root)
    print("Serialized:", serialized)
    reconstructed = deserialize(serialized)
    print("Reconstructed preorder:", preorder_traversal(reconstructed))


if __name__ == "__main__":
    main()
