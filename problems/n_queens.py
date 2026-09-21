"""n_queens.py

Problem Statement:
Implement a Python module that finds all distinct solutions to the N-Queens problem.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, constraint satisfaction, recursion, and pruning
Real-world Use Case: Resource placement problems, scheduling non-conflicting tasks, and combinatorial search.
Input Description: Functions accept a board size n.
Output Description: Functions return all valid board placements with queens.
Example Inputs and Outputs:
    solve_n_queens(4) -> [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
Constraints: Use O(n!) time and prune invalid queen placements early.
Brute Force Approach: Check every possible configuration.
Optimized Approach: Use backtracking with column and diagonal checks.
Time Complexity: O(n!)
Space Complexity: O(n^2) for result storage and recursion.
Step-by-step Dry Run:
    place queen in first row, then recursive row placements.
    backtrack when any column or diagonal is attacked.
Edge Cases: n = 0, n = 1, and n = 2 or n = 3 where no solutions exist.
Common Mistakes: missing diagonal calculation, not restoring state, and using
inefficient validation.
Follow-up Interview Questions:
    1. What are the diagonal conflict formulas?
    2. How can you compute only the count of solutions efficiently?
    3. How does symmetry reduce search space?
Alternative Approaches: Use bitmasking for faster solving in languages with
efficient bit operations.
Expected Output: The script prints all n-queens solutions for sample board sizes.
Key Takeaways: Constraint-aware backtracking efficiently explores valid queen placements.
"""

from __future__ import annotations

from typing import List, Set


def solve_n_queens(n: int) -> List[List[str]]:
    """Return all distinct solutions for the N-Queens problem."""
    solutions: List[List[str]] = []
    queens: List[int] = [-1] * n
    columns: Set[int] = set()
    diagonals: Set[int] = set()
    anti_diagonals: Set[int] = set()

    def build_board() -> List[str]:
        board: List[str] = []
        for row in range(n):
            row_chars = ["."] * n
            row_chars[queens[row]] = "Q"
            board.append("".join(row_chars))
        return board

    def backtrack(row: int) -> None:
        if row == n:
            solutions.append(build_board())
            return

        for col in range(n):
            current_diag = row - col
            current_anti_diag = row + col
            if col in columns or current_diag in diagonals or current_anti_diag in anti_diagonals:
                continue
            queens[row] = col
            columns.add(col)
            diagonals.add(current_diag)
            anti_diagonals.add(current_anti_diag)

            backtrack(row + 1)

            columns.remove(col)
            diagonals.remove(current_diag)
            anti_diagonals.remove(current_anti_diag)
            queens[row] = -1

    backtrack(0)
    return solutions


def main() -> None:
    """Main function demonstrating N-Queens solutions."""
    for n in range(1, 5):
        solutions = solve_n_queens(n)
        print(f"n={n}, solutions={len(solutions)}")
        for solution in solutions:
            print("\n".join(solution))
            print()


if __name__ == "__main__":
    main()
