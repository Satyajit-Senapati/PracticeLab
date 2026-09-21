"""word_ladder.py

Problem Statement:
Implement a Python module that finds the length of the shortest transformation
sequence from a begin word to an end word by changing one letter at a time and
only using words from a given dictionary.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BFS, word graph modeling, shortest path, string mutation
Real-world Use Case: Spelling correction, word morphing puzzles, and search
space traversal.
Input Description: Functions accept a begin word, end word, and word list.
Output Description: Functions return the length of the shortest transformation
sequence or 0 if no sequence exists.
Example Inputs and Outputs:
    ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) -> 5
Constraints: Use O(N * L^2) time where N is dictionary size and L is word
length. Use BFS to find the shortest path.
Brute Force Approach: Build the full word graph and search all paths.
Optimized Approach: Use BFS with intermediate wildcard states.
Time Complexity: O(N * L^2)
Space Complexity: O(N * L)
Step-by-step Dry Run:
    hit -> hot -> dot -> dog -> cog
    return 5
Edge Cases: end word not present, empty dictionary, begin equals end.
Common Mistakes: using DFS instead of BFS for shortest path, regenerating
neighbors inefficiently, and not marking visited states.
Follow-up Interview Questions:
    1. How would you produce the actual transformation sequence?
    2. Can you optimize by bidirectional BFS?
    3. What happens if words have varying lengths?
Alternative Approaches: Use bidirectional BFS or precompute wildcard maps.
Expected Output: The script prints shortest transformation lengths for sample inputs.
Key Takeaways: BFS on a word graph finds the shortest path in transformation problems.
"""

from __future__ import annotations

from collections import deque, defaultdict
from typing import Dict, List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """Return the length of the shortest transformation sequence."""
    if end_word not in word_list:
        return 0

    word_list = list(set(word_list + [begin_word]))
    adjacency: Dict[str, List[str]] = defaultdict(list)
    word_length = len(begin_word)

    for word in word_list:
        for i in range(word_length):
            intermediate = word[:i] + "*" + word[i+1:]
            adjacency[intermediate].append(word)

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        current_word, level = queue.popleft()
        for i in range(word_length):
            intermediate = current_word[:i] + "*" + current_word[i+1:]
            for neighbor in adjacency[intermediate]:
                if neighbor == end_word:
                    return level + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
            adjacency[intermediate] = []

    return 0


def main() -> None:
    """Main function demonstrating word ladder BFS."""
    examples = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
        ("a", "c", ["a", "b", "c"]),
    ]
    for begin, end, word_list in examples:
        print(f"{begin} -> {end}: {ladder_length(begin, end, word_list)}")


if __name__ == "__main__":
    main()
