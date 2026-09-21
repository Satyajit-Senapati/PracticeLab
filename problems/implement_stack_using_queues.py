"""implement_stack_using_queues.py

Problem Statement:
Implement a stack using two queues.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google
Concepts Tested: queue simulation, amortized operations.
Real-world Use Case: simulating stack operations where only queue APIs are available.
Input Description: push, pop, top, and empty operations.
Output Description: Stack behavior implemented with queues.
Example Inputs and Outputs:
    push(1), push(2), top() -> 2, pop() -> 2.
"""

from __future__ import annotations

from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


def main() -> None:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())


if __name__ == "__main__":
    main()
