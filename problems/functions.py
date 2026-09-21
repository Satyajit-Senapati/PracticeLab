"""functions.py

Problem Statement:
Build a Python module that demonstrates function definition, invocation,
parameter handling, default arguments, keyword-only arguments, return values,
and modular composition in an interview-ready format.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: functions, parameters, return values, default values,
keyword arguments, higher-order functions, modular design
Real-world Use Case: Encapsulating data transformation logic, reusing
behaviors across ETL pipelines, and separating business rules into testable
units.
Input Description: Functions receive numeric values, strings, iterables,
functions as arguments, and optional parameters.
Output Description: Functions return computed results, formatted strings,
collections, and transformed outputs.
Example Inputs and Outputs:
    add(1, 2) -> 3
    greet("Alice") -> "Hello, Alice!"
    apply_operation([1, 2], sum) -> 3
Constraints: Use clear function names, document behavior via docstrings, avoid
side effects, and apply type hints consistently.
Brute Force Approach: Place all logic in a single block and use global state.
Optimized Approach: Split responsibilities into small, composable functions
with explicit inputs and outputs.
Time Complexity: O(n) for iterable processing functions, O(1) for simple
arithmetic and string formatting.
Space Complexity: O(n) for copied list processing, O(1) for scalar
operations.
Step-by-step Dry Run:
    result = concatenate_strings(["a", "b"], ",")
    joined = "a,b"
    return "a,b"
Edge Cases: empty iterables, None inputs, missing keyword arguments, and
mixed value types.
Common Mistakes: using mutable default arguments, ignoring keyword-only
semantics, and failing to return values consistently.
Follow-up Interview Questions:
    1. Why should you avoid mutable default arguments?
    2. What is the difference between positional and keyword arguments?
    3. How do you write functions that are easy to unit test?
Alternative Approaches: Use callable classes for stateful behavior, decorators
for cross-cutting concerns, or dataclasses to represent structured inputs.
Expected Output: The script prints examples of function invocation, keyword
parameter usage, and higher-order function behavior.
Key Takeaways: Functions should be small, self-contained, and documented to
promote reuse and maintainability.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any, Dict, List, Optional, Sequence, Tuple


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting message using a default greeting prefix."""
    return f"{greeting}, {name}!"


def concatenate_strings(values: Sequence[str], separator: str = ",") -> str:
    """Concatenate values using the given separator."""
    return separator.join(values)


def apply_operation(values: Iterable[float], operation: Callable[[Iterable[float]], float]) -> float:
    """Apply a higher-order operation to an iterable of numeric values."""
    return operation(values)


def build_user_profile(
    username: str,
    *,
    email: str,
    is_active: bool = True,
    roles: Optional[Sequence[str]] = None,
) -> Dict[str, Any]:
    """Build a user profile dictionary using keyword-only arguments."""
    return {
        "username": username,
        "email": email,
        "is_active": is_active,
        "roles": list(roles) if roles is not None else ["user"],
    }


def safe_append(values: Optional[List[Any]], item: Any) -> List[Any]:
    """Append an item to a list with safe handling for None inputs."""
    if values is None:
        return [item]
    return values + [item]


def main() -> None:
    """Main function demonstrating function usage and patterns."""
    sum_result = add(3, 7)
    greeting = greet("Alice")
    custom_greeting = greet("Bob", greeting="Welcome")
    joined_string = concatenate_strings(["red", "green", "blue"], "|")
    operation_result = apply_operation([1, 2, 3, 4], sum)
    profile = build_user_profile("jdoe", email="jdoe@example.com", roles=("admin",))
    appended = safe_append(None, "first")

    print("Sum result:", sum_result)
    print("Greeting:", greeting)
    print("Custom greeting:", custom_greeting)
    print("Joined string:", joined_string)
    print("Operation result:", operation_result)
    print("User profile:", profile)
    print("Safe append result:", appended)


if __name__ == "__main__":
    main()
