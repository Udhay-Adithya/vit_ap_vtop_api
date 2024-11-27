# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.5

FROM python:${PYTHON_VERSION}-slim

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt gunicorn

COPY . .

EXPOSE 8080

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app