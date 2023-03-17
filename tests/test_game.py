import pytest
from app.game import Game
from unittest.mock import Mock


open_frame = Mock(
    get_first=lambda: 3,
    get_second=lambda: 4,
    get_third=lambda: 0,
    get_total=lambda: 7,
    is_strike=lambda: False,
    is_spare=lambda: False,
)

spare_frame = Mock(
    get_first=lambda: 5,
    get_second=lambda: 5,
    get_third=lambda: 0,
    get_total=lambda: 10,
    is_strike=lambda: False,
    is_spare=lambda: True,
)

strike_frame = Mock(
    get_first=lambda: 10,
    get_second=lambda: 0,
    get_third=lambda: 0,
    get_total=lambda: 10,
    is_strike=lambda: True,
    is_spare=lambda: False,
)

perfect_final_frame = Mock(
    get_first=lambda: 10,
    get_second=lambda: 10,
    get_third=lambda: 10,
    get_total=lambda: 30,
    is_strike=lambda: True,
    is_spare=lambda: False,
)


def test_add_frame_to_scorecard():
    game = Game()
    game.add(open_frame)
    assert game.scorecard == [open_frame]


def test_calculate_without_bonuses():
    game = Game()
    for _ in range(10):
        game.add(open_frame)
    assert game.calculate_face_value() == 70


def test_calculate_spare_bonuses():
    game = Game()
    for _ in range(5):
        game.add(spare_frame)
        game.add(open_frame)
    assert game.calculate_spares() == 15


def test_calculate_strikes_preceding_open_frames():
    game = Game()
    for _ in range(5):
        game.add(strike_frame)
        game.add(open_frame)
    assert game.calculate_strikes() == 35


def test_calculate_strikes_following_strikes():
    game = Game()
    for _ in range(2):
        game.add(strike_frame)
        game.add(strike_frame)
        game.add(open_frame)
        game.add(open_frame)
        game.add(open_frame)
    assert game.calculate_strikes() == 40


def test_perfect_game():
    game = Game()
    for _ in range(9):
        game.add(strike_frame)
    game.add(perfect_final_frame)
    assert game.calculate_grand_total() == 300
