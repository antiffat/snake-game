import pytest
from src.game import Game

# test initialization of the game with correct dimensions
def test_game_initialization():
    game = Game(10, 10, "Tester")
    assert game.width == 10 and game.height == 10, "Game dimensions should initialize correctly."
