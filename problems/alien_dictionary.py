"""alien_dictionary.py

Problem Statement:
Implement a Python module that determines the order of letters in an alien language.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: graph construction, topological sort, dependency ordering,
cycle detection
Real-world Use Case: Inferring custom alphabet order from sorted dictionary data and language processing.
Input Description: Function accepts a list of words sorted lexicographically in an alien dictionary.
Output Description: Returns a string representing a valid letter order or an empty string if invalid.
Example Inputs and Outputs:
    words = ["wrt","wrf","er","ett","rftt"] -> "wertf"
Constraints: Use O(C + V) time for characters and edges.
Brute Force Approach: Compare pairs of words and sort letters using discovered precedence.
Optimized Approach: Build a directed graph and run topological sort.
Time Complexity: O(n * l + alphabet_size)
Space Complexity: O(alphabet_size + edges)
Step-by-step Dry Run:
    compare adjacent words, create dependency edges, detect cycles with DFS or Kahn's algorithm.
Edge Cases: prefix invalidation, isolated characters, and single-word input.
Common Mistakes: ignoring prefix conflict and not including all letters.
Follow-up Interview Questions:
    1. How do you handle multiple valid orders?
    2. Can you detect invalid inputs due to cycles?
    3. What if the alphabet contains characters not in any constraint edge?
Alternative Approaches: Use DFS-based topsort or Kahn's BFS.
Expected Output: The script prints a valid alien dictionary order for a sample input.
Key Takeaways: Topological sort recovers order from precedence constraints.
"""

from collections import deque

def alien_order(words: list[str]) -> str:
    """Return any valid character ordering; return empty for invalid dictionaries."""
    graph = {char: set() for word in words for char in word}
    indegree = dict.fromkeys(graph, 0)
    for first, second in zip(words, words[1:]):
        for left, right in zip(first, second):
            if left != right:
                if right not in graph[left]:
                    graph[left].add(right)
                    indegree[right] += 1
                break
        else:
            if len(first) > len(second):
                return ""
    queue = deque(char for char in graph if indegree[char] == 0)
    order = []
    while queue:
        char = queue.popleft()
        order.append(char)
        for following in sorted(graph[char]):
            indegree[following] -= 1
            if indegree[following] == 0:
                queue.append(following)
    return "".join(order) if len(order) == len(graph) else ""
