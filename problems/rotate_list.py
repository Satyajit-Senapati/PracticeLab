"""rotate_list.py

Problem Statement:
Implement a Python module that rotates a linked list to the right by k places.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked list length, pointer wrapping, cyclic list manipulation,
modulo arithmetic
Real-world Use Case: Cyclic rotations, queue adjustments, and list realignment.
Input Description: Functions accept the head of a linked list and an integer k.
Output Description: Functions return the head of the rotated list.
Example Inputs and Outputs:
    [1,2,3,4,5], k=2 -> [4,5,1,2,3]
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Perform k rotations by moving the tail each time.
Optimized Approach: Connect the list into a ring and break at the correct point.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    length=5, k=2 -> new tail at position 3 -> break ring and rotate.
Edge Cases: empty list, k=0, k multiples of list length.
Common Mistakes: incorrect modulo computation, losing tail connection, and invalid break position.
Follow-up Interview Questions:
    1. How would you rotate left instead?
    2. Can you perform the rotation with recursion?
    3. What if k is negative?
Alternative Approaches: Use an array of nodes and rebuild pointers.
Expected Output: The script prints rotated lists for sample inputs.
Key Takeaways: Converting to a ring simplifies list rotations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Rotate the list right by k places and return the new head."""
    if not head or not head.next or k == 0:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    tail.next = head
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    return new_head


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
        ([0, 1, 2], 4),
        ([], 1),
    ]
    for values, k in examples:
        head = build_list(values)
        rotated = rotate_right(head, k)
        print(values, "k=", k, "->", list_to_values(rotated))


if __name__ == "__main__":
    main()
