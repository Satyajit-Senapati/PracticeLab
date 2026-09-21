"""serialize_deserialize_binary_tree.py

Problem Statement:
Implement a Python module that serializes and deserializes a binary tree to and
from a string representation.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, BFS serialization, recursion, and data
structure encoding
Real-world Use Case: Tree persistence, data transfer, and storage of
hierarchical structures.
Input Description: Functions accept the root of a binary tree or a serialized
string.
Output Description: Functions return a serialized string or reconstruct the
binary tree root.
Example Inputs and Outputs:
    root = [1,2,3,null,null,4,5]
    serialize(root) -> "1,2,3,null,null,4,5"
Constraints: Use a format that supports reconstruction of tree structure.
Brute Force Approach: Use recursive string concatenation.
Optimized Approach: Use BFS to serialize and deserialize reliably.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    convert nodes to values, include null markers, rebuild valid tree.
Edge Cases: empty tree, single-node tree, and trees with missing children.
Common Mistakes: dropping null placeholders, not using the same format for both
operations, and not consuming tokens correctly.
Follow-up Interview Questions:
    1. How would you serialize a binary search tree more compactly?
    2. What other formats could you use besides comma-separated values?
    3. Can you support trees with arbitrary node values including commas?
Alternative Approaches: Use preorder traversal with null markers.
Expected Output: The script prints serialized and deserialized tree structures.
Key Takeaways: Consistent encoding and decoding rules are critical for lossless tree serialization.
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


def serialize(root: Optional[TreeNode]) -> str:
    """Serialize a binary tree into a string using level-order traversal."""
    if root is None:
        return ""

    result: list[str] = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    return ",".join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    """Deserialize a string back into a binary tree."""
    if not data:
        return None

    nodes = data.split(",")
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    index = 1

    while queue and index < len(nodes):
        node = queue.popleft()
        if nodes[index] != "null":
            node.left = TreeNode(int(nodes[index]))
            queue.append(node.left)
        index += 1

        if index < len(nodes) and nodes[index] != "null":
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)
        index += 1

    return root


def main() -> None:
    """Main function demonstrating binary tree serialization."""
    root = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(3, left=TreeNode(4), right=TreeNode(5)),
    )
    data = serialize(root)
    print("Serialized:", data)
    deserialized_root = deserialize(data)
    print("Deserialized root value:", deserialized_root.val if deserialized_root else None)


if __name__ == "__main__":
    main()
