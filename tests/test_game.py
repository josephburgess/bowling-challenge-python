import pytest
from app import Game
from tests.mock_frames import (
    open_frame,
    spare_frame,
    strike_frame,
    spare_bonus_frame,
    perfect_final_frame,
)


class TestGame:
    def test_add_frame_to_scorecard(self):
        game = Game()
        game.add(open_frame)
        assert game.scorecard == [open_frame]

    def test_calculate_without_bonuses(self):
        game = Game()
        for _ in range(10):
            game.add(open_frame)
        assert game.calculate_face_value() == 70

    def test_calculate_spare_bonuses(self):
        game = Game()
        for _ in range(5):
            game.add(spare_frame)
            game.add(open_frame)
        assert game.calculate_spares() == 15

    def test_calculate_strikes_preceding_open_frames(self):
        game = Game()
        for _ in range(5):
            game.add(strike_frame)
            game.add(open_frame)
        assert game.calculate_strikes() == 35

    def test_calculate_strikes_following_strikes(self):
        game = Game()
        for _ in range(2):
            game.add(strike_frame)
            game.add(strike_frame)
            game.add(open_frame)
            game.add(open_frame)
            game.add(open_frame)
        assert game.calculate_strikes() == 40

    def test_perfect_game(self):
        game = Game()
        for _ in range(9):
            game.add(strike_frame)
        game.add(perfect_final_frame)
        assert game.calculate_grand_total() == 300

    def test_spare_final_frame(self):
        game = Game()
        for _ in range(2):
            game.add(strike_frame)
            game.add(strike_frame)
            game.add(open_frame)
            game.add(open_frame)
        game.add(open_frame)
        game.add(spare_bonus_frame)
        assert game.calculate_grand_total() == 130

    def test_only_open_frames(self):
        game = Game()
        for _ in range(10):
            game.add(open_frame)
        assert game.calculate_grand_total() == 70

    def test_only_spare_frames(self):
        game = Game()
        for _ in range(9):
            game.add(spare_frame)
        game.add(spare_bonus_frame)
        assert game.calculate_grand_total() == 150

    def test_alternating_strike_and_open_frames(self):
        game = Game()
        for _ in range(5):
            game.add(strike_frame)
            game.add(open_frame)
        assert game.calculate_grand_total() == 120

    def test_alternating_spare_and_open_frames(self):
        game = Game()
        for _ in range(5):
            game.add(spare_frame)
            game.add(open_frame)
        assert game.calculate_grand_total() == 100

    def test_single_strike_frame(self):
        game = Game()
        game.add(strike_frame)
        for _ in range(9):
            game.add(open_frame)
        assert game.calculate_grand_total() == 80
