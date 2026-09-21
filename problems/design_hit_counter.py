"""design_hit_counter.py

Problem Statement:
Design a hit counter that counts hits received in the last 5 minutes.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft
Concepts Tested: queue, time-based sliding window, amortized complexity.
Real-world Use Case: rate limiting and traffic monitoring.
Input Description: timestamped hit events.
Output Description: Number of hits in the past 300 seconds.
Example Inputs and Outputs:
    hits at 1,2,3 -> count at 4 = 3

Constraints: Timestamps are non-decreasing.
Time Complexity: O(1) amortized per operation.
Space Complexity: O(k) where k is number of hits in 5 minutes.
"""

from __future__ import annotations

from collections import deque


class HitCounter:
    def __init__(self) -> None:
        self.hits: deque[int] = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


def main() -> None:
    counter = HitCounter()
    events = [(1, None), (2, None), (3, None), (4, 4), (301, 301)]
    for timestamp, query in events:
        if query is None:
            counter.hit(timestamp)
            print(f"hit at {timestamp}")
        else:
            print(f"get_hits at {timestamp} -> {counter.get_hits(timestamp)}")


if __name__ == "__main__":
    main()
