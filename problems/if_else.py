"""if_else.py

Problem Statement:
Implement a Python module that demonstrates conditional logic using if/elif/else
branches across numeric, string, boolean, and membership conditions.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: conditional statements, boolean evaluation, branching logic,
control flow, short-circuiting, nested conditions, readability
Real-world Use Case: Routing requests, validating inputs, applying business
rules, feature toggles, and managing conditional workflow in ETL or API logic.
Input Description: Functions accept numbers, strings, booleans, and iterables.
Output Description: Functions return decisions, transformed values, or
categorized results based on conditions.
Example Inputs and Outputs:
    classify_number(10) -> "positive"
    classify_grade(85) -> "B"
    choose_discount(True, 25) -> "member discount"
Constraints: Use meaningful variable names, avoid nested condition complexity,
and keep branch logic explicit and testable.
Brute Force Approach: Write long nested if/else blocks without helper
functions.
Optimized Approach: Use clear conditional structure, guard clauses, and helper
functions for repeatable checks.
Time Complexity: O(1) for scalar comparisons, O(n) for membership checks in
iterables.
Space Complexity: O(1) for scalar outputs.
Step-by-step Dry Run:
    classification = classify_number(-5)
    result = "negative"
    return "negative"
Edge Cases: non-numeric input, boundary values, empty strings, and falsey
values like 0 or None.
Common Mistakes: incorrect condition ordering, using `if` instead of `elif`,
forgetting `else`, and mixing conditions without parentheses.
Follow-up Interview Questions:
    1. When should you use `elif` instead of nested `if`?
    2. How do truthy and falsy values affect condition evaluation?
    3. What patterns help keep conditional code maintainable?
Alternative Approaches: Use dictionary-based dispatch for simple cases,
lookup tables, or polymorphism for complex conditional behavior.
Expected Output: The script prints representative examples of numeric,
string, and boolean condition handling.
Key Takeaways: Readable conditional branches and well-defined decision logic
are essential for maintainable code.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, Union


def classify_number(value: float) -> str:
    """Classify a numeric value as positive, negative, or zero."""
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


def classify_grade(score: int) -> str:
    """Return a letter grade based on a numeric score."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def choose_discount(is_member: bool, purchase_amount: float) -> str:
    """Choose the correct discount message based on membership and amount."""
    if is_member and purchase_amount > 100:
        return "premium discount"
    if is_member:
        return "member discount"
    if purchase_amount > 100:
        return "standard discount"
    return "no discount"


def find_category(keyword: str, categories: Dict[str, Iterable[str]]) -> str:
    """Determine which category a keyword belongs to based on membership."""
    normalized_keyword = keyword.strip().lower()
    if not normalized_keyword:
        return "uncategorized"

    for category, keywords in categories.items():
        if normalized_keyword in (item.lower() for item in keywords):
            return category
    return "uncategorized"


def is_truthy(value: Any) -> bool:
    """Return whether a value evaluates to True in Python."""
    return bool(value)


def main() -> None:
    """Main function demonstrating if/elif/else logic examples."""
    number_result = classify_number(-5)
    grade_result = classify_grade(85)
    discount_result = choose_discount(True, 110.0)
    category_result = find_category(
        "Banana",
        {
            "fruit": ["apple", "banana", "orange"],
            "vegetable": ["carrot", "kale", "spinach"],
        },
    )
    truthy_result = is_truthy("")

    print("Number classification:", number_result)
    print("Grade classification:", grade_result)
    print("Discount selection:", discount_result)
    print("Category lookup:", category_result)
    print("Truthy evaluation for empty string:", truthy_result)


if __name__ == "__main__":
    main()
