"""word_search.py

Problem Statement:
Implement a Python module that checks whether a given word exists in a 2D
character board by tracing adjacent characters horizontally or vertically.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: DFS backtracking, grid traversal, visited tracking,
string matching
Real-world Use Case: Word search puzzles, pattern detection in matrices, and
path finding in game boards.
Input Description: Functions accept a 2D list of characters and a target word.
Output Description: Functions return True if the word can be formed by
adjacent letters, otherwise False.
Example Inputs and Outputs:
    exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED") -> True
Constraints: Use O(m*n*4^L) time in the worst case due to backtracking, where
L is the word length.
Brute Force Approach: Try all starting positions and DFS search.
Optimized Approach: Use pruning with visited marking.
Time Complexity: O(m*n*4^L)
Space Complexity: O(L)
Step-by-step Dry Run:
    start at 'A', explore neighbors and match each character sequentially
    return True when full word matched
Edge Cases: empty board, empty word, single-cell board, and repeated
characters.
Common Mistakes: not marking visited cells, revisiting cells in the same
path, and failing to backtrack correctly.
Follow-up Interview Questions:
    1. How would you optimize for many search queries on the same board?
    2. Can you support diagonal adjacency?
    3. What changes if words can wrap around edges?
Alternative Approaches: Use a trie for multiple words, but for a single word
a DFS-backtracking approach is sufficient.
Expected Output: The script prints whether words exist for sample boards.
Key Takeaways: DFS with visited tracking is the standard way to search words in a grid.
"""

from __future__ import annotations

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """Return True if the word exists in the board by adjacent character path."""
    rows = len(board)
    cols = len(board[0]) if rows else 0
    visited: List[List[bool]] = [[False] * cols for _ in range(rows)]

    def dfs(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if (
            r < 0
            or c < 0
            or r >= rows
            or c >= cols
            or visited[r][c]
            or board[r][c] != word[index]
        ):
            return False

        visited[r][c] = True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if dfs(r + dr, c + dc, index + 1):
                return True
        visited[r][c] = False
        return False

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    return False


def main() -> None:
    """Main function demonstrating word search in a board."""
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print("ABCCED ->", exist(board, "ABCCED"))
    print("SEE ->", exist(board, "SEE"))
    print("ABCB ->", exist(board, "ABCB"))


if __name__ == "__main__":
    main()
