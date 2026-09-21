"""protocols.py

Problem Statement:
Implement a Python module that demonstrates structural subtyping using
Protocols, including defining protocol interfaces and supporting duck typing
with static typing.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: typing.Protocol, structural typing, duck typing,
abstract requirements, static type hints
Real-world Use Case: Defining flexible pipeline components, supporting multiple
implementations of processing contracts, and enabling integration of external
libraries with a shared interface.
Input Description: Functions accept protocol-compliant objects and lists of
items implementing required methods.
Output Description: The module returns values produced by protocol-aware
functions and demonstrates type-safe reuse of diverse objects.
Example Inputs and Outputs:
    process(printer, "hello") -> "Printed: hello"
    total = compute_area([circle, square]) -> 50.27
Constraints: Use Protocols to define shared behavior without inheritance, keep
protocol definitions minimal, and avoid concrete implementation coupling.
Brute Force Approach: Use base classes or explicit type checks.
Optimized Approach: Use Protocols to express expected behavior while enabling
duck typing.
Time Complexity: O(n) for processing sequences.
Space Complexity: O(n) for result collections.
Step-by-step Dry Run:
    printer = ConsolePrinter()
    result = process(printer, "text")
    return "Printed: text"
Edge Cases: objects missing required protocol methods, incompatible types,
multiple implementations, and generic protocol use.
Common Mistakes: relying on runtime type checks, failing to define accurate
protocol methods, and confusing Protocols with ABCs.
Follow-up Interview Questions:
    1. How do Protocols differ from abstract base classes?
    2. When should you use Protocols in a Python codebase?
    3. Can Protocols be used with runtime checks?
Alternative Approaches: Use ABCs for concrete inheritance hierarchies, interfaces
via duck typing without static typing, or explicit type checks with isinstance.
Expected Output: The script prints results from objects that fulfill protocol
contracts and demonstrates protocol-based composition.
Key Takeaways: Protocols enable flexible, type-safe interfaces without tight
inheritance coupling.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable, Sequence


class Printable(Protocol):
    """Protocol representing an object that can print a message."""

    def print(self, message: str) -> str:
        ...


class Shape(Protocol):
    """Protocol representing an object that can compute its area."""

    def area(self) -> float:
        ...


class ConsolePrinter:
    """A simple printer implementation for the Printable protocol."""

    def print(self, message: str) -> str:
        result = f"Printed: {message}"
        print(result)
        return result


class Circle:
    """A circle implementation of the Shape protocol."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Square:
    """A square implementation of the Shape protocol."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side


def process(printer: Printable, message: str) -> str:
    """Process a message with a protocol-compliant printer."""
    return printer.print(message)


def compute_total_area(shapes: Sequence[Shape]) -> float:
    """Compute the total area of a sequence of Shape objects."""
    return sum(shape.area() for shape in shapes)


def main() -> None:
    """Main function demonstrating Protocol usage."""
    printer = ConsolePrinter()
    printed_text = process(printer, "hello world")
    shapes = [Circle(radius=2.0), Square(side=4.0)]
    total_area = compute_total_area(shapes)

    print("Printed text result:", printed_text)
    print("Total shape area:", total_area)


if __name__ == "__main__":
    main()
