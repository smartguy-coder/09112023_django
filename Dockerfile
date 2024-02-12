FROM python:3.11.6-alpine

WORKDIR /library

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install poetry

RUN apk add postgresql-client build-base postgresql-dev

COPY library /library
COPY poetry.lock pyproject.toml /library/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi



EXPOSE 8000