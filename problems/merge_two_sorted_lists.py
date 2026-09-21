"""merge_two_sorted_lists.py

Problem Statement:
Implement a Python module that merges two sorted singly linked lists into one
sorted list.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: pointer manipulation, linked list traversal, merging sorted
structures
Real-world Use Case: Merging sorted streams, ordered list union operations,
and merge step in merge sort.
Input Description: Functions accept the heads of two sorted linked lists.
Output Description: Functions return the head of the merged sorted list.
Example Inputs and Outputs:
    l1 = [1,2,4], l2 = [1,3,4] -> [1,1,2,3,4,4]
Constraints: Use O(n + m) time and O(1) extra space by reusing nodes.
Brute Force Approach: Convert lists to arrays, merge, and reconstruct the list.
Optimized Approach: Use two pointers to merge in place with a dummy head.
Time Complexity: O(n + m)
Space Complexity: O(1)
Step-by-step Dry Run:
    compare 1 and 1 -> add left, compare 2 and 1 -> add right, and continue.
Edge Cases: one empty list, both empty, and interleaved values.
Common Mistakes: losing next pointers, using extra lists, and not handling the
final tail correctly.
Follow-up Interview Questions:
    1. How would you merge k sorted lists?
    2. Can you merge lists recursively?
    3. What is the relation to the merge step in merge sort?
Alternative Approaches: Use a priority queue for k-way merging.
Expected Output: The script prints merged sorted lists for sample inputs.
Key Takeaways: In-place merging with a dummy node keeps code simple and efficient.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted linked lists and return the merged head."""
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


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
    """Main function demonstrating merging sorted linked lists."""
    examples = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([0], [0, 1]),
    ]
    for l1_values, l2_values in examples:
        l1 = build_list(l1_values)
        l2 = build_list(l2_values)
        merged = merge_two_lists(l1, l2)
        print(l1_values, l2_values, "->", list_to_values(merged))


if __name__ == "__main__":
    main()
