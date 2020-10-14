# TO-DO LIST WITH FASTAPI + MONGODB

![version](https://img.shields.io/badge/version-0.0.1-blue.svg?maxAge=2592000)

Este projeto é um backend do mundo real baseado em fastapi + mongodb. Ele pode ser usado como um back-end de amostra ou um projeto fastapi ou de amostra com mongodb.

O FastApi foi construído para criar apis para servir modelos de Machine Leaarning, com isso para analises é utilizado Gensim.

## Começo rápido (Quickstart)

Executar testes:
``` $ docker-compose exec web pytest . ```

Para executar:
``` $ ipython -i test.py ``` ou ``` $ python3 -i test.py ```

Caso precise achar o PATH do Pipenv: 
``` $ pipenv --venv ```

Rodar o servidor uvicorn: 
``` $ uvicorn main:app --reload ```

Para executar o aplicativo da web em depuração, use:
``` $ uvicorn app.main:app --reload ```

Em seguida, crie o .env arquivo (ou renomeie e modifique .env) na raiz do projeto e defina as variáveis ​​de ambiente para o aplicativo:
```
touch .env
echo "PROJECT_NAME=FastAPI" >> .env
echo DATABASE_URL=mongo://$MONGO_USER:$MONGO_PASSWORD@$MONGO_HOST:$MONGO_PORT/$MONGO_DB >> .env
echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env
```

***

## Implantação com Docker

Você deve ter dockere docker-composeferramentas instaladas para trabalho com material nesta seção. Primeiro, crie o .envarquivo como na seção Quickstart ou modifique .env.example. MONGO_HOSTdeve ser especificado como db ou modificado docker-compose.ymltambém. Depois é só executar:
``` docker-compose up -d ```

O aplicativo estará disponível em localhostou 127.0.0.1 em seu navegador.

***

## Estrutura do projeto
Os arquivos relacionados ao aplicativo estão no appdiretório. alembicé um diretório com migrações sql. As partes do aplicativo são:
```
neumann/
├── app/ = API e documentação
│   ├── api/
│   │   ├── api_v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── gensim.py
│   │   │   │   ├── notes.py
│   │   │   │   └── users.py
│   │   │   │
│   │   │   ├── __init__.py
│   │   │   └── api.py
│   │   │
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
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
│   ├── conftest.py
│   ├── notes.py
│   ├── ping.py
│   ├── users.py
│   └── analysis.py
│
├── .dockerignore
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── start_server.py
```

***

## Rotas da web

Todas as rotas estão disponíveis em ```/docs``` ou ```/redoc```, caminhos com Swagger* ou ReDoc.

- [Documentation](http://localhost:8000/docs)
- [Documentation](http://localhost:8000/redoc)

*[Swagger](https://swagger.io/) - O Swagger é uma estrutura de software de código aberto apoiada por um grande ecossistema de ferramentas que ajuda os desenvolvedores a projetar, criar, documentar e consumir serviços da Web RESTful.

***

## Referências

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Pypi FastAPI](https://pypi.org/project/fastapi/)
- [Github FastAPI](https://github.com/tiangolo/fastapi)
- [FastAPI + Vue.JS — Integração Python/JavaScript](https://medium.com/@marciobbarbosa/fastapi-vue-js-integra%C3%A7%C3%A3o-python-javascript-ddab7e6905a4)
- [Pydantic Field Types](https://pydantic-docs.helpmanual.io/usage/types/)
- [Python Shallow Copy and Deep Copy](https://www.programiz.com/python-programming/shallow-deep-copy)
- [HTTPX Requests Compatibility Guide](https://www.python-httpx.org/compatibility/)
- [Sphinx Python Documentation Generation](https://www.sphinx-doc.org/en/master/index.html)
- [Pytest - Monkeypatching/mocking modules and environments](https://docs.pytest.org/en/latest/monkeypatch.html)
- [Pypi - Find, install and publish Python packages with the Python Package Index](https://pypi.org/)
- [Python libraries to make your code readable, reliable and maintainable](https://dev.to/likid_geimfari/python-libraries-to-make-your-code-readable-reliable-and-maintainable-3p9l)
- [mypy](http://mypy-lang.org/)
- [Python 3 - 6. Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html)

MONGO
- [MongoDB + mongo-express + docker-compose](https://medium.com/@renato.groffe/mongodb-mongo-express-docker-compose-montando-rapidamente-um-ambiente-para-uso-824f25ca6957)
- [Set up a MongoDB server with Docker](https://linuxhint.com/setup_mongodb_server_docker/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)

MÓDULE
- [More Itertools](https://github.com/more-itertools/more-itertools)

ORM
- [Pony Object-Relational Mapper](https://github.com/ponyorm/pony/)
- [peewee-async](https://github.com/05bit/peewee-async)
- [Gino](https://github.com/python-gino/gino)
- [Tortoise ORM](https://github.com/tortoise/tortoise-orm)
- [Motor](https://github.com/mongodb/motor/)

ANALYZE
- [requests-toolbelt](https://pypi.org/project/requests-toolbelt/)
- [nltk](https://github.com/nltk/nltk)
- [stanza](https://github.com/stanfordnlp/stanza)

HELP
- [Motor: Iterating Over Results](https://emptysqua.re/blog/motor-iterating-over-results/)
- [MotorCollection](https://motor.readthedocs.io/en/stable/api-tornado/motor_collection.html)
- [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Field Types](https://pydantic-docs.helpmanual.io/usage/types/)
- [markqiu](https://github.com/markqiu/fastapi-mongodb-realworld-example-app/tree/master/app)
- [Tutorial: Using Motor With asyncio](https://motor.readthedocs.io/en/stable/tutorial-asyncio.html?highlight=to_list#querying-for-more-than-one-document)

APPLY
- [todo.txt format](https://github.com/todotxt/todo.txt)
- [Notes App](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Notes-App.md)
- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [Projeto de APIs RESTful com NodeJS e Restify](https://code.tutsplus.com/pt/tutorials/restful-api-design-with-nodejs-restify--cms-22637)
- [Desenvolvendo e testando uma API assíncrona com FastAPI e Pytest](https://testdriven.io/blog/fastapi-crud/#routes)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [HTTPie](https://httpie.org/)
- [Introduction to ASGI: Emergence of an Async Python Web Ecosystem](https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/)
- [Docker for Python Developers](https://mherman.org/presentations/dockercon-2018/#1)
- [Find, install and publish Python packages with the Python Package Index](https://pypi.org/)
- [Tutorial básico de SQLAlchemy](https://leportella.com/tutorial-basico-sqlalchemy.html)
- [Tipos de coluna e dados](https://docs.sqlalchemy.org/en/13/core/type_basics.html)

STUDY
- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
- [Sibling package imports](https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944)
- [Usando anotações de tipo do Python](https://dev.to/dstarner/using-pythons-type-annotations-4cfe#:~:text=Type%20Annotations%20are%20a%20new,to%20the%20dynamically%20typed%20Python.)
- [Dicas para digitar dicas (Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Verificação de tipo Python (Guia)](https://realpython.com/python-type-checking/)
- [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- [Gensim Core Concepts](https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html)
- [The troublesome "Active Record" pattern](http://calpaterson.com/activerecord.html)
- [Standardizing the World of Machine Learning Web Service APIs](https://www.kdnuggets.com/2015/07/psi-machine-learning-web-service-apis.html)
- [Protocols and Structures for Inference](https://www.google.com/search?q=Protocols+and+Structures+for+Inference&oq=Protocols+and+Structures+for+Inference&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8)
- [Protocols and Structures for Inference: A RESTful API for Machine Learning](http://proceedings.mlr.press/v50/montgomery15.pdf)

TEST
- [expressive_regex](https://github.com/fsadannn/expressive_regex)
- [more-itertools](https://pypi.org/project/more-itertools/)

IMPLEMENT
- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)
- [Funções em Python: entendendo parâmetros, argumentos, *args e **kwargs](https://medium.com/luizalabs/fun%C3%A7%C3%B5es-em-python-entendendo-par%C3%A2metros-argumentos-args-e-kwargs-4291b1f817f6)

***

## NOTAS PARA TESTE

tarefas domésticas

lavar a louça
secar a louça
lavar a roupa
passar a roupa
lavar o banheiro
recolher o lixo
limpar o quintal
limpar a geladeira
limpar o fogão

tarefas escolares
fazer o trabalho de história
fazer os exercicios de matemática
prova de português

tarefas de trabalho
entregar o relatório mensal
reunião com o cliente

tarefas do veículo
trocar o óleo
trocar as pastilhas de freio

***
