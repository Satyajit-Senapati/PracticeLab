"""meeting_rooms_ii.py

Problem Statement:
Implement a Python module that finds the minimum number of conference rooms required to schedule all meetings, where each meeting has a start and end time.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: interval scheduling, greedy algorithms, min-heaps, sorting
Real-world Use Case: Resource allocation, calendar scheduling, conference room management.
Input Description: Functions accept a list of meeting intervals [[start, end]].
Output Description: Functions return the minimum number of rooms required.
Example Inputs and Outputs:
    min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) -> 2
Constraints: Use O(n log n) time and O(n) space; manage overlapping intervals.
Brute Force Approach: Compare every meeting pair to detect conflicts.
Optimized Approach: Sort by start times and use a min-heap to track meeting end times.
Time Complexity: O(n log n)
Space Complexity: O(n)
Step-by-step Dry Run:
    intervals = [[0, 30], [5, 10], [15, 20]]
    active rooms = 2
    return 2
Edge Cases: empty list, no overlaps, and all meetings overlapping.
Common Mistakes: not reusing rooms when meetings end, sorting by wrong key, and forgetting to pop ended meetings from the heap.
Follow-up Interview Questions:
    1. How would you schedule the maximum number of non-overlapping meetings?
    2. What changes if meetings can share endpoints?
    3. Can you solve this without a heap?
Alternative Approaches: Sort start and end times separately and scan with two pointers.
Expected Output: The script prints required rooms for sample schedules.
Key Takeaways: Track the greedy minimum end time to reuse rooms optimally.
"""

from __future__ import annotations

import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Return the minimum number of meeting rooms required."""
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    min_heap: List[int] = []

    for start, end in intervals:
        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)

    return len(min_heap)


def main() -> None:
    """Main function demonstrating Meeting Rooms II scheduling."""
    examples = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]],
        [[1, 5], [8, 9], [8, 9]],
    ]
    for intervals in examples:
        print(intervals, "->", min_meeting_rooms(intervals))


if __name__ == "__main__":
    main()
