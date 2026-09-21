"""descriptors.py

Problem Statement:
Implement a Python module that demonstrates descriptor usage for managing
attribute access, validation, and computed properties in reusable classes.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: descriptors, __get__, __set__, __delete__, attribute access,
validation, reusable property logic
Real-world Use Case: Implementing validated model fields, lazy properties,
cached attributes, and reusable behavior across domain objects.
Input Description: Classes accept field values and use descriptors for validation
and caching.
Output Description: The module returns objects with controlled attribute
behavior and demonstrates descriptor-managed assignment and retrieval.
Example Inputs and Outputs:
    user = User(username="alice", age=30)
    user.age = 31 -> valid assignment
    product.tax_rate -> computed value
Constraints: Use descriptors to encapsulate attribute logic, preserve
separation of concerns, and avoid per-class duplication of validation code.
Brute Force Approach: Implement validation in every setter method manually.
Optimized Approach: Reuse descriptor classes to centralize attribute logic.
Time Complexity: O(1) for descriptor get/set operations.
Space Complexity: O(1) for attribute storage, plus any cached values.
Step-by-step Dry Run:
    user = User(username="alice", age=30)
    user.age = 31
    return 31
Edge Cases: invalid assignments, missing attributes, and descriptor sharing
across classes.
Common Mistakes: using descriptors with mutable default values and not
handling attribute storage correctly.
Follow-up Interview Questions:
    1. How do descriptors differ from properties?
    2. What is the purpose of __get__, __set__, and __delete__?
    3. When should you implement a descriptor instead of a property?
Alternative Approaches: Use properties, dataclasses with validators, or
explicit setters in plain classes.
Expected Output: The script prints descriptor-driven validation and computed
property behavior.
Key Takeaways: Descriptors encapsulate attribute access logic and make it
reusable across classes.
"""

from __future__ import annotations

from typing import Any, Optional


class TypedAttribute:
    """Descriptor that validates the type of assigned values."""

    def __init__(self, name: str, expected_type: type) -> None:
        self.name = name
        self.expected_type = expected_type
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: type) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be of type {self.expected_type.__name__}")
        setattr(instance, self.storage_name, value)

    def __delete__(self, instance: Any) -> None:
        raise AttributeError(f"{self.name} cannot be deleted")


class PositiveInteger:
    """Descriptor that validates values are positive integers."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: type) -> int:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, 0)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.name} must be a positive integer")
        setattr(instance, self.storage_name, value)

    def __delete__(self, instance: Any) -> None:
        raise AttributeError(f"{self.name} cannot be deleted")


class User:
    """A user record using descriptors for typed and validated fields."""

    username = TypedAttribute("username", str)
    age = PositiveInteger("age")

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age


class Product:
    """A product record with a computed discount property."""

    price = TypedAttribute("price", float)
    discount_rate = TypedAttribute("discount_rate", float)

    def __init__(self, price: float, discount_rate: float) -> None:
        self.price = price
        self.discount_rate = discount_rate

    @property
    def discounted_price(self) -> float:
        return self.price * (1 - self.discount_rate)


def main() -> None:
    """Main function demonstrating descriptor behavior."""
    user = User(username="alice", age=30)
    try:
        user.age = 31
    except ValueError as error:
        print(error)

    product = Product(price=100.0, discount_rate=0.15)

    print("User username:", user.username)
    print("User age:", user.age)
    print("Discounted product price:", product.discounted_price)


if __name__ == "__main__":
    main()
