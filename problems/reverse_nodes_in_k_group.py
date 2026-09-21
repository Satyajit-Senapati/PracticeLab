"""reverse_nodes_in_k_group.py

Problem Statement:
Implement a Python module that reverses nodes in k-group chunks in a linked list.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked list manipulation, group reversal, pointer management,
edge-case handling
Real-world Use Case: Batch processing of sequential records, block-wise
transformations, and chunk reordering in data streams.
Input Description: Functions accept the head of a linked list and an integer k.
Output Description: Functions return the head of the modified list.
Example Inputs and Outputs:
    [1,2,3,4,5], k=2 -> [2,1,4,3,5]
    [1,2,3,4,5], k=3 -> [3,2,1,4,5]
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Extract values in groups, reverse chunks, and rebuild the list.
Optimized Approach: Reverse nodes in place for each full k-group.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    reverse first k nodes, attach reversed group, repeat for remaining nodes.
Edge Cases: k = 1, list length less than k, and final incomplete group.
Common Mistakes: losing the remainder list, failing to connect group tails,
and reversing only one group incorrectly.
Follow-up Interview Questions:
    1. How would you reverse nodes in groups of variable sizes?
    2. Can you do this recursively?
    3. What if the list is circular?
Alternative Approaches: Use a stack to reverse each group.
Expected Output: The script prints transformed lists for sample inputs.
Key Takeaways: In-place group reversal preserves list structure while reversing blocks.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def reverse_nodes_in_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverse nodes in k-sized groups and return the new head."""
    dummy = ListNode(0, head)
    group_prev = dummy

    def get_kth_node(start: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = start
        for _ in range(k - 1):
            if current is None:
                return None
            current = current.next
        return current

    while True:
        kth = get_kth_node(group_prev.next, k)
        if not kth:
            break

        group_next = kth.next
        prev, current = kth.next, group_prev.next

        while current is not group_next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        tail = group_prev.next
        group_prev.next = kth
        group_prev = tail

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
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 2),
    ]
    for values, k in examples:
        head = build_list(values)
        result = reverse_nodes_in_k_group(head, k)
        print(values, "k=", k, "->", list_to_values(result))


if __name__ == "__main__":
    main()
