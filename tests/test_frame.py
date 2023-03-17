import pytest
from app.frame import Frame

frame = Frame(10, 3, 4)


def test_frame_rolls():
    assert frame.first == 10
    assert frame.second == 3
    assert frame.third == 4
