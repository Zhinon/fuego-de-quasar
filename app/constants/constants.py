from app.models.ship import Ship


INITIAL_SHIPS = [
    {
        'name': 'kenobi',
        'position': {'x': -500, 'y': -200},
    },
    {
        'name': 'skywalker',
        'position': {'x': 100, 'y': -100},
    },
    {
        'name': 'sato',
        'position': {'x': 500, 'y': 100},
    },
]

SHIPS_OBJECTS = [Ship(**ship) for ship in INITIAL_SHIPS]

SHIPS_MAP = {
    'kenobi': SHIPS_OBJECTS[0],
    'skywalker': SHIPS_OBJECTS[1],
    'sato': SHIPS_OBJECTS[2],
}