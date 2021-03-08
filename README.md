# Operacion Fuego de Quasar
### https://arielaranda-fuego-de-quasar.herokuapp.com/

Build Status: [![Build Status](https://travis-ci.com/Zhinon/fuego-de-quasar.svg?branch=main)](https://travis-ci.com/Zhinon/fuego-de-quasar)

Coverage: [![Coverage Status](https://coveralls.io/repos/github/Zhinon/fuego-de-quasar/badge.svg?branch=main)](https://coveralls.io/github/Zhinon/fuego-de-quasar?branch=main)

Proyecto creado para el desafio de Mercado Libre.
## Tecnologias usadas

- Python 3.8
- Fastapi
- Pydantic
- Pytest
- Travis
- Coveralls
- Heroku

## Instalación local

Para ejecutar la web de forma local es necesario tener python 3.8 instalado y recomiendo utilizar un ambiente virtual para la instalacion de los `requirements`
_Para la creacion de ambientes virtuales se puede usar [venv](https://docs.python.org/3/library/venv.html#module-venv) o [virtualenv](https://pypi.org/project/virtualenv/)_
1. Clonar el repo:
```sh
mkdir mkdir ~/fuego
cd ~/fuego
git clone https://github.com/Zhinon/fuego-de-quasar.git
cd fuego-de-quasar
```
2. Instalar requirements
```sh
pip install -r requirements.txt
```
3. Correr servidor
```sh
uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
```
4. Una vez que este corriendo el servidor, ya se puede ingresar a [la pagina](http://0.0.0.0:5000)

## Correr test

- Simplemente se pueden correr haciendo:
```sh
pytest
```
- O para ver el coverage report se pueden correr haciendo:
```sh
coverage run -m pytest
coverage report
```

## Documentación de APIs
Toda documentacion de las APIs pueden ser encontradas en la misma pagina:
- Docs: https://arielaranda-fuego-de-quasar.herokuapp.com/docs
- Recod: https://arielaranda-fuego-de-quasar.herokuapp.com/redoc
