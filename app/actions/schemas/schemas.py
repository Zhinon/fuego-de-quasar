from typing import Literal, List
from pydantic import BaseModel, conlist

from app.constants.constants import SHIPNAMES


class SatelliteSchema(BaseModel):
    name: Literal['kenobi', 'skywalker', 'sato']
    distance: float
    message: List[str]

class TopSecretRequestSchema(BaseModel):
    satellites: conlist(SatelliteSchema, min_items=3, max_items=3)
