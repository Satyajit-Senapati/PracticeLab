"""reverse_bits.py

Problem Statement:
Reverse the bits of a 32-bit unsigned integer.

Interview Difficulty: Easy
Commonly Asked By: Microsoft, Apple, Amazon, Google
Concepts Tested: bit manipulation and binary representation.
Real-world Use Case: low-level bitfields, hashing, and network protocols.
Input Description: A 32-bit unsigned integer.
Output Description: The unsigned integer result after reversing bits.
Example Inputs and Outputs:
    43261596 -> 964176192
Constraints: Assume a 32-bit input.
Time Complexity: O(1)
Space Complexity: O(1)
"""

from __future__ import annotations


def reverse_bits(n: int) -> int:
    """Reverse the bits of a 32-bit unsigned integer."""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


def main() -> None:
    examples = [43261596, 0, 1, 4294967295]
    for value in examples:
        print(f"{value} -> {reverse_bits(value)}")


if __name__ == "__main__":
    main()
