"""magic_methods.py

Problem Statement:
Implement a Python module that demonstrates common magic methods and operator
overloading for a custom vector-like data structure.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: magic methods, __init__, __repr__, __add__, __len__,
__iter__, __getitem__, operator overloading, custom object behavior
Real-world Use Case: Building numeric vector types, domain-specific data
structures, and custom collection objects that behave like built-in types.
Input Description: Functions accept vector values, scalar values, and sequence
inputs for basic operations.
Output Description: The module returns vector instances, combined results, and
iterable behaviors provided by magic methods.
Example Inputs and Outputs:
    v1 + v2 -> Vector([3, 5, 7])
    len(v1) -> 3
    list(v1) -> [1, 2, 3]
Constraints: Use magic methods safely, preserve immutability where appropriate,
and support standard container behaviors.
Brute Force Approach: Use plain functions on lists without custom object methods.
Optimized Approach: Implement rich comparison and container protocol methods
for vector usability.
Time Complexity: O(n) for vector operations.
Space Complexity: O(n) for output vector copies.
Step-by-step Dry Run:
    v1 = Vector([1, 2, 3])
    v2 = Vector([2, 3, 4])
    combined = v1 + v2
    return Vector([3, 5, 7])
Edge Cases: vectors of different lengths, non-numeric values, indexing errors,
and unsupported operations.
Common Mistakes: returning non-Vector values from __add__, failing to handle
invalid indices, and not raising appropriate exceptions.
Follow-up Interview Questions:
    1. What is the purpose of __repr__ vs __str__?
    2. How does Python dispatch operator overloading?
    3. When should you implement __iter__ on a custom type?
Alternative Approaches: Use composition around built-in lists, namedtuple with
methods, or NumPy arrays for numeric vector operations.
Expected Output: The script prints vector operations, iteration results, and
indexing behavior.
Key Takeaways: Magic methods enable custom objects to integrate naturally with
Python syntax and built-in operations.
"""

from __future__ import annotations

from typing import Iterable, Iterator, List


class Vector:
    """A simple vector class demonstrating magic methods."""

    def __init__(self, values: Iterable[float]) -> None:
        self._values: List[float] = list(values)

    def __repr__(self) -> str:
        return f"Vector({self._values})"

    def __len__(self) -> int:
        return len(self._values)

    def __iter__(self) -> Iterator[float]:
        return iter(self._values)

    def __getitem__(self, index: int) -> float:
        return self._values[index]

    def __add__(self, other: Vector) -> Vector:
        if len(self) != len(other):
            raise ValueError("Vectors must have equal length for addition")
        return Vector(a + b for a, b in zip(self._values, other._values))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self._values == other._values

    def dot(self, other: Vector) -> float:
        if len(self) != len(other):
            raise ValueError("Vectors must have equal length for dot product")
        return sum(a * b for a, b in zip(self._values, other._values))


def main() -> None:
    """Main function demonstrating vector magic methods."""
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([2.0, 3.0, 4.0])
    combined = v1 + v2
    length = len(v1)
    items = list(v1)
    dot_product = v1.dot(v2)
    equal_check = combined == Vector([3.0, 5.0, 7.0])

    print("Vector v1:", v1)
    print("Combined vector:", combined)
    print("Vector length:", length)
    print("Vector items:", items)
    print("Dot product:", dot_product)
    print("Equality check:", equal_check)


if __name__ == "__main__":
    main()
