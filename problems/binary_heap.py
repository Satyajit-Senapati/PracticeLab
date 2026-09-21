"""binary_heap.py

Problem Statement:
Implement a Python module that demonstrates a min-heap and max-heap using
heapq and custom wrappers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: heap operations, priority queues, comparisons, heap
invariants
Real-world Use Case: Task scheduling, priority queues, graph search, and
streaming median calculations.
Input Description: Functions accept values to push and pop from heaps.
Output Description: The module exposes wrapper functions for min-heap and
max-heap operations.
Example Inputs and Outputs:
    push values to min heap -> smallest value at root
    push values to max heap -> largest value at root
Constraints: Use O(log n) insertion and removal.
Brute Force Approach: Use sorting for each retrieval.
Optimized Approach: Use heap operations to maintain an efficient priority
queue.
Time Complexity: O(log n) per heap operation
Space Complexity: O(n)
Step-by-step Dry Run:
    push values, peek root, pop values in correct order
    return heap ordered sequence
Edge Cases: empty heap operations, duplicate values, and negative numbers.
Common Mistakes: confusing min-heap and max-heap semantics, pushing raw
values for max heap without transformation.
Follow-up Interview Questions:
    1. How can you implement a max-heap in Python with heapq?
    2. What is the difference between heap push and pop times?
    3. How do heaps compare to balanced binary search trees?
Alternative Approaches: Use bisect to maintain a sorted list, but with higher
cost.
Expected Output: The script prints sequences popped from min and max heaps.
Key Takeaways: Python's heapq is a min-heap implementation, and max-heaps can be built using value negation.
"""

from __future__ import annotations

import heapq
from typing import List


def min_heap_operations(values: List[int]) -> List[int]:
    """Return sorted values popped from a min-heap."""
    heap: List[int] = []
    for value in values:
        heapq.heappush(heap, value)

    result: List[int] = []
    while heap:
        result.append(heapq.heappop(heap))
    return result


def max_heap_operations(values: List[int]) -> List[int]:
    """Return sorted values popped from a max-heap implemented by negation."""
    heap: List[int] = []
    for value in values:
        heapq.heappush(heap, -value)

    result: List[int] = []
    while heap:
        result.append(-heapq.heappop(heap))
    return result


def main() -> None:
    """Main function demonstrating heap operations."""
    values = [5, 1, 3, 8, 2]
    print("Min-heap pop order:", min_heap_operations(values))
    print("Max-heap pop order:", max_heap_operations(values))


if __name__ == "__main__":
    main()
