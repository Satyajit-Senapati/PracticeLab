"""add_binary.py

Problem Statement:
Implement binary string addition for two non-negative numbers represented as
binary strings and return their sum as a binary string.

Interview Difficulty: Easy
Commonly Asked By: Google, Facebook, Amazon, Microsoft, Apple
Concepts Tested: string manipulation, arithmetic simulation, two-pointer
techniques, carry propagation
Real-world Use Case: binary arithmetic in bitwise systems and low-level data
representation.
Input Description: Two binary strings a and b.
Output Description: A binary string representing the sum.
Example Inputs and Outputs:
    add_binary("1010", "1011") -> "10101"
Constraints: Strings contain only '0' and '1' and may be up to 10^4 length.
Brute Force Approach: Convert to integers and add the values.
Optimized Approach: Add digit-by-digit from the least significant bit with carry.
Time Complexity: O(max(len(a), len(b)))
Space Complexity: O(max(len(a), len(b)))
Edge Cases: different lengths, all carries, empty string treated as "0".
Common Mistakes: forgetting the final carry, reversing the result incorrectly.
"""

from __future__ import annotations


def add_binary(a: str, b: str) -> str:
    """Add two binary strings and return the binary sum."""
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result: list[str] = []

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2

    return "".join(reversed(result))


def main() -> None:
    """Main function demonstrating add_binary examples."""
    examples = [
        ("1010", "1011"),
        ("0", "0"),
        ("1111", "1"),
        ("100", "110010"),
    ]
    for a, b in examples:
        print(f"{a} + {b} -> {add_binary(a, b)}")


if __name__ == "__main__":
    main()
