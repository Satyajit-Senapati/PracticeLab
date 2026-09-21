"""design_lru_cache.py

Problem Statement:
Implement a Python module that designs an LRU cache with get and put operations.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: linked hash map, doubly linked list, cache eviction,
O(1) operations
Real-world Use Case: In-memory caching for web servers, database query caching, and resource pooling.
Input Description: Class accepts a capacity and supports get(key) and put(key, value).
Output Description: Returns cached values or updates/inserts entries with eviction policy.
Example Inputs and Outputs:
    cache = LRUCache(2); cache.put(1,1); cache.put(2,2); cache.get(1) -> 1; cache.put(3,3) evicts 2.
Constraints: Both get and put should operate in O(1).
Brute Force Approach: Use dictionary and list, O(n) updates.
Optimized Approach: Use dictionary for lookup and doubly linked list for order.
Time Complexity: O(1) for get and put.
Space Complexity: O(capacity)
Step-by-step Dry Run:
    move accessed or updated nodes to head; evict tail when capacity exceeded.
Edge Cases: capacity = 0, updating existing keys.
Common Mistakes: forgetting to update access order or remove old tail.
Follow-up Interview Questions:
    1. How to make it thread-safe?
    2. Can you implement an LFU cache instead?
    3. What changes for variable-sized items?
Alternative Approaches: Use OrderedDict in Python.
Expected Output: The script demonstrates cache hits and evictions.
Key Takeaways: LRU caching requires fast lookup plus fast reordering.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    value: int
    prev: Optional["Node"] = None
    next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            tail = self.tail.prev
            if tail and tail is not self.head:
                self._remove(tail)
                del self.cache[tail.key]


def main() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("Get 1:", cache.get(1))
    cache.put(3, 3)
    print("Get 2:", cache.get(2))
    cache.put(4, 4)
    print("Get 1:", cache.get(1))
    print("Get 3:", cache.get(3))
    print("Get 4:", cache.get(4))


if __name__ == "__main__":
    main()
