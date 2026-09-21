"""number_of_islands.py

Problem Statement:
Implement a Python module that counts the number of islands in a 2D grid of
land and water.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: BFS/DFS, grid traversal, connected components, recursion,
visited tracking
Real-world Use Case: Mapping land masses, image segmentation, flood fill,
and clustering in spatial grids.
Input Description: Functions accept a 2D list of characters ('1' for land,
'0' for water).
Output Description: Functions return the number of separated islands.
Example Inputs and Outputs:
    num_islands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]) -> 3
Constraints: Use O(m*n) time and O(m*n) space for visited state.
Brute Force Approach: Check every cell and flood fill if land.
Optimized Approach: Use DFS or BFS to mark connected land once.
Time Complexity: O(m * n)
Space Complexity: O(m * n)
Step-by-step Dry Run:
    scan top-left, find first island, mark connected cells visited, repeat.
    count = 3
Edge Cases: empty grid, all water, all land, and narrow grids.
Common Mistakes: revisiting cells, not marking visited before recursion,
and using diagonal adjacency incorrectly.
Follow-up Interview Questions:
    1. How would you handle diagonal adjacency?
    2. Can you solve this iteratively with BFS?
    3. How would this change for a dynamic water level?
Alternative Approaches: Use union-find to merge land cells into connected
components.
Expected Output: The script prints island counts for sample grids.
Key Takeaways: Grid graph connected component counting is a standard BFS/DFS application.
"""

from __future__ import annotations

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Return the number of islands in the grid."""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited: List[List[bool]] = [[False] * cols for _ in range(rows)]
    islands = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == "0" or visited[r][c]:
            return

        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                islands += 1
                dfs(r, c)

    return islands


def main() -> None:
    """Main function demonstrating island counting."""
    examples = [
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]],
    ]
    for grid in examples:
        print("Grid:")
        for row in grid:
            print("".join(row))
        print("Islands ->", num_islands(grid))
        print()


if __name__ == "__main__":
    main()
