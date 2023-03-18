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

spare_bonus_frame = Mock(
    get_first=lambda: 5,
    get_second=lambda: 5,
    get_third=lambda: 5,
    get_total=lambda: 15,
    is_strike=lambda: False,
    is_spare=lambda: True,
)
