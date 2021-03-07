import pytest

from app.utils.location_utils import get_message_origin


class TestLocationUtils:

    def test_get_message_origin_with_correct_points(self):
        expected_point = (0, 0)

        result = get_message_origin([(-1, 0, 1), (0, -2, 2), (3, 0, 3)])

        assert result == expected_point

    def test_get_message_origin_with_incorrect_points(self):
        with pytest.raises(Exception):
            get_message_origin([(-500, -200, 100), (100, -100, 115.5), (500, 100, 142.7)])
