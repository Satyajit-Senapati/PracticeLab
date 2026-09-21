"""reverse_linked_list.py

Problem Statement:
Implement a Python module that reverses a singly linked list.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: pointers, linked list traversal, in-place reversal,
iterative and recursive approaches
Real-world Use Case: Reversing data streams, undo operations, and list
management in low-level data structures.
Input Description: Functions accept the head of a singly linked list.
Output Description: Functions return the head of the reversed list.
Example Inputs and Outputs:
    1 -> 2 -> 3 -> 4 -> None becomes 4 -> 3 -> 2 -> 1 -> None
Constraints: Use O(n) time and O(1) extra space for the iterative method.
Brute Force Approach: Use a stack to collect nodes then rebuild the list.
Optimized Approach: Reverse the `next` pointers in one pass.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    current=1, prev=None -> current.next = prev -> prev=1 -> current=2
    return prev at end for reversed head
Edge Cases: empty list, single-node list, and two-node list.
Common Mistakes: losing the next node, forgetting to set tail.next to None,
and using extra space unnecessarily.
Follow-up Interview Questions:
    1. How would you reverse a linked list recursively?
    2. Can you reverse nodes in groups of k?
    3. What changes if the list is doubly linked?
Alternative Approaches: Use a stack or array to temporarily store nodes.
Expected Output: The script prints the reversed list for sample inputs.
Key Takeaways: In-place pointer reversal is the standard O(n) solution.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list iteratively and return the new head."""
    prev: Optional[ListNode] = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def build_list(values: list[int]) -> Optional[ListNode]:
    """Build a linked list from a list of integers."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def list_to_values(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a list of integer values."""
    values: list[int] = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def main() -> None:
    """Main function demonstrating linked list reversal."""
    examples = [
        [1, 2, 3, 4, 5],
        [1],
        [],
    ]
    for values in examples:
        head = build_list(values)
        reversed_head = reverse_list(head)
        print(values, "->", list_to_values(reversed_head))


if __name__ == "__main__":
    main()
