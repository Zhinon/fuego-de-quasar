from fastapi import HTTPException

from app.actions.base import BaseAction
from app.constants.constants import SHIPS_OBJECTS
from app.models.ship import MessageRecieved
from app.utils import (
    location_utils,
    message_utils,
    ship_utils,
 )

class GetCoordsAndMessageAction(BaseAction):

    def validate(self, *args, **kwargs):
        self.ships_info = {}
        request_dict = kwargs['request'].dict()
        for ship_message in request_dict['satellites']:
            self.ships_info[ship_message['name']] = ship_message
        import ipdb; ipdb.set_trace()
        if len(self.ships_info) != 3:
            raise HTTPException(status_code=422, detail="Request validation error")

    def _run(self, *args, **kwargs):
        kenobi_ship = SHIPS_OBJECTS[0]
        skywalker_ship = SHIPS_OBJECTS[1]
        sato_ship = SHIPS_OBJECTS[2]

        try:
            position_x, position_y = location_utils.get_location([
                (
                    kenobi_ship.position.x,
                    kenobi_ship.position.y,
                    self.ships_info['kenobi']['distance'],
                ),
                (
                    skywalker_ship.position.x,
                    skywalker_ship.position.y,
                    self.ships_info['skywalker']['distance'],
                ),
                (
                    sato_ship.position.x,
                    sato_ship.position.y,
                    self.ships_info['sato']['distance'],
                )
            ])
            message = message_utils.get_message([
                self.ships_info['kenobi']['message'],
                self.ships_info['skywalker']['message'],
                self.ships_info['sato']['message'],
            ])
        except Exception:
            raise HTTPException(status_code=404, detail="Couldn't figure out the location or the message")

        ships_utils.update_ships(self.ships_info)

        return {
            'position': { 'x': position_x, 'y': position_y},
            'message': message,
        }
