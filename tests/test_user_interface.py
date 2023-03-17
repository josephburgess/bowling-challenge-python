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
        self.assertEqual(roll_one, 5)
