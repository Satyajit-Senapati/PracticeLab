"""linked_list_cycle.py

Problem Statement:
Implement a Python module that determines whether a singly linked list contains a cycle.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: pointers, cycle detection, Floyd's tortoise and hare algorithm,
linked list traversal
Real-world Use Case: Detecting loops in linked data structures, network
traversal, and validation of pointer-based structures.
Input Description: Functions accept the head of a singly linked list.
Output Description: Functions return True if the list has a cycle, otherwise False.
Example Inputs and Outputs:
    [3,2,0,-4] with tail connecting to second node -> True
    [1,2] with no cycle -> False
Constraints: Use O(n) time and O(1) space.
Brute Force Approach: Use a hash set to track visited nodes.
Optimized Approach: Use two pointers moving at different speeds.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    slow and fast start at head, fast moves twice as fast, if they meet a cycle exists.
Edge Cases: empty list and single-node list.
Common Mistakes: advancing pointers incorrectly and missing the fast pointer null checks.
Follow-up Interview Questions:
    1. How can you find the start of the cycle?
    2. What if the list is doubly linked?
    3. How do you detect a cycle with recursion?
Alternative Approaches: Use a set of visited references for a simpler solution.
Expected Output: The script prints whether each sample list contains a cycle.
Key Takeaways: Floyd's cycle-finding algorithm detects loops in constant space.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def has_cycle(head: Optional[ListNode]) -> bool:
    """Return True if the linked list contains a cycle."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


def build_list(values: list[int], cycle_index: int = -1) -> Optional[ListNode]:
    """Build a linked list from values and optionally create a cycle."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
        nodes.append(current)

    if cycle_index != -1:
        current.next = nodes[cycle_index]

    return head


def main() -> None:
    """Main function demonstrating cycle detection."""
    examples = [
        ([3, 2, 0, -4], 1),
        ([1, 2], -1),
        ([], -1),
    ]
    for values, cycle_index in examples:
        head = build_list(values, cycle_index)
        print(values, "cycle_index=", cycle_index, "->", has_cycle(head))


if __name__ == "__main__":
    main()
