"""find_ladders.py

Problem Statement:
Find all shortest transformation sequences from beginWord to endWord.

Interview Difficulty: Hard
Commonly Asked By: Google, Amazon
Concepts Tested: BFS, graph search, backtracking, shortest paths.
Real-world Use Case: analyzing stepwise transformations in word ladders.
Input Description: beginWord, endWord, and a word list.
Output Description: List of shortest transformation sequences.
Example Inputs and Outputs:
    beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    -> [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
Constraints: Return all shortest sequences.
Time Complexity: O(N + M)
Space Complexity: O(N + M)
"""

from __future__ import annotations

from collections import defaultdict, deque


def find_ladders(begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:
    word_set = set(word_list)
    if end_word not in word_set:
        return []

    layers: dict[str, list[list[str]]] = {begin_word: [[begin_word]]}
    while layers:
        next_layer: dict[str, list[list[str]]] = defaultdict(list)
        for word in layers:
            if word == end_word:
                return layers[word]
            for i in range(len(word)):
                prefix, suffix = word[:i], word[i+1:]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    candidate = prefix + c + suffix
                    if candidate in word_set:
                        next_layer[candidate] += [path + [candidate] for path in layers[word]]
        word_set -= set(next_layer)
        layers = next_layer
    return []


def main() -> None:
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(find_ladders(begin_word, end_word, word_list))


if __name__ == "__main__":
    main()
