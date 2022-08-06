# Central-Api

## Getting started

steps to raise the project

- create a .env file
- then compile the content of the example.dev into the file dev.env
- choose whether to raise it locally or with docker

the url of the proyect

in local is: [http://localhost:4000](http://localhost:4000)

### Docker

to raise the docker environment apply the following command to create the image:

`docker-compose build`

After generating the image, execute the following command

`docker-compose up`
    to see the process of lifting and see the logs of all the containers
o

`docker-compose up -d` to run in the background

to see the logs of a specific container use: `docker-compose logs -f central-api`

to access a specific container:
`docker exec -it central-api bash`

### Local

for local execution you only need to launch the following command:

- `python3 -m venv .venv` only the first time
- `source .venv/bin/active` to active de python env
- `pip install -r requirements.txt`
- `uvicorn server.src.server:app --port 4000 --reload`

### Resources

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [pymongo](https://pymongo.readthedocs.io/en/stable/index.html) is not the best doc
- [paydantic](https://pydantic-docs.helpmanual.io/) to type python
- [flake8](https://flake8.pycqa.org/en/latest/) style guide
- [black](https://pypi.org/project/black/) code formatt