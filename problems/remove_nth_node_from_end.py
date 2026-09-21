"""remove_nth_node_from_end.py

Problem Statement:
Implement a Python module that removes the n-th node from the end of a singly linked list.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: two-pointer technique, linked list traversal, dummy nodes,
in-place deletion
Real-world Use Case: Linked list manipulation, deletion by relative position,
data structure maintenance.
Input Description: Functions accept the head of a linked list and an integer n.
Output Description: Functions return the head of the modified list.
Example Inputs and Outputs:
    [1,2,3,4,5], n=2 -> [1,2,3,5]
    [1], n=1 -> []
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Count nodes and remove the (length-n)-th node.
Optimized Approach: Use fast and slow pointers to locate the predecessor of the node to remove.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    advance fast by n steps, then move fast and slow together until fast reaches end.
    remove slow.next.
Edge Cases: remove head, single-node list, and n equals list length.
Common Mistakes: not using a dummy node, off-by-one errors, and invalid pointer handling.
Follow-up Interview Questions:
    1. How can you remove the middle node in one pass?
    2. What if the list is doubly linked?
    3. Can you solve this recursively?
Alternative Approaches: Use a list to store nodes and remove by index.
Expected Output: The script prints lists after removal for sample inputs.
Key Takeaways: Two-pointer traversal removes nodes from the end without extra memory.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the n-th node from the end of the list and return the new head."""
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    for _ in range(n + 1):
        if first:
            first = first.next
    while first:
        first = first.next
        second = second.next

    if second and second.next:
        second.next = second.next.next

    return dummy.next


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
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
        ([1, 2], 1),
    ]
    for values, n in examples:
        head = build_list(values)
        result = remove_nth_from_end(head, n)
        print(values, "n=", n, "->", list_to_values(result))


if __name__ == "__main__":
    main()
