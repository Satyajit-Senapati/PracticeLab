"""merge_k_sorted_lists.py

Problem Statement:
Merge k sorted linked lists and return the merged sorted list.

Interview Difficulty: Hard
Commonly Asked By: Google, Facebook, Amazon, Microsoft
Concepts Tested: priority queues, divide and conquer, linked list merging.
Real-world Use Case: merging sorted streams or results from distributed systems.
Input Description: A list of heads of sorted linked lists.
Output Description: The head of the merged sorted list.
Example Inputs and Outputs:
    [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
Constraints: Use O(n log k) time where n is total number of nodes.
Time Complexity: O(N log k)
Space Complexity: O(k) for the heap.
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import Optional

@dataclass(order=True)
class HeapNode:
    val: int
    node: "ListNode" = field(compare=False)  # Only values participate in heap ordering.


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists into one sorted list."""
    heap: list[HeapNode] = []
    for node in lists:
        if node:
            heapq.heappush(heap, HeapNode(node.val, node))

    dummy = ListNode(0)
    tail = dummy
    while heap:
        smallest = heapq.heappop(heap)
        tail.next = smallest.node
        tail = tail.next
        if smallest.node.next:
            heapq.heappush(heap, HeapNode(smallest.node.next.val, smallest.node.next))

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
    while head:
        values.append(head.val)
        head = head.next
    return values


def main() -> None:
    examples = [
        [[1, 4, 5], [1, 3, 4], [2, 6]],
        [[], [0]],
    ]
    for list_values in examples:
        lists = [build_list(values) for values in list_values]
        merged = merge_k_lists(lists)
        print([list_to_values(node) for node in lists], "->", list_to_values(merged))


if __name__ == "__main__":
    main()
