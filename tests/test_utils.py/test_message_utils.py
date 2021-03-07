import pytest

from app.utils.message_utils import get_message


class TestMessageUtils:

    def test_get_message_with_correct_messages(self):
        expected_msg = 'Este es un mensaje'

        result = get_message([
            ["Este", " ", " ", "mensaje"],
            [" ", " ", "es", " ", "mensaje"],
            [" ", " ", " ", " ", " ", "un", " "],
        ])

        assert result == expected_msg

    def test_get_message_unable_to_decode(self):
        with pytest.raises(Exception):
            get_message([
                ["Este", " ", " ", "mensaje"],
                [" ", " ", " ", " ", "mensaje"],
                [" ", " ", " ", " ", " ", "un", " "],
            ])
