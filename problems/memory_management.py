"""memory_management.py

Problem Statement:
Implement a Python module that demonstrates memory management concepts,
including object references, reference counts, and weak references where
appropriate.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: memory management, references, garbage collection,
reference counting, weakref, memory leaks, object lifecycle
Real-world Use Case: Avoiding memory leaks in long-running services, managing
cache lifecycles, and understanding object retention in data pipelines.
Input Description: Functions accept objects, sequences, and optional callbacks
for weak reference behavior.
Output Description: The module returns diagnostic values, demonstrates weak
reference lifetimes, and explains object retention.
Example Inputs and Outputs:
    strong_reference_demo() -> object stays alive
    weak_reference_demo() -> object collected after deletion
    cycle_detection_demo() -> True
Constraints: Use weak references for cache-like relationships, avoid relying on
implementation-specific reference counts, and explain behaviors clearly.
Brute Force Approach: Ignore memory retention issues and rely on normal
reference semantics.
Optimized Approach: Use weakref for optional references and explicit
reference management for long-lived objects.
Time Complexity: O(1) for reference operations.
Space Complexity: O(1) for examples and object references.
Step-by-step Dry Run:
    class WeakList(list): pass
    obj = WeakList([1, 2, 3])
    ref = weakref.ref(obj)
    del obj
    return ref() is None
Edge Cases: objects that do not support weak references, using weak refs for
critical references, and unexpected object lifetimes.
Common Mistakes: assuming weak references preserve objects, depending on
reference count values, and forgetting to break cycles for cleanup.
Follow-up Interview Questions:
    1. How does Python's garbage collector work?
    2. When should you use weak references?
    3. What causes memory leaks in Python?
Alternative Approaches: Use context managers for resource cleanup, explicit
cache eviction policies, or object pools.
Expected Output: The script prints memory management example results and
explains weak reference behavior.
Key Takeaways: Understanding references and garbage collection helps prevent
memory leaks and makes long-running code more robust.
"""

from __future__ import annotations

import gc
import weakref
from typing import Any, Optional


def strong_reference_demo() -> bool:
    """Demonstrate that objects remain alive while strong references exist."""
    data = [1, 2, 3]
    alias = data
    return alias is data


def weak_reference_demo() -> bool:
    """Demonstrate weak reference behavior when the original object is deleted."""
    class WeakList(list):
        """Unlike a plain list, this subclass supports weak references."""

    data = WeakList([1, 2, 3])
    reference = weakref.ref(data)
    assert reference() is data
    del data
    gc.collect()
    return reference() is None


def cycle_detection_demo() -> bool:
    """Demonstrate that cyclic references can be collected by the GC."""
    class Node:
        def __init__(self) -> None:
            self.next: Optional[Node] = None

    first = Node()
    second = Node()
    first.next = second
    second.next = first
    ref = weakref.ref(first)
    del first, second
    collected = gc.collect()
    return ref() is None and collected > 0


def main() -> None:
    """Main function demonstrating memory management examples."""
    strong_demo = strong_reference_demo()
    weak_demo = weak_reference_demo()
    cycle_demo = cycle_detection_demo()

    print("Strong reference demo:", strong_demo)
    print("Weak reference demo:", weak_demo)
    print("Cycle detection demo:", cycle_demo)


if __name__ == "__main__":
    main()
