"""minimum_genetic_mutation.py

Problem Statement:
Find the minimum number of genetic mutations needed to transform a start gene into an end gene using valid mutations.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon
Concepts Tested: BFS, string mutation, shortest path in graph.
Real-world Use Case: mutation path analysis in computational biology.
Input Description: start gene, end gene, and a gene bank list.
Output Description: Minimum number of mutations, or -1 if impossible.
Example Inputs and Outputs:
    start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"] -> 1
Constraints: Each mutation changes one character at a time.
Time Complexity: O(n * m * k)
Space Complexity: O(n + m)
"""

from __future__ import annotations

from collections import deque


def min_mutation(start: str, end: str, bank: list[str]) -> int:
    """Return the minimum mutation steps from start to end."""
    bank_set = set(bank)
    if end not in bank_set:
        return -1

    genes = ['A', 'C', 'G', 'T']
    queue = deque([(start, 0)])
    visited: set[str] = {start}

    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps

        for i in range(len(current)):
            for gene in genes:
                if gene == current[i]:
                    continue
                mutated = current[:i] + gene + current[i + 1:]
                if mutated in bank_set and mutated not in visited:
                    visited.add(mutated)
                    queue.append((mutated, steps + 1))
    return -1


def main() -> None:
    print(min_mutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
    print(min_mutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))


if __name__ == "__main__":
    main()
