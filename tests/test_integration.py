import unittest
from unittest.mock import patch
from app import Application


class TestIntegration:
    @patch("builtins.print")
    @patch("builtins.input", side_effect=["10"] * 12)
    def test_full_game(self, mock_input, mock_print):
        app = Application()
        app.run()
        assert len(app.UI.game.scorecard) == 10
        assert app.UI.game.scorecard[0].is_strike() == True
        assert app.UI.game.calculate_grand_total() == 300
        mock_input.assert_called()
        mock_print.assert_any_call("Your total score is: 300")


if __name__ == "__main__":
    unittest.main()
