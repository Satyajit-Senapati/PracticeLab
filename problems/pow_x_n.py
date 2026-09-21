"""pow_x_n.py

Problem Statement:
Implement pow(x, n), which calculates x raised to the power n.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: binary exponentiation, recursion, fast power.
Real-world Use Case: mathematical libraries, exponentiation in graphics and simulations.
Input Description: a float x and an integer n.
Output Description: x raised to the power n.
Example Inputs and Outputs:
    x = 2.0, n = 10 -> 1024.0
    x = 2.1, n = 3 -> 9.261
Constraints: Support negative exponents and large n.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from __future__ import annotations


def my_pow(x: float, n: int) -> float:
    """Calculate x to the power n using fast exponentiation."""
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    while n > 0:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result


def main() -> None:
    examples = [
        (2.0, 10),
        (2.1, 3),
        (2.0, -2),
        (0.5, 3),
    ]
    for x, n in examples:
        print(f"{x}^{n} -> {my_pow(x, n)}")


if __name__ == "__main__":
    main()
