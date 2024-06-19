FROM nikolaik/python-nodejs:python3.11-nodejs20-slim

ARG SOURCES_DIR="src/"
ARG POETRY_VERSION=1.8.2

ENV PROJECT_VERSION=0.0.1

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN set -ex \
    && apt-get update
COPY pyproject.toml poetry.lock ./
ARG POETRY_GROUP=main
RUN set -ex \
    && npm install -g nodemon \
    && pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && pip install setuptools==68.1.2
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction
RUN rm -rf /root/.cache

WORKDIR /code

COPY ${SOURCES_DIR} /code/
