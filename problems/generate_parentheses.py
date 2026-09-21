"""generate_parentheses.py

Problem Statement:
Generate all combinations of well-formed parentheses for a given number of pairs.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Facebook
Concepts Tested: backtracking, recursion, combinatorics.
Real-world Use Case: expression generation and bracket matching.
Input Description: An integer n representing pairs of parentheses.
Output Description: A list of valid parentheses strings.
Example Inputs and Outputs:
    n = 3 -> ["((()))","(()())","(())()","()(())","()()()"]
Constraints: Generate all well-formed combinations.
Time Complexity: O Catalan number growth.
Space Complexity: O(n * C_n)
"""

from __future__ import annotations


def generate_parentheses(n: int) -> list[str]:
    """Return all well-formed parentheses combinations for n pairs."""
    result: list[str] = []

    def backtrack(current: str, open_count: int, close_count: int) -> None:
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


def main() -> None:
    print(generate_parentheses(3))
    print(generate_parentheses(1))


if __name__ == "__main__":
    main()
