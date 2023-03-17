import unittest
from unittest.mock import Mock, patch
from app.user_interface import UserInterface
from app.game import Game


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.user_interface = UserInterface(self.game)

    @patch("builtins.input", side_effect=["5"])
    def test_get_roll_one(self, mock_input):
        roll_one = self.user_interface.get_roll_one()
        assert roll_one == 5

    @patch("builtins.input", side_effect=["5", "3"])
    def test_get_roll_two(self, mock_input):
        self.user_interface.get_roll_one()
        roll_two = self.user_interface.get_roll_two()
        assert roll_two == 3