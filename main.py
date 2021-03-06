from fastapi import FastAPI
from app.actions.schemas.schemas import TopSecretRequestSchema


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello world"}

@app.post("/topsecret/")
def topsecret(request: TopSecretRequestSchema):
    return request
