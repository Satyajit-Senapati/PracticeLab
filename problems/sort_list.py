"""sort_list.py

Problem Statement:
Implement a Python module that sorts a linked list in ascending order.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked list merge sort, recursion, divide-and-conquer,
stable sorting
Real-world Use Case: Sorting linked data in memory constrained systems and
converting unsorted sequences into ordered lists.
Input Description: Functions accept the head of a singly linked list.
Output Description: Functions return the head of the sorted list.
Example Inputs and Outputs:
    [4,2,1,3] -> [1,2,3,4]
Constraints: Use O(n log n) time and O(log n) recursion space.
Brute Force Approach: Convert to array, sort, and rebuild the list.
Optimized Approach: Use merge sort directly on the linked list.
Time Complexity: O(n log n)
Space Complexity: O(log n)
Step-by-step Dry Run:
    split list to halves, sort each half, merge sorted halves.
Edge Cases: empty list, single node, and already sorted list.
Common Mistakes: losing next pointers, incorrect midpoint split, and not using a dummy node during merge.
Follow-up Interview Questions:
    1. How does merge sort differ when applied to arrays vs linked lists?
    2. Can you do this in constant space?
    3. What is the advantage of merge sort for linked lists?
Alternative Approaches: Use top-down merge sort or bottom-up iterative merge.
Expected Output: The script prints sorted results for sample linked lists.
Key Takeaways: Merge sort on a linked list avoids random access and is stable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Sort a linked list in ascending order and return the sorted head."""
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)

    dummy = ListNode(0)
    tail = dummy
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
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
        [4, 2, 1, 3],
        [-1, 5, 3, 4, 0],
        [],
    ]
    for values in examples:
        head = build_list(values)
        sorted_head = sort_list(head)
        print(values, "->", list_to_values(sorted_head))


if __name__ == "__main__":
    main()
