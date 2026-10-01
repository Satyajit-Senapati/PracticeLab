"""operators.py

Problem Statement:
Create a Python module that demonstrates core operator behavior including
arithmetic, comparison, logical, bitwise, assignment, and membership operators.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: operators, expressions, precedence, evaluation order, boolean
logic, bitwise operations, augmented assignment, membership testing
Real-world Use Case: Validating business rules, computing metrics, filtering
records, toggling flags, and performing data transformations in pipelines.
Input Description: Functions accept numeric values, strings, Booleans, and
iterables to demonstrate operator semantics.
Output Description: The functions return computed results, boolean decisions,
and collections that reflect correct operator usage.
Example Inputs and Outputs:
    arithmetic_operations(5, 3) -> {'sum': 8, 'difference': 2, 'product': 15, 'quotient': 1.6666666666666667, 'power': 125, 'modulo': 2}
    comparison_operations(5, 3) -> {'equal': False, 'not_equal': True, 'greater': True, 'greater_or_equal': True, 'less': False, 'less_or_equal': False}
    logical_operations(True, False) -> {'and': False, 'or': True, 'not_first': False, 'not_second': True}
Constraints: Use Python best practices, type hints, meaningful variable names,
and avoid side effects in demonstration functions.
Brute Force Approach: Write separate expressions inline without reusable
structure.
Optimized Approach: Encapsulate operator demonstrations in dedicated functions
with clear inputs and outputs.
Time Complexity: O(n) for membership checks on iterables, O(1) for scalar
operations.
Space Complexity: O(n) for output dictionaries, O(1) for scalar results.
Step-by-step Dry Run:
    result = arithmetic_operations(2, 4)
    sum_result = 6
    difference_result = -2
    product_result = 8
    quotient_result = 0.5
    return {...}
Edge Cases: Division by zero, empty iterables, non-hashable membership targets,
and mixed type comparisons.
Common Mistakes: Using `/` when integer division is intended, confusing `and`
with `&`, misordering expressions, and forgetting short-circuit behavior.
Follow-up Interview Questions:
    1. What is the difference between `==` and `is`?
    2. How does operator precedence affect expression evaluation?
    3. When should you use bitwise operators instead of logical operators?
Alternative Approaches: Use Python `operator` module for function equivalents,
expressions in lambdas, or custom wrapper classes for operator overloading.
Expected Output: The script prints representative examples of arithmetic,
comparison, logical, bitwise, and membership operations.
Key Takeaways: Understanding operator semantics is critical for correct logic
and expressive, maintainable code.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple


def arithmetic_operations(first: float, second: float) -> Dict[str, float]:
    """Perform basic arithmetic operations on two numeric values."""
    if second == 0:
        quotient = float("inf")
    else:
        quotient = first / second

    return {
        "sum": first + second,
        "difference": first - second,
        "product": first * second,
        "quotient": quotient,
        "power": first ** second,
        "modulo": first % second if second != 0 else None,
    }


def comparison_operations(first: Any, second: Any) -> Dict[str, bool]:
    """Compare two values using standard comparison operators."""
    return {
        "equal": first == second,
        "not_equal": first != second,
        "greater": first > second,
        "greater_or_equal": first >= second,
        "less": first < second,
        "less_or_equal": first <= second,
    }


def logical_operations(first: bool, second: bool) -> Dict[str, bool]:
    """Evaluate logical operators on boolean inputs."""
    return {
        "and": first and second,
        "or": first or second,
        "not_first": not first,
        "not_second": not second,
    }


def bitwise_operations(first: int, second: int) -> Dict[str, int]:
    """Demonstrate bitwise operator results for integers."""
    return {
        "and": first & second,
        "or": first | second,
        "xor": first ^ second,
        "left_shift": first << 1,
        "right_shift": first >> 1,
        "bitwise_not_first": ~first,
    }


def assignment_operations(value: int) -> Dict[str, int]:
    """Demonstrate augmented assignment behavior."""
    result = value
    result += 2
    result -= 1
    result *= 3
    result //= 2
    result %= 5
    return {"final_result": result}


def membership_operations(target: Any, collection: Iterable[Any]) -> Dict[str, bool]:
    """Test membership using `in` and `not in` operators."""
    return {
        "is_member": target in collection,
        "is_not_member": target not in collection,
    }


def identity_vs_equality(first: Any, second: Any) -> Dict[str, bool]:
    """Compare identity and equality for two objects."""
    return {
        "equal": first == second,
        "identical": first is second,
    }


def main() -> None:
    """Main function demonstrating operator examples."""
    arithmetic_result = arithmetic_operations(7, 3)
    comparison_result = comparison_operations(7, 3)
    logical_result = logical_operations(True, False)
    bitwise_result = bitwise_operations(7, 3)
    assignment_result = assignment_operations(4)
    membership_result = membership_operations("apple", ["apple", "banana"])
    identity_result = identity_vs_equality([1, 2], [1, 2])

    print("Arithmetic operations:", arithmetic_result)
    print("Comparison operations:", comparison_result)
    print("Logical operations:", logical_result)
    print("Bitwise operations:", bitwise_result)
    print("Assignment operations:", assignment_result)
    print("Membership operations:", membership_result)
    print("Identity vs equality:", identity_result)


if __name__ == "__main__":
    main()
