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

## Web routes

All routes are available in ``` /docs ``` or ``` /redoc ```, paths with Swagger* or ReDoc.

- [Documentation docs](http://localhost:8000/docs)
- [Documentation redoc](http://localhost:8000/redoc)

*[Swagger](https://swagger.io/) - Swagger is an open source software framework supported by a large ecosystem of tools that helps developers design, create, document and consume RESTful web services.

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
