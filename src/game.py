import random
import sys
import time


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

    def spawn_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def move_snake(self, direction):
        head_x, head_y = self.snake[0]
        if direction == "UP":
            head_y -= 1
        elif direction == "DOWN":
            head_y += 1
        elif direction == "LEFT":
            head_x -= 1
        elif direction == "RIGHT":
            head_x += 1
        new_head = (head_x, head_y) # what the heck is it

        if new_head in self.snake or not (0 <= head_x < self.width and 0 <= head_y < self.height):
            self.game_over = True
            print("Game Over!")
        else:
            self.snake.insert(0, new_head)
            if new_head == self.food:
                self.score += 1
                self.food = self.spawn_food()
            else:
                self.snake.pop()

    def check_win(self):
        return len(self.snake) == self.width * self.height




if __name__ == "__main__":
    width = int(input("Enter the width of the game board (5 to 25): "))
    height = int(input("Enter the height of the game board (5 to 25): "))
    player_name = input("Enter your name: ")
    game = Game(width, height, player_name)
    game.run()

