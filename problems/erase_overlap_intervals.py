"""erase_overlap_intervals.py

Problem Statement:
Given a list of intervals, determine the minimum number of intervals to remove so that the rest are non-overlapping.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: greedy algorithms, interval scheduling.
Real-world Use Case: optimizing event selection and resource allocation.
Input Description: A list of intervals.
Output Description: Minimum number of intervals to remove.
Example Inputs and Outputs:
    [[1,2],[2,3],[3,4],[1,3]] -> 1
Constraints: Keep the maximum number of non-overlapping intervals.
Time Complexity: O(n log n)
Space Complexity: O(1)
"""

from __future__ import annotations


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """Return the minimum number of intervals to remove to avoid overlap."""
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for start, finish in intervals[1:]:
        if start < end:
            count += 1
        else:
            end = finish
    return count


def main() -> None:
    print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))


if __name__ == "__main__":
    main()
