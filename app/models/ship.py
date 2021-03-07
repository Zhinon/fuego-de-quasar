from pydantic import BaseModel
from typing import (
    Optional,
    List,
)


class Position(BaseModel):
    x: float
    y: float

class Ship(BaseModel):
    name: Literal['kenobi', 'skywalker', 'sato']
    position: Position
    current_message: Optional[List[str]]
    current_distance_message: Optional[float]
