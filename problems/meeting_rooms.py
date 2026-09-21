"""meeting_rooms.py

Problem Statement:
Implement a Python module that determines the minimum number of meeting rooms
required to schedule all meetings without conflicts.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: interval scheduling, sorting, min-heaps, greedy algorithms,
resource allocation
Real-world Use Case: Booking systems, conference room scheduling, and
calendar overlap analysis.
Input Description: Functions accept a list of meeting intervals [start, end].
Output Description: Functions return the minimum number of rooms required.
Example Inputs and Outputs:
    min_meeting_rooms([[0, 30],[5, 10],[15, 20]]) -> 2
Constraints: Use O(n log n) time and O(n) space. Manage overlaps by tracking
current active meetings.
Brute Force Approach: Compare every interval with every other interval.
Optimized Approach: Sort by start time and use a min-heap to track end times.
Time Complexity: O(n log n)
Space Complexity: O(n)
Step-by-step Dry Run:
    intervals = [[0, 30], [5, 10], [15, 20]]
    active rooms = 2
    return 2
Edge Cases: empty list, all meetings disjoint, and completely overlapping
meetings.
Common Mistakes: forgetting to free rooms when meetings end, using start
instead of end times for heap operations, and not sorting intervals.
Follow-up Interview Questions:
    1. How would you schedule the maximum number of meetings in one room?
    2. Can this be solved using two pointers alone?
    3. How do you adapt this for meeting durations with priorities?
Alternative Approaches: Use separate sorted start and end arrays with two
pointers instead of a heap.
Expected Output: The script prints required room counts for sample schedules.
Key Takeaways: Track meeting end times to reuse rooms efficiently.
"""

from __future__ import annotations

import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Return the minimum number of meeting rooms required."""
    if not intervals:
        return 0

    intervals.sort(key=lambda interval: interval[0])
    min_heap: List[int] = []

    for start, end in intervals:
        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)

    return len(min_heap)


def main() -> None:
    """Main function demonstrating meeting room scheduling."""
    examples = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]],
        [[0, 5], [5, 10], [10, 15]],
    ]
    for intervals in examples:
        print(intervals, "->", min_meeting_rooms(intervals))


if __name__ == "__main__":
    main()
