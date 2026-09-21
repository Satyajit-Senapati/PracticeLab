"""partition_list.py

Problem Statement:
Implement a Python module that partitions a linked list around a value x such
that all nodes less than x come before nodes greater than or equal to x.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked list traversal, two-list construction, stability,
in-place node rearrangement
Real-world Use Case: Partitioning jobs, threshold-based ordering, and
stable reordering of sequential data.
Input Description: Functions accept the head of a linked list and an integer x.
Output Description: Functions return the head of the partitioned list.
Example Inputs and Outputs:
    [1,4,3,2,5,2], x=3 -> [1,2,2,4,3,5]
Constraints: Preserve the original relative order within each partition.
Brute Force Approach: Extract node values, partition arrays, and rebuild.
Optimized Approach: Build two lists and concatenate them.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    build less and greater lists, then join them.
Edge Cases: all nodes less than x, all nodes greater than or equal to x, and empty list.
Common Mistakes: losing node links, not terminating the greater list, and
swapping values instead of nodes.
Follow-up Interview Questions:
    1. How would you partition a doubly linked list?
    2. Can you do this in one pass without extra dummy nodes?
    3. What if x can change per node?
Alternative Approaches: Use arrays to partition values before rebuilding.
Expected Output: The script prints partitioned lists for sample inputs.
Key Takeaways: Two-list merging preserves stability and avoids complex pointer juggling.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """Partition the list around x and return the new head."""
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head

    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    after.next = None
    before.next = after_head.next
    return before_head.next


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
        ([1, 4, 3, 2, 5, 2], 3),
        ([2, 1], 2),
        ([], 1),
    ]
    for values, x in examples:
        head = build_list(values)
        result = partition(head, x)
        print(values, "x=", x, "->", list_to_values(result))


if __name__ == "__main__":
    main()
