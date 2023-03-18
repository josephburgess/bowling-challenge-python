import unittest
from unittest.mock import MagicMock, patch
from app import Application


class TestApplication(unittest.TestCase):
    @patch("app.application.Game")
    @patch("app.application.Frame")
    def test_run(self, mock_Frame, mock_Game):
        mock_input_values = ["5", "2"] * 10

        with patch("builtins.input", side_effect=mock_input_values):
            mock_game_instance = MagicMock()
            mock_game_instance.frame_count = 10
            mock_game_instance.calculate_grand_total.return_value = 70
            mock_frame_instance = MagicMock()
            mock_Game.return_value = mock_game_instance
            mock_Frame.return_value = mock_frame_instance
            mock_game_instance.scorecard = [mock_frame_instance] * 10
            app = Application()
            with patch("builtins.print") as mock_print:
                app.run()
                assert len(app.UI.game.scorecard) == 10
                assert app.UI.game.calculate_grand_total() == 70
                mock_print.assert_any_call("Your total score is: 70")


if __name__ == "__main__":
    unittest.main()
