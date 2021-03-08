from app.constants.constants import SHIPS_OBJECTS
from app.models.ship import MessageRecieved


def update_ships(ship_info):
    kenobi_ship = SHIPS_OBJECTS[0]
    skywalker_ship = SHIPS_OBJECTS[1]
    sato_ship = SHIPS_OBJECTS[2]

    kenobi_ship.last_message_received = MessageRecieved(
        message=ships_info['kenobi']['message'],
        distance=ships_info['kenobi']['distance'],
    )
    skywalker_ship.last_message_received = MessageRecieved(
        message=ships_info['skywalker']['message'],
        distance=ships_info['skywalker']['distance'],
    )
    sato_ship.last_message_received = MessageRecieved(
        message=ships_info['sato']['message'],
        distance=ships_info['sato']['distance'],
    )