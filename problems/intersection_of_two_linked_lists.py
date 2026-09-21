"""intersection_of_two_linked_lists.py

Problem Statement:
Implement a Python module that finds the intersection node of two singly linked lists.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: pointer traversal, list alignment, linked list intersection,
cycle-free list logic
Real-world Use Case: Identifying shared nodes in pointer-based data
structures and merging linked data paths.
Input Description: Functions accept the heads of two singly linked lists.
Output Description: Functions return the intersecting node or None if no intersection exists.
Example Inputs and Outputs:
    listA = [4,1,8,4,5], listB = [5,6,1,8,4,5] -> intersection at node with value 8
Constraints: Use O(n + m) time and O(1) extra space.
Brute Force Approach: Use a hash set of nodes from the first list.
Optimized Approach: Advance pointers in both lists and align them by length.
Time Complexity: O(n + m)
Space Complexity: O(1)
Step-by-step Dry Run:
    compute lengths, align starts, advance both until nodes match.
Edge Cases: no intersection, one or both lists empty, intersection at head.
Common Mistakes: comparing values instead of node references, not aligning lists, and using extra memory unnecessarily.
Follow-up Interview Questions:
    1. How would you find intersection if the lists may contain cycles?
    2. Can you use a hash set and what is the tradeoff?
    3. What if values instead of nodes define intersection?
Alternative Approaches: Use pointers redirected to the other list's head.
Expected Output: The script prints the intersection value or None for sample inputs.
Key Takeaways: Aligning pointer traversal lengths enables O(1) space intersection detection.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def get_length(head: Optional[ListNode]) -> int:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


def get_intersection_node(
    headA: Optional[ListNode], headB: Optional[ListNode]
) -> Optional[ListNode]:
    """Return the intersection node of two singly linked lists."""
    lenA = get_length(headA)
    lenB = get_length(headB)

    while lenA > lenB and headA:
        headA = headA.next
        lenA -= 1
    while lenB > lenA and headB:
        headB = headB.next
        lenB -= 1

    while headA and headB:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


def build_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def main() -> None:
    intersect = build_list([8, 4, 5])
    headA = build_list([4, 1])
    headB = build_list([5, 6, 1])
    tailA = headA
    while tailA and tailA.next:
        tailA = tailA.next
    if tailA:
        tailA.next = intersect
    tailB = headB
    while tailB and tailB.next:
        tailB = tailB.next
    if tailB:
        tailB.next = intersect

    intersection = get_intersection_node(headA, headB)
    print("Intersection value:", intersection.val if intersection else None)


if __name__ == "__main__":
    main()
