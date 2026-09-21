"""context_manager.py

Problem Statement:
Implement a Python module that demonstrates context manager usage, including
built-in `with` statements, custom context manager classes, and generator-based
context managers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: context managers, resource management, __enter__, __exit__,
contextlib, exception handling, cleanup
Real-world Use Case: Managing file handles, database connections, locks,
network resources, and transactional operations in data engineering pipelines.
Input Description: Functions accept file paths, simulated resource names, and
configuration options for context manager behavior.
Output Description: The functions and classes demonstrate resource acquisition,
cleanup, and exception-aware context handling.
Example Inputs and Outputs:
    read_file_contents("example.txt") -> file contents string
    with ManagedResource("cache") as resource: ... -> resource opened/closed
Constraints: Use context managers to manage resources safely, preserve cleanup
even on exceptions, and prefer generator-based context managers for simple
scenarios.
Brute Force Approach: Explicitly call open and close methods without `with`.
Optimized Approach: Use context managers to encapsulate resource acquisition
and cleanup.
Time Complexity: O(n) for reading file contents, O(1) for acquiring and
releasing resources.
Space Complexity: O(n) for file contents when loaded into memory.
Step-by-step Dry Run:
    with open_file("example.txt") as file: content = file.read()
    return content
Edge Cases: exceptions inside the context, nested contexts, failing resource
acquisition, and ensuring cleanup always occurs.
Common Mistakes: forgetting to close resources, using `with` incorrectly, and
raising exceptions inside __exit__.
Follow-up Interview Questions:
    1. How does __exit__ handle exceptions?
    2. When would you use contextlib.contextmanager instead of a class?
    3. What resources are best managed with context managers?
Alternative Approaches: Use explicit `try/finally` blocks or helper functions
for simpler cleanup.
Expected Output: The script prints sample resource manager usage and confirms
cleanup behavior for normal and exceptional cases.
Key Takeaways: Context managers provide a reliable pattern for resource
management and cleanup in Python programs.
"""

from __future__ import annotations

import contextlib
from pathlib import Path
from typing import Generator, Iterator


def read_file_contents(file_path: str) -> str:
    """Read the contents of a file using a built-in context manager."""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        return handle.read()


class ManagedResource:
    """Custom context manager that simulates resource acquisition and cleanup."""

    def __init__(self, resource_name: str) -> None:
        self.resource_name = resource_name
        self.is_open = False

    def __enter__(self) -> ManagedResource:
        print(f"Acquiring resource: {self.resource_name}")
        self.is_open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        print(f"Releasing resource: {self.resource_name}")
        self.is_open = False
        return False


@contextlib.contextmanager
def simple_resource(resource_name: str) -> Generator[ManagedResource, None, None]:
    """Generator-based context manager for a simple managed resource."""
    resource = ManagedResource(resource_name)
    try:
        yield resource
    finally:
        resource.is_open = False
        print(f"Cleaning up resource: {resource_name}")


def main() -> None:
    """Main function demonstrating context manager usage."""
    try:
        sample_path = "sample.txt"
        Path(sample_path).write_text("Hello, context managers!", encoding="utf-8")
        contents = read_file_contents(sample_path)
        print("File contents:", contents)
    finally:
        Path(sample_path).unlink(missing_ok=True)

    with ManagedResource("cache") as manager:
        print("Inside managed resource", manager.is_open)

    with simple_resource("database") as resource:
        print("Inside simple resource", resource.is_open)


if __name__ == "__main__":
    main()
