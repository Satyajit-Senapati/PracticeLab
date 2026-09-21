"""clone_graph.py

Problem Statement:
Implement a Python module that clones an undirected graph using depth-first search.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: graph traversal, recursion, mapping visited nodes, and cloning structures
Real-world Use Case: Graph data replication, object graph copying, and network topology cloning.
Input Description: Functions accept a reference node in an undirected graph.
Output Description: Functions return a deep copy of the graph rooted at that node.
Example Inputs and Outputs:
    clone_graph(node) -> copy of node and connected components
Constraints: Preserve graph structure and avoid infinite recursion on cycles.
Brute Force Approach: Use BFS/DFS with a visited map.
Optimized Approach: Use DFS recursion with a dictionary mapping original to clone.
Time Complexity: O(V + E)
Space Complexity: O(V)
Step-by-step Dry Run:
    clone each node if not seen, clone neighbors recursively, and return root clone.
Edge Cases: empty graph, single node with no neighbors, and cyclic graphs.
Common Mistakes: not cloning each node only once, missing neighbor links, and failing on self-loops.
Follow-up Interview Questions:
    1. How would you clone a directed graph?
    2. Can you do this iteratively with a stack?
    3. How would you handle graphs with additional node metadata?
Alternative Approaches: Use BFS with a queue and visited map.
Expected Output: The script prints the values of the cloned graph root.
Key Takeaways: Maintain a mapping from original nodes to cloned nodes during traversal.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(eq=False)
class Node:
    """Graph node for an undirected graph clone example."""
    val: int
    neighbors: List["Node"] = field(default_factory=list)


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """Return a deep clone of the graph starting at node."""
    if node is None:
        return None

    visited: Dict[Node, Node] = {}

    def dfs(current: Node) -> Node:
        if current in visited:
            return visited[current]

        clone = Node(current.val)
        visited[current] = clone
        for neighbor in current.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)


def main() -> None:
    """Main function demonstrating graph cloning."""
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned = clone_graph(node1)
    print("Original value:", node1.val)
    print("Cloned value:", cloned.val if cloned else None)


if __name__ == "__main__":
    main()
