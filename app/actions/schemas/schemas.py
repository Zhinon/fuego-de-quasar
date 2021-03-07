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

    class Config:
        schema_extra = {
            'example' : {
                "satellites": [
                    {
                        "name": "kenobi",
                        "distance": 103.14,
                        "message": [" ", "es", " ", "mensaje"],
                    },
                    {
                        "name": "skywalker",
                        "distance": 53.27,
                        "message": ["Este", " ", " ", "mensaje"],
                    },
                    {
                        "name": "sato",
                        "distance": 82.89,
                        "message": [" ", " ", "un", "mensaje"],
                    },
                ]
            }
        }

class PositionSchema(BaseModel):
    x: float
    y: float

class ResponseSchema(BaseModel):
    position: PositionSchema
    message: str

    class Config:
        schema_extra = {
            'example': {
                'position': {
                    'x': -100,
                    'y': 75.5,
                },
                'message': 'Este es un mensaje',
            }
        }
