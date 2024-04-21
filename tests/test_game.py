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

