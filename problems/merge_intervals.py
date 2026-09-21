"""merge_intervals.py

Problem Statement:
Implement a Python module that merges overlapping intervals into consolidated
intervals.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: sorting, interval merging, greedy algorithms,
edge-case handling
Real-world Use Case: Calendar scheduling, timeline consolidation, booking
systems, and range merging.
Input Description: Functions accept a list of interval pairs [start, end].
Output Description: Functions return a list of merged intervals.
Example Inputs and Outputs:
    merge_intervals([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]
Constraints: Handle sorting and overlapping interval detection.
Brute Force Approach: Compare every interval pair for overlap.
Optimized Approach: Sort intervals by start time and merge in one pass.
Time Complexity: O(n log n)
Space Complexity: O(n)
Step-by-step Dry Run:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    return [[1,6],[8,10],[15,18]]
Edge Cases: empty interval list, single interval, fully nested intervals, and
adjacent intervals.
Common Mistakes: not sorting by start time, merging non-overlapping intervals,
and failing to update the active interval correctly.
Follow-up Interview Questions:
    1. How do you handle intervals with identical start times?
    2. What if intervals are open-ended?
    3. Can this be used with k meeting rooms?
Alternative Approaches: Use a sweep line with event sorting or segment
trees for advanced interval queries.
Expected Output: The script prints merged interval lists for sample inputs.
Key Takeaways: Sort and merge in one linear pass yields an efficient solution.
"""

from __future__ import annotations

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals and return the consolidated list."""
    if not intervals:
        return []

    intervals.sort(key=lambda interval: interval[0])
    merged: List[List[int]] = [intervals[0][:]]

    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current[:])

    return merged


def main() -> None:
    """Main function demonstrating interval merging."""
    examples = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[6, 8], [1, 9], [2, 4], [4, 7]],
    ]
    for intervals in examples:
        print(intervals, "->", merge_intervals(intervals))


if __name__ == "__main__":
    main()
