"""reorder_list.py

Problem Statement:
Implement a Python module that reorders a singly linked list from:
L0->L1->…->Ln-1->Ln into L0->Ln->L1->Ln-1->L2->Ln-2->….

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: slow/fast pointers, list reversal, in-place pointer manipulation,
linked list splitting
Real-world Use Case: Reordering sequences in place without extra memory,
media playlist shuffling, and pointer-based list transformations.
Input Description: Functions accept the head of a singly linked list.
Output Description: Functions reorder the list in place and return the head.
Example Inputs and Outputs:
    [1,2,3,4] -> [1,4,2,3]
    [1,2,3,4,5] -> [1,5,2,4,3]
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Build a list of nodes, reorder values, and reconstruct.
Optimized Approach: Find the midpoint, reverse the second half, and merge halves.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    split the list after midpoint -> reverse second half -> merge alternating.
Edge Cases: empty list, single-node list, and two-node list.
Common Mistakes: not terminating the merged list properly, forgetting to split,
and not handling odd-length lists correctly.
Follow-up Interview Questions:
    1. How would you reorder using recursion?
    2. Can you do this with a doubly linked list more easily?
    3. What if the list is circular?
Alternative Approaches: Use a deque or array of node references.
Expected Output: The script prints reordered lists for sample inputs.
Key Takeaways: Reordering can be done in-place using midpoint splitting and merging.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reorder the list in-place and return the list head."""
    if not head or not head.next:
        return head

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev: Optional[ListNode] = None
    current = second
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second = prev

    first, second = head, second
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2

    return head


def build_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def list_to_values(head: Optional[ListNode]) -> list[int]:
    values: list[int] = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def main() -> None:
    examples = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1],
    ]
    for values in examples:
        head = build_list(values)
        reordered = reorder_list(head)
        print(values, "->", list_to_values(reordered))


if __name__ == "__main__":
    main()
