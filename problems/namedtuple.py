"""namedtuple.py

Problem Statement:
Implement a Python module that demonstrates `namedtuple` usage for creating
lightweight, immutable records with named fields.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: namedtuple, tuple-like records, immutability, field access,
structured data modeling, readability
Real-world Use Case: Defining schema-like records for log entries,
configuration records, lightweight DTOs, and structured intermediate data
during ingestion pipelines.
Input Description: Functions accept field values, lists of records, and
optional transformation inputs.
Output Description: The module returns `namedtuple` instances, transformed
copies, and aggregated data derived from record fields.
Example Inputs and Outputs:
    create_person("Alice", 30) -> Person(name='Alice', age=30)
    average_age([person1, person2]) -> 27.5
    promote_to_manager(person) -> updated Person with role='manager'
Constraints: Use `namedtuple` for simple immutable records, avoid excessive
complexity, and keep functions focused on record creation and transformation.
Brute Force Approach: Use dictionaries or plain tuples with positional access.
Optimized Approach: Use `namedtuple` for readable field access and lightweight
record definitions.
Time Complexity: O(n) for collection operations, O(1) for single record creation.
Space Complexity: O(n) for collections of records.
Step-by-step Dry Run:
    person = create_person("Alice", 30)
    return Person(name='Alice', age=30)
Edge Cases: empty strings, missing optional fields, duplicate records, and
attempts to mutate immutable fields.
Common Mistakes: treating `namedtuple` as a mutable object and relying on
positional access over named fields.
Follow-up Interview Questions:
    1. How is `namedtuple` different from a `dataclass`?
    2. When would you choose `namedtuple` over a dictionary?
    3. How do you replace a field value in a `namedtuple`?
Alternative Approaches: Use `dataclasses` for richer behavior, plain classes
for methods, or dictionaries for dynamic records.
Expected Output: The script prints structured `namedtuple` instances and
collection summaries for record lists.
Key Takeaways: `namedtuple` provides immutable, readable records for simple
data models.
"""

from __future__ import annotations

from collections import namedtuple
from typing import List

Person = namedtuple("Person", ["name", "age", "role"])


def create_person(name: str, age: int, role: str = "developer") -> Person:
    """Create a new Person namedtuple instance."""
    return Person(name=name, age=age, role=role)


def promote_to_manager(person: Person) -> Person:
    """Return a new Person instance with the role updated to manager."""
    return person._replace(role="manager")


def average_age(people: List[Person]) -> float:
    """Compute the average age of a list of Person records."""
    if not people:
        return 0.0
    total_age = sum(person.age for person in people)
    return total_age / len(people)


def filter_by_role(people: List[Person], role: str) -> List[Person]:
    """Return all Person records matching the specified role."""
    return [person for person in people if person.role == role]


def main() -> None:
    """Main function demonstrating namedtuple usage."""
    alice = create_person("Alice", 30)
    bob = create_person("Bob", 25, role="tester")
    alice_manager = promote_to_manager(alice)
    people = [alice, bob, alice_manager]
    avg_age = average_age(people)
    developers = filter_by_role(people, "developer")

    print("Person example:", alice)
    print("Promoted manager:", alice_manager)
    print("Average age:", avg_age)
    print("Developer roles:", developers)


if __name__ == "__main__":
    main()
