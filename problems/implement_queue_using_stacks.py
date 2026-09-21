"""implement_queue_using_stacks.py

Problem Statement:
Implement a queue using two stacks.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google
Concepts Tested: amortized analysis, stack simulation.
Real-world Use Case: using stack-based APIs to build queue semantics.
Input Description: push, pop, peek, and empty operations.
Output Description: Queue behavior using stack operations.
Example Inputs and Outputs:
    push(1), push(2), peek() -> 1, pop() -> 1.
"""

from __future__ import annotations

from collections import deque


class MyQueue:
    def __init__(self) -> None:
        self.input_stack: deque[int] = deque()
        self.output_stack: deque[int] = deque()

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def _move(self) -> None:
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        if not self.output_stack:
            self._move()
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            self._move()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


def main() -> None:
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())


if __name__ == "__main__":
    main()
