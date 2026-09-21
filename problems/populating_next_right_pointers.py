"""populating_next_right_pointers.py

Problem Statement:
Implement a Python module that populates each node's next pointer to its right adjacent node in the same level.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: tree traversal, BFS, pointer linking, level order processing,
next pointer maintenance
Real-world Use Case: Constructing sibling links in tree structures for fast horizontal navigation.
Input Description: Function accepts the root of a perfect binary tree.
Output Description: Returns the root with next pointers populated.
Example Inputs and Outputs:
    root = [1,2,3,4,5,6,7] -> next pointers link 2->3 and 4->5->6->7.
Constraints: Use O(1) extra space, excluding recursion stack for the perfect tree variant.
Brute Force Approach: Level-order traversal with a queue.
Optimized Approach: Use already established next pointers to traverse level by level.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    connect left child to right child and right child to next level's left child when available.
Edge Cases: empty tree and leaf nodes.
Common Mistakes: not using next pointers across parents or mishandling the last node in a level.
Follow-up Interview Questions:
    1. How does this change for non-perfect trees?
    2. Can you do this iteratively without extra queue space?
    3. What is the runtime for trees with missing nodes?
Alternative Approaches: Use BFS queue for general binary trees.
Expected Output: The script prints next pointers for each level of a sample perfect tree.
Key Takeaways: Perfect binary trees allow level connections using existing next pointers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """Node with next pointer."""
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    next: Optional["Node"] = None


def connect(root: Optional[Node]) -> Optional[Node]:
    """Connect next pointers for each node on the same level."""
    if not root:
        return None

    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left

    return root


def print_levels(root: Optional[Node]) -> None:
    """Print nodes by level using next pointers."""
    level = root
    while level:
        current = level
        values = []
        while current:
            values.append(current.val)
            current = current.next
        print(values)
        level = level.left


def main() -> None:
    root = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7)))
    connect(root)
    print_levels(root)


if __name__ == "__main__":
    main()
