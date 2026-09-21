"""decorators.py

Problem Statement:
Implement a Python module that demonstrates function decorators, including
wrapping behavior, metadata preservation, and practical use cases like timing
and input validation.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: decorators, higher-order functions, closures, functools,
metadata preservation, cross-cutting concerns
Real-world Use Case: Logging, performance monitoring, authentication,
retry policies, and validation in data processing or web application layers.
Input Description: Functions accept callable targets, numeric and string values,
and optional configuration parameters for decorator behavior.
Output Description: Decorated functions return original results while additional
aspects are applied transparently.
Example Inputs and Outputs:
    add(1, 2) -> 3 with logged execution
    greet("Alice") -> "Hello, Alice!"
    safe_divide(1, 0) -> None with validation warning
Constraints: Use decorators to separate concerns, preserve function metadata
with functools.wraps, avoid decorator side effects, and support reusable
wrappers.
Brute Force Approach: Inline logging or validation in each function body.
Optimized Approach: Apply cross-cutting behavior via reusable decorators.
Time Complexity: O(1) overhead for simple decorator wrapping, additional cost
for logging or validation operations.
Space Complexity: O(1) additional wrapper state.
Step-by-step Dry Run:
    decorated_add = log_execution(add)
    result = decorated_add(1, 2)
    print start and end logs
    return 3
Edge Cases: missing function metadata, chained decorators, exceptions inside
wrapped functions, and decorator calls with parameters.
Common Mistakes: forgetting functools.wraps, using decorators incorrectly,
and not handling variable positional or keyword arguments.
Follow-up Interview Questions:
    1. How do decorators work under the hood in Python?
    2. What is the purpose of functools.wraps?
    3. How can decorators be used with classes?
Alternative Approaches: Use context managers for scoped behavior, explicit wrapper
functions, or mixins for class-based cross-cutting concerns.
Expected Output: The script prints decorated function execution logs, validation
warnings, and original function results.
Key Takeaways: Decorators provide a clean way to add reusable behavior around
function execution without modifying core logic.
"""

from __future__ import annotations

import functools
import time
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log_execution(func: F) -> F:
    """Decorator that logs function execution start and end."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        function_name = func.__name__
        print(f"Starting execution of {function_name}")
        result = func(*args, **kwargs)
        print(f"Finished execution of {function_name}")
        return result

    return wrapper  # type: ignore[return-value]


def time_execution(func: F) -> F:
    """Decorator that measures how long a function takes to execute."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"{func.__name__} executed in {elapsed:.6f} seconds")
        return result

    return wrapper  # type: ignore[return-value]


def validate_non_zero_division(func: F) -> F:
    """Decorator that validates denominator values before division."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if len(args) >= 2 and args[1] == 0:
            print("Warning: division by zero avoided")
            return None
        if kwargs.get("denominator") == 0:
            print("Warning: division by zero avoided")
            return None
        return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]


@log_execution
@time_execution
def add(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


@validate_non_zero_division
def divide(numerator: int, denominator: int) -> Any:
    """Return the result of integer division, or None on zero denominator."""
    return numerator / denominator


def main() -> None:
    """Main function demonstrating decorator behavior."""
    addition_result = add(3, 5)
    division_result = divide(10, 0)
    division_success = divide(10, 2)

    print("Addition result:", addition_result)
    print("Division result with zero denominator:", division_result)
    print("Division result:", division_success)


if __name__ == "__main__":
    main()
