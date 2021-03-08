from fastapi import FastAPI
from app.actions.schemas.schemas import (
    TopSecretRequestSchema,
    TopSecretSplitRequestSchema,
    ResponseSchema,
)
from app.actions.server import ACTIONS_MAP
from app.constants.typing_helper import AllowedShipnames


app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello world'}

@app.post('/topsecret/', response_model=ResponseSchema, responses={404: {}})
def topsecret(request: TopSecretRequestSchema):
    return ACTIONS_MAP['post_get_coords_and_message']().run(request=request)

@app.get('/topsecret_split/', response_model=ResponseSchema, responses={404: {}})
def topsecret_split_get():
    return ACTIONS_MAP['get_coords_and_message_split']().run()

@app.post('/topsecret_split/{satellite_name}')
def topsecret_split_post(satellite_name: AllowedShipnames, request: TopSecretSplitRequestSchema):
    return ACTIONS_MAP['post_message_and_distance_split']().run(satellite_name=satellite_name, request=request)
