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


def test_add_frame_to_scorecard():
    game = Game()
    game.add(open_frame)
    assert game.scorecard == [open_frame]


def test_calculate_without_bonuses():
    game = Game()
    num = 10
    for _ in range(num):
        game.add(open_frame)
    assert game.calculate_face_value() == 70
