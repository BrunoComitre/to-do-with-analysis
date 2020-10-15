# TO-DO LIST WITH FASTAPI + MONGODB
<br />

![version](https://img.shields.io/badge/version-0.0.1-blue.svg?maxAge=2592000)

This is a real-world backend project based on FastApi + MongoDB. It can be used as a CRUD sample backend or a FastApi or MongoDB sample project.

FastApi was built to create apis to serve Machine Learning models, with that it is used for analysis [Gensim](https://radimrehurek.com/gensim/).

***
<br />

## Quickstart

Run test:
``` $ docker-compose exec web pytest . ```

To execute:
``` $ ipython -i test.py ``` or ``` $ python3 -i test.py ```

If you need to find the Pipenv PATH:
``` $ pipenv --venv ```

Run the uvicorn server:
``` $ uvicorn main:app --reload ```

To run the debugging web application, use:
``` $ uvicorn app.main:app --reload ```

Then, create the .env file (or rename and modify .env) at the root of the project and set the environment variables for the application:

```
touch .env
echo "PROJECT_NAME=FastAPI" >> .env
echo DATABASE_URL=mongo://$MONGO_USER:$MONGO_PASSWORD@$MONGO_HOST:$MONGO_PORT/$MONGO_DB >> .env
echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env
```

***
<br />

## Deploy with Docker

You must have docker and docker-compose tools installed to work with material in this section. First, create the .env file as in the Quickstart section or modify .env example MONGO_HOST must be specified as db or modified docker-compose.yml. Then just run:
``` docker-compose up -d ```

The application will be available on localhost 127.0.0.1 in your browser.

***
<br />

## Project structure

The application-related files are in the app directory. The parts of the application are:

```
todo-fastapi-mongodb/
├── app/
│   ├── api/
│   │   ├── api_v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── gensim.py
│   │   │   │   ├── login.py
│   │   │   │   ├── notes.py
│   │   │   │   ├── users.py
│   │   │   │   └── utils.py
│   │   │   │
│   │   │   ├── __init__.py
│   │   │   └── api.py
│   │   │
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── errors.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── mongodb_utils.py
│   │   └── mongodb.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── gensim.py
│   │   ├── notes.py
│   │   ├── token.py
│   │   └── users.py
│   │
│   ├── payloads/
│   │   ├── __init__.py
│   │   ├── gensim.py
│   │   ├── notes.py
│   │   ├── query_builder.py
│   │   └── users.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── insomnia_tests/
│   └── insomnia_collection.json
│
├── requirements/
│   ├── analyze.txt
│   ├── dev.txt
│   └── test.txt
│
├── tests/
│   ├── __init__.py
│   ├── analysis.py
│   ├── conftest.py
│   ├── notes.py
│   ├── ping.py
│   └── users.py
│
├── .dockerignore
├── .env
├── .gitignore
├── CHANGELOG.md
├── docker-compose.yml
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
├── ROADMAP.md
└── start_server.py
```

***
<br />

## Web routes

All routes are available in ``` /docs ``` or ``` /redoc ```, paths with Swagger* or ReDoc.

- [Documentation docs](http://localhost:8000/docs)
- [Documentation redoc](http://localhost:8000/redoc)

*[Swagger](https://swagger.io/) - Swagger is an open source software framework supported by a large ecosystem of tools that helps developers design, create, document and consume RESTful web services.

***
<br />

## References

- [MAIN] [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [MAIN] [Pypi FastAPI](https://pypi.org/project/fastapi/)
- [MAIN] [Github FastAPI](https://github.com/tiangolo/fastapi)
- [MAIN] [FastAPI + Vue.JS — Integração Python/JavaScript](https://medium.com/@marciobbarbosa/fastapi-vue-js-integra%C3%A7%C3%A3o-python-javascript-ddab7e6905a4)
- [MAIN] [Pydantic Field Types](https://pydantic-docs.helpmanual.io/usage/types/)
- [MAIN] [Python Shallow Copy and Deep Copy](https://www.programiz.com/python-programming/shallow-deep-copy)
- [MAIN] [HTTPX Requests Compatibility Guide](https://www.python-httpx.org/compatibility/)
- [MAIN] [Sphinx Python Documentation Generation](https://www.sphinx-doc.org/en/master/index.html)
- [MAIN] [Pytest - Monkeypatching/mocking modules and environments](https://docs.pytest.org/en/latest/monkeypatch.html)
- [MAIN] [Pypi - Find, install and publish Python packages with the Python Package Index](https://pypi.org/)
- [MAIN] [Python libraries to make your code readable, reliable and maintainable](https://dev.to/likid_geimfari/python-libraries-to-make-your-code-readable-reliable-and-maintainable-3p9l)
- [MAIN] [mypy](http://mypy-lang.org/)
- [MAIN] [Python 3 - 6. Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html)
- [MONGO] [MongoDB + mongo-express + docker-compose](https://medium.com/@renato.groffe/mongodb-mongo-express-docker-compose-montando-rapidamente-um-ambiente-para-uso-824f25ca6957)
- [MONGO] [Set up a MongoDB server with Docker](https://linuxhint.com/setup_mongodb_server_docker/)
- [MONGO] [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [MÓDULE] [More Itertools](https://github.com/more-itertools/more-itertools)
- [ORM] [Pony Object-Relational Mapper](https://github.com/ponyorm/pony/)
- [ORM] [[peewee-async](https://github.com/05bit/peewee-async)
- [ORM] [[Gino](https://github.com/python-gino/gino)
- [ORM] [[Tortoise ORM](https://github.com/tortoise/tortoise-orm)
- [ORM] [[Motor](https://github.com/mongodb/motor/)
- [ANALYZE] [requests-toolbelt](https://pypi.org/project/requests-toolbelt/)
- [ANALYZE] [nltk](https://github.com/nltk/nltk)
- [ANALYZE] [stanza](https://github.com/stanfordnlp/stanza)
- [HELP] [Motor: Iterating Over Results](https://emptysqua.re/blog/motor-iterating-over-results/)
- [HELP] [MotorCollection](https://motor.readthedocs.io/en/stable/api-tornado/motor_collection.html)
- [HELP] [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [HELP] [Field Types](https://pydantic-docs.helpmanual.io/usage/types/)
- [HELP] [markqiu](https://github.com/markqiu/fastapi-mongodb-realworld-example-app/tree/master/app)
- [HELP] [Tutorial: Using Motor With asyncio](https://motor.readthedocs.io/en/stable/tutorial-asyncio.html?highlight=to_list#querying-for-more-than-one-document)
- [APPLY] [todo.txt format](https://github.com/todotxt/todo.txt)
- [APPLY] [Notes App](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Notes-App.md)
- [APPLY] [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [APPLY] [Projeto de APIs RESTful com NodeJS e Restify](https://code.tutsplus.com/pt/tutorials/restful-api-design-with-nodejs-restify--cms-22637)
- [APPLY] [Desenvolvendo e testando uma API assíncrona com FastAPI e Pytest](https://testdriven.io/blog/fastapi-crud/#routes)
- [APPLY] [Pydantic](https://pydantic-docs.helpmanual.io/)
- [APPLY] [HTTPie](https://httpie.org/)
- [APPLY] [Introduction to ASGI: Emergence of an Async Python Web Ecosystem](https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/)
- [APPLY] [Docker for Python Developers](https://mherman.org/presentations/dockercon-2018/#1)
- [APPLY] [Find, install and publish Python packages with the Python Package Index](https://pypi.org/)
- [APPLY] [Tutorial básico de SQLAlchemy](https://leportella.com/tutorial-basico-sqlalchemy.html)
- [APPLY] [Tipos de coluna e dados](https://docs.sqlalchemy.org/en/13/core/type_basics.html)
- [STUDY] [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
- [STUDY] [Sibling package imports](https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944)
- [STUDY] [Usando anotações de tipo do Python](https://dev.to/dstarner/using-pythons-type-annotations-4cfe#:~:text=Type%20Annotations%20are%20a%20new,to%20the%20dynamically%20typed%20Python.)
- [STUDY] [Dicas para digitar dicas (Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [STUDY] [Verificação de tipo Python (Guia)](https://realpython.com/python-type-checking/)
- [STUDY] [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- [STUDY] [Gensim Core Concepts](https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html)
- [STUDY] [The troublesome "Active Record" pattern](http://calpaterson.com/activerecord.html)
- [STUDY] [Standardizing the World of Machine Learning Web Service APIs](https://www.kdnuggets.com/2015/07/psi-machine-learning-web-service-apis.html)
- [STUDY] [Protocols and Structures for Inference](https://www.google.com/search?q=Protocols+and+Structures+for+Inference&oq=Protocols+and+Structures+for+Inference&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8)
- [STUDY] [Protocols and Structures for Inference: A RESTful API for Machine Learning](http://proceedings.mlr.press/v50/montgomery15.pdf)
- [TEST] [expressive_regex](https://github.com/fsadannn/expressive_regex)
- [TEST] [more-itertools](https://pypi.org/project/more-itertools/)
- [IMPLEMENT] [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)
- [IMPLEMENT] [Funções em Python: entendendo parâmetros, argumentos, *args e **kwargs](https://medium.com/luizalabs/fun%C3%A7%C3%B5es-em-python-entendendo-par%C3%A2metros-argumentos-args-e-kwargs-4291b1f817f6)

***
<br />

## Sample test notes

housework

- wash the dishes
- dry the dishes
- washing
- ironing
- wash the bathroom
- get the garbage
- clean the yard
- clean the fridge
- clean the stove

school chores

- do history work
- do the math exercises
- portuguese test

work tasks

- deliver the monthly report
- meeting with the client

vehicle tasks

- change the oil
- change the brake pads

***
