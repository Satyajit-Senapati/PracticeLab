"""shortest_path_unweighted.py

Problem Statement:
Return one shortest path between two vertices in an unweighted directed graph represented by an adjacency dictionary. Return [] if unreachable. Do not change the graph.
Interview Difficulty: Medium
Concepts Tested: BFS, parent tracking, path reconstruction
Input Description: A graph dictionary with hashable vertices, a start vertex, and a goal vertex.
Output Description: A vertex list including start and goal.
Example Inputs and Outputs:
    shortest_path({"a":["b"],"b":["c"]}, "a", "c") -> ["a","b","c"]
Constraints: A graph dictionary with hashable vertices, a start vertex, and a goal vertex.
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque

def shortest_path(graph: dict, start, goal) -> list:
    queue = deque([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            path = [current]
            while current != start:
                current = parent[current]
                path.append(current)
            return path[::-1]
        for neighbor in graph.get(current, ()):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    return []
