"""word_search_ii.py

Problem Statement:
Implement a Python module that finds all words from a list present in a 2D board.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: trie, backtracking, DFS, pruning,
prefix search
Real-world Use Case: Word search puzzles, autocomplete over grid-based input, and pattern detection in matrices.
Input Description: Function accepts a 2D character board and a list of words.
Output Description: Returns all words that can be formed by sequentially adjacent letters.
Example Inputs and Outputs:
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"] -> ["oath","eat"]
Constraints: Use each cell once per word; optimize with a trie.
Brute Force Approach: DFS for each word separately.
Optimized Approach: Build a trie of words and search the board once.
Time Complexity: O(m*n*4^l) in worst case, pruned by trie prefixes.
Space Complexity: O(sum(word lengths))
Step-by-step Dry Run:
    build trie, DFS from each board cell with prefix pruning, collect matches.
Edge Cases: no board cells, empty word list.
Common Mistakes: revisiting the same cell in one word path or missing duplicate words.
Follow-up Interview Questions:
    1. How do tries help reduce repeated work?
    2. Can you return words in lexicographic order?
    3. What if diagonal moves are allowed?
Alternative Approaches: Use DFS without trie for small word lists.
Expected Output: The script prints the list of found words for a sample board.
Key Takeaways: Trie-based pruning can dramatically reduce search space in board word search.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = None
    word: Optional[str] = None

    def __post_init__(self) -> None:
        if self.children is None:
            self.children = {}


def build_trie(words: List[str]) -> TrieNode:
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word
    return root


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    root = build_trie(words)
    rows, cols = len(board), len(board[0])
    found: List[str] = []

    def dfs(r: int, c: int, node: TrieNode) -> None:
        char = board[r][c]
        if char not in node.children:
            return
        next_node = node.children[char]
        if next_node.word:
            found.append(next_node.word)
            next_node.word = None

        board[r][c] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, next_node)
        board[r][c] = char

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, root)

    return found


def main() -> None:
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print("Found words:", find_words(board, words))


if __name__ == "__main__":
    main()
