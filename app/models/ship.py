from pydantic import BaseModel
from typing import (
    Optional,
    List,
)
from app.constants.typing_helper import AllowedShipnames

class Position(BaseModel):
    x: float
    y: float


class MessageRecieved(BaseModel):
    message: Optional[List[str]]
    message_distance: Optional[float]


class Ship(BaseModel):
    name: AllowedShipnames
    position: Position
    last_message_received: Optional[MessageRecieved] = MessageRecieved()
