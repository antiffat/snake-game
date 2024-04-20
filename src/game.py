import sys

class Game:
    MIN_SIZE = 5
    MAX_SIZE = 25

    def __init__(self, width=10, height=10, player_name="Player"):
        if not (self.MIN_SIZE <= width <= self.MAX_SIZE and self.MIN_SIZE <= height <= self.MAX_SIZE):
            raise ValueError(f"Map size must be between {self.MIN_SIZE}x{self.MIN_SIZE} and {self.MAX_SIZE}x{self.MAX_SIZE}.")
        self.width = width
        self.height = height
        self.player_name = player_name
        self.snake = [(width // 2, height // 2)] # creates a list containing a single tuple. It will start with one segment located in the middle of the game board.
        self.score = 0
        self.game_over = False
        self.food = self.spawn_food()



