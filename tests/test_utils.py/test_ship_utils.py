from app.models.ship import Ship
from app.utils.ship_utils import update_ships
from app.constants.constants import (
    INITIAL_SHIPS,
    SHIPS_OBJECTS,
)

class TestShipUtils:

    def setup_method(self):
        SHIPS_OBJECTS = [Ship(**ship) for ship in INITIAL_SHIPS]

    def test_update_ships(self):
        ship_kenobi = SHIPS_OBJECTS[0]
        ship_skywalker = SHIPS_OBJECTS[1]
        ship_sato = SHIPS_OBJECTS[2]

        assert ship_kenobi.dict() == {
            'name': 'kenobi',
            'position': {'x': -500.0, 'y': -200.0},
            'last_message_received': {'message': None, 'message_distance': None},
        }
        assert ship_skywalker.dict() == {
            'name': 'skywalker',
            'position': {'x': 100.0, 'y': -100.0},
            'last_message_received': {'message': None, 'message_distance': None},
        }
        assert ship_sato.dict() == {
            'name': 'sato',
            'position': {'x': 500.0, 'y': 100.0},
            'last_message_received': {'message': None, 'message_distance': None},
        }

        update_data = {
            'kenobi': {'name': 'kenobi', 'distance': 10, 'message': [' ']},
            'skywalker': {'name': 'skywalker', 'distance': 20, 'message': ['']},
            'sato': {'name': 'sato', 'distance': 30, 'message': [' ']},
        }

        update_ships(update_data)

        assert ship_kenobi.dict() == SHIPS_OBJECTS[0].dict() == {
            'name': 'kenobi',
            'position': {'x': -500.0, 'y': -200.0},
            'last_message_received': {'message': [' '], 'message_distance': 10.0}
        }
        assert ship_skywalker.dict() == SHIPS_OBJECTS[1].dict() == {
            'name': 'skywalker',
            'position': {'x': 100.0, 'y': -100.0},
            'last_message_received': {'message': [''], 'message_distance': 20.0},
        }
        assert ship_sato.dict() == SHIPS_OBJECTS[2].dict() == {
            'name': 'sato',
            'position': {'x': 500.0, 'y': 100.0},
            'last_message_received': {'message': [' '], 'message_distance': 30.0},
        }
