"""dijkstra_shortest_paths.py

Problem Statement:
Compute shortest distances from a start vertex in a directed weighted graph.
Each adjacency entry contains (neighbor, weight) pairs. Reject negative
weights and return distances only for reachable vertices.
Interview Difficulty: Medium
Concepts Tested: heap, Dijkstra, weighted graphs, shortest paths
Input Description: A graph with hashable vertices and non-negative integer weights.
Output Description: A dictionary of reachable vertices and their shortest distances.
Example Inputs and Outputs:
    dijkstra_shortest_paths({"a":[("b",4),("c",1)],"c":[("b",2)]}, "a") -> {"a":0,"c":1,"b":3}
Constraints: All edge weights must be non-negative integers.
Time Complexity: O((V + E) log (V + E))
Space Complexity: O(V + E)
"""

import heapq
from itertools import count

def dijkstra_shortest_paths(graph: dict, start) -> dict:
    """Use stale-entry skipping and a tie counter for arbitrary hashable vertices."""
    if any(weight < 0 for edges in graph.values() for _, weight in edges):
        raise ValueError("Dijkstra requires non-negative weights.")
    sequence = count()
    distances = {start: 0}
    heap = [(0, next(sequence), start)]
    while heap:
        distance, _, vertex = heapq.heappop(heap)
        if distance != distances[vertex]:
            continue
        for neighbor, weight in graph.get(vertex, ()):
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, next(sequence), neighbor))
    return distances
