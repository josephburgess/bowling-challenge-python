import pytest
from app.frame import Frame

frame = Frame(10, 3, 4)
open_frame = Frame(8, 1, 0)
spare_frame = Frame(5, 5, 0)


def test_frame_rolls():
    assert frame.first == 10
    assert frame.second == 3
    assert frame.third == 4


def test_frame_get_first():
    assert frame.get_first() == 10


def test_frame_get_second():
    assert frame.get_second() == 3


def test_frame_get_third():
    assert frame.get_third() == 4


def test_frame_get_total():
    assert frame.get_total() == 17
    assert open_frame.get_total() == 9
    assert spare_frame.get_total() == 10
