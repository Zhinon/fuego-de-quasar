from app.models.ship import Ship


INITIAL_SHIPS = [
    {
        'name': 'kenobi',
        'position': {'x': -500, 'y': -200},
    },
    {
        'name': 'skaywalker',
        'position': {'x': 100, 'y': -100},
    },
    {
        'name': 'sato',
        'position': {'x': 500, 'y': 100},
    },
]

SHIPS_OBJECTS = [Ship(**ship) for ship in INITIAL_SHIPS]
