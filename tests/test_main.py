from fastapi.testclient import TestClient
from main import app

def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        'Operacion': 'Fuego de Quasar',
        'Author': 'Ariel Aranda',
        'Api_Doc': 'https://arielaranda-fuego-de-quasar.herokuapp.com/docs',
        'Api_redoc': 'https://arielaranda-fuego-de-quasar.herokuapp.com/redoc',
        'Github_repo': 'https://github.com/Zhinon/fuego-de-quasar',
    }