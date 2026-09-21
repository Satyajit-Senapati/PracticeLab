"""randomized_set.py

Problem Statement:
Implement a Python module that supports insert, remove, and getRandom in average constant time.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hash tables, array indexing, random selection, amortized complexity
Real-world Use Case: Random sampling from a dynamic set, load balancing, caching, and gaming systems.
Input Description: Functions accept values to insert and remove, and provide random retrieval.
Output Description: Functions support O(1) insert, delete, and random access operations.
Example Inputs and Outputs:
    insert(1) -> True
    insert(2) -> True
    get_random() -> 1 or 2
Constraints: Use a hash map for indices and a list for values.
Brute Force Approach: Use a list with linear remove operations.
Optimized Approach: Maintain an array and dictionary to keep operations constant time.
Time Complexity: O(1) average per operation
Space Complexity: O(n)
Step-by-step Dry Run:
    insert 1, insert 2, remove 1, get random from [2]
    return 2
Edge Cases: duplicate inserts, removing absent values, and random access when empty.
Common Mistakes: not updating index map on swap, using list.remove() directly, and failing to keep O(1) time.
Follow-up Interview Questions:
    1. How would you return multiple random elements?
    2. What changes for weighted random selection?
    3. How does this compare to a basic set?
Alternative Approaches: Use ordered dictionaries with additional indexing, but with higher complexity.
Expected Output: The script prints sample operations on the randomized set.
Key Takeaways: Combining a list and dictionary gives average constant-time set operations with random access.
"""

from __future__ import annotations

import random
from typing import Dict, List, Optional


class RandomizedSet:
    """A set that supports insertion, deletion, and random access in average O(1)."""

    def __init__(self) -> None:
        self._values: List[int] = []
        self._index_map: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self._index_map:
            return False
        self._index_map[val] = len(self._values)
        self._values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._index_map:
            return False
        idx = self._index_map[val]
        last_val = self._values[-1]
        self._values[idx] = last_val
        self._index_map[last_val] = idx
        self._values.pop()
        del self._index_map[val]
        return True

    def get_random(self) -> Optional[int]:
        if not self._values:
            return None
        return random.choice(self._values)


def main() -> None:
    """Main function demonstrating RandomizedSet operations."""
    randomized_set = RandomizedSet()
    print("Insert 1:", randomized_set.insert(1))
    print("Insert 2:", randomized_set.insert(2))
    print("Remove 1:", randomized_set.remove(1))
    print("Random element:", randomized_set.get_random())


if __name__ == "__main__":
    main()
