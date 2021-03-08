from pydantic import BaseModel
from typing import (
    Optional,
    List,
)
from typing_extensions import Literal


class Position(BaseModel):
    x: float
    y: float


class MessageRecieved(BaseModel):
    message: Optional[List[str]]
    message_distance: Optional[float]


class Ship(BaseModel):
    name: Literal['kenobi', 'skywalker', 'sato']
    position: Position
    last_message_received: Optional[MessageRecieved] = None
