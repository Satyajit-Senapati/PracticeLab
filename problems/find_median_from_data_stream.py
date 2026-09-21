"""find_median_from_data_stream.py

Problem Statement:
Design a data structure that supports inserting numbers and finding the median efficiently.

Interview Difficulty: Hard
Commonly Asked By: Google, Facebook, Microsoft
Concepts Tested: heaps, balancing, order statistics.
Real-world Use Case: dynamic median tracking in metrics and analytics.
Input Description: Stream of integers.
Output Description: The median of all numbers inserted so far.
Example Inputs and Outputs:
    insert(1), insert(2), findMedian() -> 1.5.
Constraints: Use O(log n) insertion and O(1) median query.
Time Complexity: O(log n) per insert
Space Complexity: O(n)
"""

from __future__ import annotations

import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.low: list[int] = []  # max heap via negatives
        self.high: list[int] = []  # min heap

    def add_num(self, num: int) -> None:
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)

        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


def main() -> None:
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    print(finder.find_median())
    finder.add_num(3)
    print(finder.find_median())


if __name__ == "__main__":
    main()
