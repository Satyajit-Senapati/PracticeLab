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
