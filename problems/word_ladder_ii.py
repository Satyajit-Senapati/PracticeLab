"""word_ladder_ii.py

Problem Statement:
Implement a Python module that finds all shortest transformation sequences from beginWord to endWord.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BFS, backtracking, word graph, shortest paths,
path enumeration
Real-world Use Case: Finding minimal valid transformations in word ladders and sequence planning in state graphs.
Input Description: Function accepts a beginWord, endWord, and a word list.
Output Description: Returns all shortest transformation sequences.
Example Inputs and Outputs:
    beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] -> [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Constraints: Use BFS to discover the shortest path length, then DFS to build sequences.
Brute Force Approach: DFS all paths with pruning.
Optimized Approach: Build adjacency via wildcard patterns and track distance levels.
Time Complexity: O(N * L^2) where N is word count and L is word length.
Space Complexity: O(N * L)
Step-by-step Dry Run:
    BFS from beginWord to build graph distances, then backtrack from endWord along shortest-first parents.
Edge Cases: no valid transformation and beginWord equals endWord.
Common Mistakes: generating non-shortest paths or missing multiple equal-length sequences.
Follow-up Interview Questions:
    1. How to improve performance with bidirectional BFS?
    2. What if words are extremely long?
    3. Can you return only the number of paths?
Alternative Approaches: Use parent tracking during BFS only.
Expected Output: The script prints all shortest transformation sequences for a sample input.
Key Takeaways: Combining BFS for distance with DFS for path reconstruction yields all shortest sequences.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, List


def build_graph(words: List[str]) -> Dict[str, List[str]]:
    graph: Dict[str, List[str]] = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            graph[pattern].append(word)
    return graph


def find_ladders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if beginWord == endWord:
        return [[beginWord]]
    if endWord not in wordList:
        return []
    words = sorted(set(wordList) | {beginWord})
    graph = build_graph(words)
    distances: Dict[str, int] = {beginWord: 0}
    queue = deque([beginWord])

    while queue:
        current = queue.popleft()
        for i in range(len(current)):
            pattern = current[:i] + "*" + current[i+1:]
            for neighbor in graph[pattern]:
                if neighbor not in distances:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

    results: List[List[str]] = []
    if endWord not in distances:
        return results

    def backtrack(path: List[str]) -> None:
        word = path[-1]
        if word == endWord:
            results.append(path.copy())
            return
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            for neighbor in graph[pattern]:
                if distances.get(neighbor, float("inf")) == distances[word] + 1:
                    path.append(neighbor)
                    backtrack(path)
                    path.pop()

    backtrack([beginWord])
    return results


def main() -> None:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solutions = find_ladders(beginWord, endWord, wordList)
    print("Word ladders:", solutions)


if __name__ == "__main__":
    main()
