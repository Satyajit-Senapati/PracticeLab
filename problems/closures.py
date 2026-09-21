"""closures.py

Problem Statement:
Implement a Python module that demonstrates closures, showing how inner
functions capture and retain access to variables from an enclosing scope.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: closures, lexical scoping, nested functions, state retention,
function factories, decorators
Real-world Use Case: Building customizable callbacks, maintaining state in
functional pipelines, creating parameterized helpers, and encapsulating
configuration without global variables.
Input Description: Functions accept configuration values, iterable inputs, and
optional transformation parameters.
Output Description: Functions return callable closures that retain environment
state or produce transformed data using retained values.
Example Inputs and Outputs:
    make_multiplier(3)(5) -> 15
    make_greeter("Alice")() -> "Hello, Alice!"
    recorded_calls = counter() -> callable; repeated calls increment state
Constraints: Use closures to encapsulate state safely, avoid global variables,
and keep inner functions simple and readable.
Brute Force Approach: Use global variables or class instances to store state.
Optimized Approach: Use closures to preserve state in a scoped, functional way.
Time Complexity: O(1) for closure creation and invocation, O(n) for iterating
through values when applicable.
Space Complexity: O(1) for closure state, O(n) for materialized collections when
processed.
Step-by-step Dry Run:
    multiplier = make_multiplier(4)
    result = multiplier(5)
    return 20
Edge Cases: mutable captured variables, closures over loop variables, repeated
invocations of closures, and side effects in captured state.
Common Mistakes: capturing the wrong variable in a loop, forgetting `nonlocal`
for writable enclosed variables, and using closures for overly complex state.
Follow-up Interview Questions:
    1. How does lexical scoping affect closure behavior?
    2. Why would you choose a closure over a class?
    3. What is the difference between `global` and `nonlocal`?
Alternative Approaches: Use classes to manage state, decorators for reusable
wrappers, or simple functions with explicit state parameters.
Expected Output: The script prints example closure creation and usage, including
stateful counters and reusable factories.
Key Takeaways: Closures provide a clean way to capture environment state and
keep behavior encapsulated without relying on global mutable state.
"""

from __future__ import annotations

from typing import Callable, Iterable, List


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Return a closure that multiplies its input by the captured factor."""

    def multiplier(value: int) -> int:
        return value * factor

    return multiplier


def make_greeter(name: str) -> Callable[[], str]:
    """Return a closure that greets the captured name."""

    greeting = f"Hello, {name}!"

    def greeter() -> str:
        return greeting

    return greeter


def make_counter() -> Callable[[], int]:
    """Return a closure that increments and returns a counter value."""

    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def make_power_function(exponent: int) -> Callable[[int], int]:
    """Return a closure that raises values to the captured exponent."""

    def power(value: int) -> int:
        return value ** exponent

    return power


def filter_with_threshold(values: Iterable[int], threshold: int) -> List[int]:
    """Filter values using a closure-based predicate."""

    def is_above_threshold(value: int) -> bool:
        return value > threshold

    return [value for value in values if is_above_threshold(value)]


def main() -> None:
    """Main function demonstrating closure examples."""
    times_three = make_multiplier(3)
    result = times_three(5)
    greeter = make_greeter("Alice")
    greeting_message = greeter()
    counter = make_counter()
    first_count = counter()
    second_count = counter()
    squared = make_power_function(2)
    squared_value = squared(6)
    filtered = filter_with_threshold([1, 5, 10, 12], 6)

    print("Multiplier result:", result)
    print("Greeting message:", greeting_message)
    print("Counter values:", [first_count, second_count])
    print("Squared value:", squared_value)
    print("Filtered values above threshold:", filtered)


if __name__ == "__main__":
    main()
