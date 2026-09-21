"""hashmap_implementation.py

Problem Statement:
Implement a Python module that demonstrates a basic hash map implementation
using separate chaining for collision handling.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hash tables, collision resolution, separate chaining,
load factor, complexity analysis
Real-world Use Case: Understanding underlying dictionary mechanics, building
custom caches, and applying hash-based indexing for data retrieval.
Input Description: Functions accept keys and values for insertion, retrieval,
and deletion.
Output Description: The module exposes a HashMap class with common operations.
Example Inputs and Outputs:
    hashmap.put("a", 1); hashmap.get("a") -> 1
    hashmap.remove("a") -> None; hashmap.get("a") -> None
Constraints: Implement O(1) average time for get/put/remove and handle hash
collisions.
Brute Force Approach: Use a list of key-value pairs and scan linearly.
Optimized Approach: Use an array of buckets with linked lists for collisions.
Time Complexity: O(1) average for insertions and lookups.
Space Complexity: O(n)
Step-by-step Dry Run:
    map = HashMap()
    map.put("a", 1)
    return map.get("a") == 1
Edge Cases: updating existing keys, non-existent keys, and collision handling.
Common Mistakes: not handling collisions, failing to resize, and ignoring
hash value distribution.
Follow-up Interview Questions:
    1. What is a hash collision and how do you handle it?
    2. Why are hash maps average O(1) but worst-case O(n)?
    3. How would you implement resizing?
Alternative Approaches: Use open addressing, linear probing, or built-in
Python dictionaries for production.
Expected Output: The script prints sample HashMap operations and results.
Key Takeaways: Separate chaining provides a simple, effective collision
resolution strategy in hash maps.
"""

from __future__ import annotations

from typing import Any, List, Optional, Tuple


class HashMap:
    """A simple hash map implementation using separate chaining."""

    def __init__(self, capacity: int = 16) -> None:
        self._capacity = capacity
        self._buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacity)]

    def _bucket_index(self, key: Any) -> int:
        return hash(key) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        bucket_index = self._bucket_index(key)
        bucket = self._buckets[bucket_index]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: Any) -> Optional[Any]:
        bucket_index = self._bucket_index(key)
        bucket = self._buckets[bucket_index]
        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value
        return None

    def remove(self, key: Any) -> None:
        bucket_index = self._bucket_index(key)
        bucket = self._buckets[bucket_index]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[index]
                return

    def __repr__(self) -> str:
        return f"HashMap({self._buckets})"


def main() -> None:
    """Main function demonstrating HashMap operations."""
    hashmap = HashMap()
    hashmap.put("a", 1)
    hashmap.put("b", 2)
    hashmap.put("a", 3)

    print("a ->", hashmap.get("a"))
    print("b ->", hashmap.get("b"))
    hashmap.remove("a")
    print("a after removal ->", hashmap.get("a"))
    print("HashMap internal state:", hashmap)


if __name__ == "__main__":
    main()
