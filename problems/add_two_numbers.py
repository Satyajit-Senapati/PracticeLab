"""add_two_numbers.py

Problem Statement:
Implement a Python module that adds two numbers represented as reversed linked lists.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked list iteration, carry propagation, elementary addition,
node creation
Real-world Use Case: Arbitrary-precision arithmetic, big integer addition,
and digit-wise computations.
Input Description: Functions accept two reversed linked lists representing numbers.
Output Description: Functions return a linked list representing the sum.
Example Inputs and Outputs:
    [2,4,3] + [5,6,4] -> [7,0,8]
Constraints: Use O(max(n, m)) time and O(max(n, m)) space.
Brute Force Approach: Convert lists to integers, add, and rebuild the list.
Optimized Approach: Add digits directly with carry management.
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
Step-by-step Dry Run:
    add 2+5=7, 4+6=10 carry 1, 3+4+1=8 -> [7,0,8].
Edge Cases: different length lists, carry at final digit, and zeros.
Common Mistakes: forgetting final carry, using incorrect node order, and
modifying inputs in place incorrectly.
Follow-up Interview Questions:
    1. How would you add numbers in non-reversed order?
    2. Can you do this with recursion?
    3. What if digits exceed base 10?
Alternative Approaches: Use arrays to store digits before summing.
Expected Output: The script prints summed linked lists for sample inputs.
Key Takeaways: Digit-by-digit addition with carry mimics grade-school arithmetic.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node for a singly linked list."""
    val: int
    next: Optional["ListNode"] = None


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Add two reversed linked list numbers and return the result list."""
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0
        total = value1 + value2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

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
        ([2, 4, 3], [5, 6, 4]),
        ([0], [0]),
        ([9, 9, 9, 9], [1]),
    ]
    for l1_values, l2_values in examples:
        l1 = build_list(l1_values)
        l2 = build_list(l2_values)
        result = add_two_numbers(l1, l2)
        print(l1_values, "+", l2_values, "->", list_to_values(result))


if __name__ == "__main__":
    main()
