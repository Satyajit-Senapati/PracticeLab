"""count_primes.py

Problem Statement:
Count the number of prime numbers less than a non-negative integer n.

Interview Difficulty: Easy
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: sieve of Eratosthenes, prime detection, number theory.
Real-world Use Case: cryptography, prime-based hashing, and mathematical analysis.
Input Description: A non-negative integer n.
Output Description: Count of prime numbers strictly less than n.
Example Inputs and Outputs:
    n = 10 -> 4
Constraints: Use efficient sieve-based prime counting.
Time Complexity: O(n log log n)
Space Complexity: O(n)
"""

from __future__ import annotations


def count_primes(n: int) -> int:
    """Return the count of primes less than n."""
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p < n:
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
        p += 1
    return sum(is_prime)


def main() -> None:
    examples = [0, 1, 10, 100]
    for n in examples:
        print(f"{n} -> {count_primes(n)}")


if __name__ == "__main__":
    main()
