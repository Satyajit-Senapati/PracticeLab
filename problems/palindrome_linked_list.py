"""palindrome_linked_list.py

Problem Statement:
Implement a Python module to determine if a singly linked list is a palindrome.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: slow/fast pointers, list reversal, two-pointer comparison,
space-efficient algorithms
Real-world Use Case: Sequence symmetry checks, structural validation, and
palindromic data detection.
Input Description: Functions accept the head of a linked list.
Output Description: Functions return True if the list values form a palindrome.
Example Inputs and Outputs:
    [1,2,2,1] -> True
    [1,2] -> False
Constraints: Use O(n) time and O(1) extra space.
Brute Force Approach: Copy values to an array and check palindrome.
Optimized Approach: Reverse the second half of the list and compare halves.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    find midpoint, reverse second half, compare mirrored values.
Edge Cases: empty list, single-node list, and odd-length lists.
Common Mistakes: not restoring the list, incorrect midpoint handling, and comparing wrong nodes.
Follow-up Interview Questions:
    1. How would you do this recursively?
    2. Can you restore the list after checking?
    3. What if you need the longest palindromic sublist instead?
Alternative Approaches: Use an array of values and check equality.
Expected Output: The script prints palindrome checks for sample lists.
Key Takeaways: In-place reversal of the second half enables constant-space palindrome detection.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def is_palindrome(head: Optional[ListNode]) -> bool:
    """Return True if the linked list is a palindrome."""
    if not head or not head.next:
        return True

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev: Optional[ListNode] = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    first, second = head, prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


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
    examples = [
        [1, 2, 2, 1],
        [1, 2],
        [1],
    ]
    for values in examples:
        head = build_list(values)
        print(values, "->", is_palindrome(head))


if __name__ == "__main__":
    main()
