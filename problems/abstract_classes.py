"""abstract_classes.py

Problem Statement:
Implement a Python module that demonstrates abstract base classes (ABCs) for
defining shared interfaces and enforcing method implementations in subclasses.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: abstract base classes, abc module, method overriding,
inheritance, interface definition, polymorphism
Real-world Use Case: Defining service interfaces, data processing stages,
storage backends, and plugin architectures with guaranteed method contracts.
Input Description: Functions accept base class references, derived objects,
and optional configuration values.
Output Description: The module returns polymorphic results from subclass
implementations and demonstrates protected shared behavior.
Example Inputs and Outputs:
    process_data(CsvDataProcessor(), data) -> processed CSV string
    save_storage(FileStorage(), item) -> "saved"
Constraints: Use ABCs to require subclass methods, avoid instantiating abstract
base classes directly, and keep interface definitions focused.
Brute Force Approach: Use informal duck typing with no enforced interface.
Optimized Approach: Use ABCs to make contracts explicit and catch errors early.
Time Complexity: O(n) for processing collections.
Space Complexity: O(n) for output collections.
Step-by-step Dry Run:
    processor = JsonDataProcessor()
    result = processor.process({"key": "value"})
    return "{"key": "value"}"
Edge Cases: missing subclass implementations, invalid input, and abstract
methods not overridden.
Common Mistakes: forgetting to import ABC or abstractmethod, instantiating
abstract classes, and using ABCs for simple function-based contracts.
Follow-up Interview Questions:
    1. What is the difference between ABCs and Protocols?
    2. When should you use an abstract base class?
    3. Can abstract methods have default behavior?
Alternative Approaches: Use protocols for structural typing, plain classes
with documentation, or mixins for shared behavior.
Expected Output: The script prints results from abstract class implementations
and demonstrates polymorphic behavior.
Key Takeaways: Abstract classes provide explicit interfaces and enforce
implementation of required methods in subclasses.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class DataProcessor(ABC):
    """Abstract base class defining a data processing contract."""

    @abstractmethod
    def process(self, data: Dict[str, Any]) -> str:
        """Process input data and return a string result."""
        pass


class JsonDataProcessor(DataProcessor):
    """Processor implementation that serializes data to JSON-like output."""

    def process(self, data: Dict[str, Any]) -> str:
        return str(data)


class CsvDataProcessor(DataProcessor):
    """Processor implementation that serializes data to CSV-like output."""

    def process(self, data: Dict[str, Any]) -> str:
        return ",".join(str(value) for value in data.values())


class StorageBackend(ABC):
    """Abstract base class defining a storage contract."""

    @abstractmethod
    def save(self, item: str) -> str:
        """Save an item and return a status message."""
        pass


class FileStorage(StorageBackend):
    """Concrete storage implementation writing items to a file."""

    def save(self, item: str) -> str:
        return f"saved: {item}"


def process_data(processor: DataProcessor, data: Dict[str, Any]) -> str:
    """Process data using the provided abstract processor."""
    return processor.process(data)


def save_storage(storage: StorageBackend, item: str) -> str:
    """Save an item using the provided storage backend."""
    return storage.save(item)


def main() -> None:
    """Main function demonstrating abstract base class usage."""
    json_result = process_data(JsonDataProcessor(), {"name": "Alice", "age": 30})
    csv_result = process_data(CsvDataProcessor(), {"name": "Alice", "age": 30})
    saved_result = save_storage(FileStorage(), "report.txt")

    print("JSON-style result:", json_result)
    print("CSV-style result:", csv_result)
    print("Storage result:", saved_result)


if __name__ == "__main__":
    main()
