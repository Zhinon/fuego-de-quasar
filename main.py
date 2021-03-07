from fastapi import FastAPI
from app.actions.schemas.schemas import (
    TopSecretRequestSchema,
    ResponseSchema,
)
from app.actions.server import ACTIONS_MAP


app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello world'}

@app.post('/topsecret/', response_model=ResponseSchema)
def topsecret(request: TopSecretRequestSchema):
    return ACTIONS_MAP['post_get_coords_and_message']().run(request)
