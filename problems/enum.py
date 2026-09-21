"""enum.py

Problem Statement:
Implement a Python module that demonstrates `Enum` usage for defining named
constant values and improving code readability through enumerated types.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: Enum, auto(), member access, comparison, mapping, type
safety, semantics
Real-world Use Case: Defining status codes, event types, configuration
options, and domain states in data pipelines or service applications.
Input Description: Functions accept enum members, raw strings, and numeric
status inputs.
Output Description: The module returns enum values, mapped labels, and lists
filtered by enum membership.
Example Inputs and Outputs:
    get_status_label(Status.ACTIVE) -> "Active"
    group_by_status(items) -> {'active': [...], 'inactive': [...]} 
    is_valid_status("active") -> True
Constraints: Use Enum for semantic constants, preserve immutability, and avoid
magic strings in business logic.
Brute Force Approach: Use raw strings or integer constants for status values.
Optimized Approach: Use Enum members to enforce valid states and improve
readability.
Time Complexity: O(n) for collection filtering and grouping.
Space Complexity: O(n) for output collections.
Step-by-step Dry Run:
    label = get_status_label(Status.PENDING)
    return "Pending"
Edge Cases: invalid values, string case sensitivity, duplicate mappings, and
comparison between different enum classes.
Common Mistakes: comparing enum members to raw values, using mutable class
attributes, and ignoring `auto()` for sequential values.
Follow-up Interview Questions:
    1. What is the difference between Enum and IntEnum?
    2. When should you use Enum instead of constants?
    3. How can you add methods to an Enum class?
Alternative Approaches: Use constant classes, dictionaries, or dataclasses for
more structured data.
Expected Output: The script prints enum labels, validation results, and
grouped items by enum status.
Key Takeaways: Enum provides a safe, readable way to model fixed domains and
reduce errors from raw literals.
"""

from __future__ import annotations

from enum import Enum, auto
from typing import Dict, Iterable, List


class Status(Enum):
    """Enumeration representing a record status."""

    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()
    FAILED = auto()


def get_status_label(status: Status) -> str:
    """Return a human-readable label for the given status."""
    return {
        Status.ACTIVE: "Active",
        Status.INACTIVE: "Inactive",
        Status.PENDING: "Pending",
        Status.FAILED: "Failed",
    }.get(status, "Unknown")


def is_valid_status(value: str) -> bool:
    """Return whether the string corresponds to a valid status."""
    try:
        Status[value.upper()]
        return True
    except KeyError:
        return False


def group_by_status(items: Iterable[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """Group items by their string status value."""
    grouped: Dict[str, List[Dict[str, str]]] = {
        "active": [],
        "inactive": [],
        "pending": [],
        "failed": [],
    }
    for item in items:
        status = item.get("status", "unknown").lower()
        if status in grouped:
            grouped[status].append(item)
    return grouped


def main() -> None:
    """Main function demonstrating enum usage."""
    label = get_status_label(Status.PENDING)
    valid_status = is_valid_status("active")
    invalid_status = is_valid_status("unknown")
    grouped = group_by_status([
        {"id": "1", "status": "active"},
        {"id": "2", "status": "pending"},
        {"id": "3", "status": "failed"},
    ])

    print("Status label:", label)
    print("Valid status (active):", valid_status)
    print("Valid status (unknown):", invalid_status)
    print("Grouped items by status:", grouped)


if __name__ == "__main__":
    main()
