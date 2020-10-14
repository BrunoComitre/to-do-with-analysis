FROM python:3.8.5-slim-buster

# work directory
WORKDIR /usr/app

# Impede o Python grave arquivos pyc no disco(equivale à python -B option)
ENV PYTHONDONWRITEBYCODE 1

# Impede o Python armazene em buffer stdout e stderr(equivale à python -u option)
ENV PYTHONUNBUFFERED 1

COPY ./requirements/ /usr/requirements/

COPY ./requirements.txt /usr/requirements.txt

RUN apt-get update \
    && pip install -r /usr/requirements.txt

COPY . /usr/app/

CMD gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0
