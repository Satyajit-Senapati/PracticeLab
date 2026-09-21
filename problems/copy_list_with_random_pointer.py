"""copy_list_with_random_pointer.py

Problem Statement:
Implement a Python module that creates a deep copy of a linked list where each
node has an additional random pointer pointing to any node in the list or None.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked list manipulation, pointer cloning, hash maps,
in-place node weaving
Real-world Use Case: Cloning complex object graphs, undo/redo history,
structure duplication with shared references.
Input Description: Functions accept the head node of a linked list with next
and random pointers.
Output Description: Functions return the head of a deep-copied list.
Example Inputs and Outputs:
    list: [7,13,11,10,1] with random pointers -> copied list with same values and random structure
Constraints: Use O(n) time and O(1) extra space for the optimal solution.
Brute Force Approach: Use a dictionary to map original nodes to clones.
Optimized Approach: Interleave cloned nodes with original nodes, assign random pointers, then separate lists.
Time Complexity: O(n)
Space Complexity: O(1) extra space (excluding output)
Step-by-step Dry Run:
    clone nodes and insert after originals -> assign random pointers -> detach cloned list.
Edge Cases: empty list, single-node list, and random pointers to None.
Common Mistakes: copying random pointers before clones exist, forgetting to detach clones,
and using node values instead of references.
Follow-up Interview Questions:
    1. How would you handle additional random pointers or multiple arbitrary references?
    2. What is the memory tradeoff between hash-map and interleaving approaches?
    3. How would you clone a graph with similar pointer structure?
Alternative Approaches: Use a hash map to store original->clone node mappings.
Expected Output: The script prints values and random targets for the cloned list.
Key Takeaways: Interleave cloned nodes and separate them to clone complex linked structures in linear time.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Node:
    """Node with next and random pointers."""
    val: int
    next: Optional["Node"] = None
    random: Optional["Node"] = None


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """Return a deep copy of the linked list with random pointers."""
    if head is None:
        return None

    current = head
    while current:
        cloned = Node(current.val, current.next)
        current.next = cloned
        current = cloned.next

    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    current = head
    copied_head = head.next
    while current and current.next:
        cloned = current.next
        current.next = cloned.next
        current = current.next
        if current:
            cloned.next = current.next

    return copied_head


def build_list(values: list[int], random_indices: list[int]) -> Optional[Node]:
    if not values:
        return None
    nodes: list[Node] = [Node(val) for val in values]
    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]
    for node, rand_idx in zip(nodes, random_indices):
        node.random = nodes[rand_idx] if rand_idx != -1 else None
    return nodes[0]


def print_list(head: Optional[Node]) -> list[tuple[int, Optional[int]]]:
    result: list[tuple[int, Optional[int]]] = []
    current = head
    while current:
        random_val = current.random.val if current.random else None
        result.append((current.val, random_val))
        current = current.next
    return result


def main() -> None:
    examples = [
        ([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0]),
        ([1, 2], [1, 1]),
        ([], []),
    ]
    for values, random_indices in examples:
        head = build_list(values, random_indices)
        copied = copy_random_list(head)
        print("original:", print_list(head))
        print("copied:  ", print_list(copied))


if __name__ == "__main__":
    main()
