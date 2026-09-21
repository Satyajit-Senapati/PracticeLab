"""garbage_collection.py

Problem Statement:
Implement a Python module that demonstrates garbage collection concepts,
including how cyclic references are detected and collected by Python's GC.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: garbage collection, cyclic references, gc module,
object lifecycle, memory cleanup, reference cycles
Real-world Use Case: Debugging memory issues in long-lived applications,
understanding cleanup of cyclic data structures, and using the garbage
collector to identify leaks.
Input Description: Functions create objects with cycles, trigger GC, and
report collection results.
Output Description: The module returns boolean indicators of whether cycles
were collected and demonstrates garbage collection behavior.
Example Inputs and Outputs:
    collect_cycles() -> True
    disable_enable_gc() -> (True, True)
Constraints: Use the `gc` module responsibly, avoid relying on exact reference
counts, and explain the behavior of the Python garbage collector.
Brute Force Approach: Ignore cyclic reference behavior and assume all objects
are freed immediately.
Optimized Approach: Use the GC module to identify and collect cycles in a
managed way.
Time Complexity: O(n) to traverse object references during collection.
Space Complexity: O(n) for tracked object graphs.
Step-by-step Dry Run:
    class Node: ...
    node1.next = node2; node2.next = node1
    gc.collect()
    return True if collected
Edge Cases: disabled GC, objects with __del__ methods, and reference cycles
that are not collectible.
Common Mistakes: ignoring the effect of `__del__`, expecting deterministic
collection timing, and relying on reference counts alone.
Follow-up Interview Questions:
    1. How does Python's garbage collector interact with reference counting?
    2. What are unreachable objects?
    3. How do objects with finalizers affect collection?
Alternative Approaches: Use weak references to avoid cycles, manual cleanup,
or object pools.
Expected Output: The script prints GC collection results and cycle detection
examples.
Key Takeaways: Python's GC handles cyclic references, but developers should
understand its non-deterministic behavior and interactions with finalizers.
"""

from __future__ import annotations

import gc
from typing import Any, Tuple


def collect_cycles() -> bool:
    """Create a cyclic reference and report whether gc collects it."""

    class Node:
        def __init__(self) -> None:
            self.other: Any = None

    first = Node()
    second = Node()
    first.other = second
    second.other = first

    del first, second
    collected = gc.collect()
    return collected > 0


def disable_enable_gc() -> Tuple[bool, bool]:
    """Temporarily disable and re-enable the garbage collector."""
    original_state = gc.isenabled()
    gc.disable()
    disabled_state = not gc.isenabled()
    gc.enable()
    enabled_state = gc.isenabled()
    if not original_state:
        gc.disable()
    return disabled_state, enabled_state


def main() -> None:
    """Main function demonstrating garbage collection behavior."""
    cycle_collected = collect_cycles()
    disabled_state, enabled_state = disable_enable_gc()

    print("Cycle collected by GC:", cycle_collected)
    print("GC disabled state:", disabled_state)
    print("GC enabled state:", enabled_state)


if __name__ == "__main__":
    main()
