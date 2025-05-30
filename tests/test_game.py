import pytest
from src.game import Game

# test initialization of the game with correct dimensions
def test_game_initialization():
    game = Game(10, 10, "Tester")
    assert game.width == 10 and game.height == 10, "Game dimensions should initialize correctly."

# test if the snake starts in the middle of the board
def test_snake_initial_position():
    game = Game(10, 10, "Tester")
    expected_position = [(5, 5)]
    assert game.snake == expected_position, "Snake should start in the center of the board."

# test food spawning not on the snake
def test_food_not_on_snake():
    game = Game(10, 10, "Tester")
    assert game.food not in game.snake, "Food should not spawn on the snake."

# test snake movement
def test_snake_movement():
    game = Game(10, 10, "Tester")
    initial_head = game.snake[0]
    game.move_snake('RIGHT')
    assert game.snake[0] == (initial_head[0] + 1, initial_head[1]), "Snake should move right correctly."

# test snake collision with walls
def test_snake_collision_with_wall():
    game = Game(5, 5, "Tester")
    # move snake directly into the wall
    game.snake = [(0, 0)]
    game.move_snake('LEFT')
    assert game.game_over, "Game should end when the snake hits a wall."

# test snake eating food
def test_snake_eating_food():
    game = Game(10, 10, "Tester")
    initial_length = len(game.snake)
    game.food = (game.snake[0][0] + 1, game.snake[0][1])  # place food to the right of the head
    game.move_snake('RIGHT')
    assert len(game.snake) == initial_length + 1, "Snake should grow after eating food."


# test game over by snake running into itself
def test_snake_collision_with_self():
    game = Game(10, 10, "Tester")
    game.snake = [
        (5, 2),  # Head of the snake
        (5, 4),
        (5, 3),
        (5, 2)
    ]
    # move the snake down into itself
    game.move_snake("DOWN")

    assert game.game_over, "The game should end when the snake runs into itself."
