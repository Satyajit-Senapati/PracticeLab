"""dataclasses.py

Problem Statement:
Implement a Python module that demonstrates `dataclasses`, including data
model definition, default values, immutability, and helper methods for clean
structured data handling.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dataclasses, type hints, immutability, default_factory,
structured data modeling, data validation, serialization
Real-world Use Case: Defining schema-like records for configuration, ETL
records, domain models, and intermediate data structures in pipelines.
Input Description: Functions accept primitive values and optional configuration
for dataclass instances.
Output Description: The module returns dataclass objects, transformed copies,
and aggregated collections of structured data.
Example Inputs and Outputs:
    create_user_profile("alice", "alice@example.com") -> UserProfile(...)
    update_status(profile, "active") -> updated profile with new status
    average_age([profile1, profile2]) -> 29.5
Constraints: Use dataclasses for structured data, preserve immutability where
appropriate, and keep model definitions clear and minimal.
Brute Force Approach: Use plain dictionaries or tuples for structured data.
Optimized Approach: Use dataclasses for readability, automatic method
generation, and consistent field definitions.
Time Complexity: O(n) for collection operations, O(1) for dataclass creation.
Space Complexity: O(n) for lists of data objects.
Step-by-step Dry Run:
    profile = create_user_profile("alice", "alice@example.com")
    return UserProfile(username='alice', email='alice@example.com', ...)
Edge Cases: missing values, default mutable fields, frozen dataclass mutation,
and non-hashable field types.
Common Mistakes: using mutable default values directly, forgetting type hints,
and not using `replace()` for immutable dataclass updates.
Follow-up Interview Questions:
    1. When would you use a dataclass versus a namedtuple?
    2. How does `field(default_factory=...)` avoid shared mutable state?
    3. What are the benefits of frozen dataclasses?
Alternative Approaches: Use `namedtuple`, plain classes, or ORM models for more
complex domain requirements.
Expected Output: The script prints structured dataclass instances, copied
updates, and aggregation results.
Key Takeaways: Dataclasses simplify structured data modeling while encouraging
clean, type-safe code.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import List


@dataclass(frozen=True)
class UserProfile:
    """A simple user profile record using a frozen dataclass."""

    username: str
    email: str
    is_active: bool = True
    roles: List[str] = field(default_factory=lambda: ["user"])


@dataclass
class ProductRecord:
    """A structured product record with default pricing and stock values."""

    product_id: str
    name: str
    price: float = 0.0
    in_stock: int = 0


def create_user_profile(username: str, email: str) -> UserProfile:
    """Create a new user profile dataclass instance."""
    return UserProfile(username=username, email=email)


def update_status(profile: UserProfile, is_active: bool) -> UserProfile:
    """Return a new user profile with the updated active status."""
    return replace(profile, is_active=is_active)


def add_role(profile: UserProfile, role: str) -> UserProfile:
    """Return a new user profile with an additional role."""
    updated_roles = profile.roles + [role]
    return replace(profile, roles=updated_roles)


def create_product(product_id: str, name: str, price: float, stock: int) -> ProductRecord:
    """Create a product record with default pricing and stock values."""
    return ProductRecord(product_id=product_id, name=name, price=price, in_stock=stock)


def average_age(ages: List[int]) -> float:
    """Compute the average age from a list of ages."""
    if not ages:
        return 0.0
    return sum(ages) / len(ages)


def main() -> None:
    """Main function demonstrating dataclass creation and usage."""
    profile = create_user_profile("alice", "alice@example.com")
    inactive_profile = update_status(profile, False)
    elevated_profile = add_role(profile, "admin")
    product = create_product("P123", "Notebook", 29.99, 120)
    average_age_result = average_age([24, 30, 28])

    print("User profile:", profile)
    print("Inactive profile:", inactive_profile)
    print("Elevated profile:", elevated_profile)
    print("Product record:", product)
    print("Average age:", average_age_result)


if __name__ == "__main__":
    main()
