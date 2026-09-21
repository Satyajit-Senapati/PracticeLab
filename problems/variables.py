"""variables.py

Problem Statement:
Implement a Python module that demonstrates core variable concepts, including
assignment, types, mutability, scope, and swapping values in an interview-ready way.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: variables, assignment, data types, naming conventions, scope,
mutability, constants, swap operations, Python fundamentals
Real-world Use Case: Managing configuration values, intermediary state in data
pipelines, temporary computation storage, and ensuring predictable behavior
when handling mutable vs immutable objects.
Input Description: The module accepts standard Python values such as integers,
strings, booleans, lists, and dictionaries through function parameters.
Output Description: The functions return transformed values, demonstrating
correct variable usage and state management.
Example Inputs and Outputs:
    assign_variables() -> {'count': 42, 'price': 19.99, 'name': 'Alice', 'active': True}
    swap_variables(1, 2) -> (2, 1)
    update_list_item([1, 2, 3], 4) -> [4, 2, 3]
Constraints: Use clear variable names, maintain immutability for constants,
respect PEP 8 style, and use type hints for readability.
Brute Force Approach: Assign variables directly and return values without
modularization.
Optimized Approach: Encapsulate behavior in well-named functions, use type
hints, and keep operations simple and explicit.
Time Complexity: O(n) for list modification operations, O(1) for simple
assignments and swaps.
Space Complexity: O(n) when producing new collections, O(1) for scalar values.
Step-by-step Dry Run:
    result = swap_variables(5, 10)
    temp = 5
    first = 10
    second = 5
    return (10, 5)
Edge Cases: Empty lists, repeated values, None assignments, and variable
shadowing in nested scopes.
Common Mistakes: Reassigning a value before using it, confusing mutable and
immutable objects, using reserved keywords as variable names, and failing to
follow naming conventions.
Follow-up Interview Questions:
    1. What is the difference between mutable and immutable objects?
    2. How does variable scope affect function behavior?
    3. Why are constants conventionally uppercase in Python?
Alternative Approaches: Use tuples for immutable grouped values, dataclasses for
structured state, or dictionaries for named collections.
Expected Output: The script prints representative examples of variable
assignment, swapping, and container update behavior.
Key Takeaways: Clean variable naming, type clarity, and understanding scope and
mutability are essential coding fundamentals.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple


CONSTANT_MAX_RETRIES: int = 5
"""Demonstrate a constant value declared using naming conventions."""


def assign_variables() -> Dict[str, Any]:
    """Assign sample variables and return them as a dictionary.

    This function highlights basic variable assignment and type usage.
    """
    count: int = 42
    price: float = 19.99
    name: str = "Alice"
    active: bool = True

    return {
        "count": count,
        "price": price,
        "name": name,
        "active": active,
    }


def swap_variables(first: Any, second: Any) -> Tuple[Any, Any]:
    """Swap two variables and return the swapped values.

    Args:
        first: The first value to swap.
        second: The second value to swap.

    Returns:
        A tuple containing the values in reversed positions.
    """
    return second, first


def update_list_item(values: List[Any], new_first_item: Any) -> List[Any]:
    """Update the first item of a list in a controlled way.

    Args:
        values: A list of values to update.
        new_first_item: The new value to place at index 0.

    Returns:
        A new list with the updated first item.
    """
    if not values:
        return [new_first_item]

    updated_values: List[Any] = [new_first_item] + values[1:]
    return updated_values


def demonstrate_scope() -> Dict[str, str]:
    """Show how variable scope works between local and outer contexts."""

    outer_value: str = "outer"

    def inner_scope() -> str:
        inner_value: str = "inner"
        return f"{outer_value}:{inner_value}"

    return {
        "outer_value": outer_value,
        "inner_scope_result": inner_scope(),
    }


def main() -> None:
    """Main entry point for demonstration and example output."""
    assignments = assign_variables()
    swapped = swap_variables(1, 2)
    updated_list = update_list_item([1, 2, 3], 99)
    scope_demo = demonstrate_scope()

    print("Variable assignment example:", assignments)
    print("Swapped values example:", swapped)
    print("Updated list example:", updated_list)
    print("Scope demonstration example:", scope_demo)
    print("Constant value example:", CONSTANT_MAX_RETRIES)


if __name__ == "__main__":
    main()
