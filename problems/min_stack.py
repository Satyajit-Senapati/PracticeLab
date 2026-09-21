"""min_stack.py

Problem Statement:
Implement a Python module for a stack that supports retrieving the minimum
value in constant time.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack design, auxiliary storage, amortized complexity,
data structure invariants
Real-world Use Case: Tracking minimum values in sliding windows, transaction
monitoring, and algorithmic stack operations.
Input Description: The data structure accepts push and pop operations, plus
peek and get-min operations.
Output Description: The module exposes a MinStack class with O(1) min retrieval.
Example Inputs and Outputs:
    stack.push(-2); stack.push(0); stack.push(-3)
    stack.get_min() -> -3
    stack.pop(); stack.top() -> 0
    stack.get_min() -> -2
Constraints: Keep all operations O(1) time.
Brute Force Approach: Scan the entire stack for min after each operation.
Optimized Approach: Maintain a secondary stack of minimum values.
Time Complexity: O(1) per operation
Space Complexity: O(n)
Step-by-step Dry Run:
    push -2, push 0, push -3
    min stack = [-2, -2, -3]
    return -3
Edge Cases: popping from empty stack, multiple equal minimum values, and
single-element stacks.
Common Mistakes: forgetting to synchronize auxiliary stack with main stack,
not handling empty stack states, and using a global min incorrectly.
Follow-up Interview Questions:
    1. Can you implement this with only one stack?
    2. How does space usage change with duplicate minima?
    3. What are other stack augmentation techniques?
Alternative Approaches: Maintain a stack of (value, current_min) tuples.
Expected Output: The script prints stack operations and tracked minimums.
Key Takeaways: Auxiliary storage enables constant-time min tracking.
"""

from __future__ import annotations

from typing import List, Optional


class MinStack:
    """A stack supporting constant-time retrieval of the minimum element."""

    def __init__(self) -> None:
        self._stack: List[int] = []
        self._min_stack: List[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        if not self._stack:
            return
        value = self._stack.pop()
        if self._min_stack and value == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> Optional[int]:
        return self._stack[-1] if self._stack else None

    def get_min(self) -> Optional[int]:
        return self._min_stack[-1] if self._min_stack else None


def main() -> None:
    """Main function demonstrating MinStack usage."""
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print("Current min:", stack.get_min())
    stack.pop()
    print("Top after pop:", stack.top())
    print("Current min after pop:", stack.get_min())


if __name__ == "__main__":
    main()
