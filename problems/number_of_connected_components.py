"""number_of_connected_components.py

Problem Statement:
Count the number of connected components in an undirected graph.

Interview Difficulty: Medium
Commonly Asked By: Google, Amazon, Microsoft
Concepts Tested: graph traversal, DFS/BFS.
Real-world Use Case: network connectivity and cluster analysis.
Input Description: Number of nodes and an edge list.
Output Description: Number of connected components.
Example Inputs and Outputs:
    n = 5, edges = [[0,1],[1,2],[3,4]] -> 2
Constraints: Nodes are labeled from 0 to n-1.
Time Complexity: O(n + e)
Space Complexity: O(n + e)
"""

from __future__ import annotations

from collections import defaultdict, deque


def count_components(n: int, edges: list[list[int]]) -> int:
    """Return the number of connected components in the graph."""
    graph: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited: set[int] = set()
    components = 0

    for node in range(n):
        if node not in visited:
            components += 1
            queue = deque([node])
            visited.add(node)
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return components


def main() -> None:
    print(count_components(5, [[0, 1], [1, 2], [3, 4]]))
    print(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))


if __name__ == "__main__":
    main()
