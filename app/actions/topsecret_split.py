from fastapi import HTTPException

from app.actions.base import BaseAction
from app.constants.constants import (
    SHIPS_OBJECTS,
    SHIPS_MAP,
)
from app.models.ship import MessageRecieved
from app.utils import (
    location_utils,
    message_utils,
    ship_utils,
 )

class GetCoordsAndMessageSplit(BaseAction):

    def validate(self, *args, **kwargs):
        for ship in SHIPS_OBJECTS:
            if not ship.last_message_received.message_distance or not ship.last_message_received.message:
                raise  HTTPException(status_code=404, detail="Couldn't figure out the location or the message")


    def _run(self, *args, **kwargs):
        kenobi_ship = SHIPS_OBJECTS[0]
        skywalker_ship = SHIPS_OBJECTS[1]
        sato_ship = SHIPS_OBJECTS[2]

        try:
            position_x, position_y = location_utils.get_location([
                (
                    kenobi_ship.position.x,
                    kenobi_ship.position.y,
                    kenobi_ship.last_message_received.message_distance,
                ),
                (
                    skywalker_ship.position.x,
                    skywalker_ship.position.y,
                    skywalker_ship.last_message_received.message_distance,
                ),
                (
                    sato_ship.position.x,
                    sato_ship.position.y,
                    sato_ship.last_message_received.message_distance,
                )
            ])
            message = message_utils.get_message([
                kenobi_ship.last_message_received.message,
                skywalker_ship.last_message_received.message,
                sato_ship.last_message_received.message,
            ])
        except Exception:
            raise HTTPException(status_code=404, detail="Couldn't figure out the location or the message")

        return {
            'position': { 'x': position_x, 'y': position_y},
            'message': message,
        }


class PostMessageAndDistanceSplit(BaseAction):

    def validate(self, *args, **kwargs):
        self.request_dict = kwargs['request'].dict()
        if self.request_dict['distance'] < 1:
            raise HTTPException(status_code=422, detail="Request validation error")

    def _run(self, *args, **kwargs):
        name = kwargs['satellite_name']
        ship = SHIPS_MAP.get(name)
        ship.last_message_received.message = self.request_dict['message']
        ship.last_message_received.message_distance = self.request_dict['distance']

        return {}
