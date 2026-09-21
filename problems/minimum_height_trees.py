"""minimum_height_trees.py

Problem Statement:
Find all roots of minimum height trees for an undirected graph with n nodes.

Interview Difficulty: Medium
Commonly Asked By: Google, Microsoft
Concepts Tested: graph trimming, topological order, BFS.
Real-world Use Case: choosing optimal roots in network design.
Input Description: integer n and edge list for a tree.
Output Description: List of root labels producing minimum height.
Example Inputs and Outputs:
    n=4, edges=[[1,0],[1,2],[1,3]] -> [1]
Constraints: The graph is a tree with n nodes and n-1 edges.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations

from collections import deque, defaultdict


def find_min_height_trees(n: int, edges: list[list[int]]) -> list[int]:
    """Return all roots of minimum height trees."""
    if n == 1:
        return [0]

    neighbors: dict[int, set[int]] = defaultdict(set)
    degree = [0] * n
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
        degree[u] += 1
        degree[v] += 1

    leaves = deque(i for i in range(n) if degree[i] == 1)
    remaining = n
    while remaining > 2:
        leaves_count = len(leaves)
        remaining -= leaves_count
        for _ in range(leaves_count):
            leaf = leaves.popleft()
            for neighbor in neighbors[leaf]:
                neighbors[neighbor].remove(leaf)
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)
    return list(leaves)


def main() -> None:
    print(find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]))
    print(find_min_height_trees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))


if __name__ == "__main__":
    main()
