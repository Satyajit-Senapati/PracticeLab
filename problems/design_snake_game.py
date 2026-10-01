"""design_snake_game.py

Problem Statement:
Implement a Python module that simulates the Snake game's movement on a grid with food.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: queue, set membership, state simulation, data structures
Real-world Use Case: Game simulation, movement tracking, and collision detection.
Input Description: Class accepts width, height, and a list of food positions.
Output Description: Provides a move(direction) method returning the current score or -1 if the game ends.
Example Inputs and Outputs:
    snake = SnakeGame(width=3, height=2, food=[[1,2],[0,1]])
    snake.move("R") -> 0
Constraints: Avoid O(n) collisions by using a set for body positions.
Brute Force Approach: Use a list and scan for self-collision each move.
Optimized Approach: Maintain a deque for the snake body and a set for occupied cells.
Time Complexity: O(1) per move.
Space Complexity: O(width*height)
Step-by-step Dry Run:
    move head based on direction, check boundaries and self-collision, consume food when present.
Edge Cases: eating food at the edge and moving into the tail cell just vacated.
Common Mistakes: forgetting to remove tail from occupied set before checking self-collision.
Follow-up Interview Questions:
    1. How to extend this to multiple snakes?
    2. What if food appears randomly?
    3. Can you support wrap-around boundaries?
Alternative Approaches: Use grid matrix if space allows.
Expected Output: The script demonstrates the snake simulation with sample moves.
Key Takeaways: Deque and set combination enables efficient snake state updates.
"""

from collections import deque

class SnakeGame:
    """Track the body and permanent game-over state in constant time per move."""
    def __init__(self, width: int, height: int, food: list[list[int]]):
        if width <= 0 or height <= 0:
            raise ValueError("Board dimensions must be positive.")
        self.width, self.height = width, height
        self.food = [tuple(cell) for cell in food]
        self.body = deque([(0, 0)])
        self.occupied = {(0, 0)}
        self.score = 0
        self.game_over = False

    def move(self, direction: str) -> int:
        if self.game_over:
            return -1
        offsets = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        if direction not in offsets:
            raise ValueError("Direction must be U, D, L, or R.")
        row, col = self.body[0]
        dr, dc = offsets[direction]
        head = (row + dr, col + dc)
        growing = self.score < len(self.food) and head == self.food[self.score]
        collision = head in self.occupied and (growing or head != self.body[-1])
        if not (0 <= head[0] < self.height and 0 <= head[1] < self.width) or collision:
            self.game_over = True
            return -1
        if not growing:
            self.occupied.remove(self.body.pop())
        else:
            self.score += 1
        self.body.appendleft(head)
        self.occupied.add(head)
        return self.score
