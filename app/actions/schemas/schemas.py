from pydantic import (
    BaseModel,
    conlist,
)
from typing_extensions import Literal
from typing import List


class SatelliteSchema(BaseModel):
    name: Literal['kenobi', 'skywalker', 'sato']
    distance: float
    message: List[str]

class TopSecretRequestSchema(BaseModel):
    satellites: conlist(SatelliteSchema, min_items=3, max_items=3)
