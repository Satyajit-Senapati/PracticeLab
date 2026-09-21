"""insert_interval.py

Problem Statement:
Insert a new interval into a list of non-overlapping sorted intervals,
merging if necessary.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: interval merging, sorting, edge case handling.
Real-world Use Case: scheduling, calendar event insertion.
Input Description: A list of sorted non-overlapping intervals and a new interval.
Output Description: The updated merged interval list.
Example Inputs and Outputs:
    intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]]
Constraints: Input intervals are sorted by start time.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """Insert and merge the new interval into the existing interval list."""
    result: list[list[int]] = []
    i = 0
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


def main() -> None:
    print(insert_interval([[1, 3], [6, 9]], [2, 5]))
    print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


if __name__ == "__main__":
    main()
