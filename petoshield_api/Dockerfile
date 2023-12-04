FROM python:3.11.4-slim-buster

WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt
RUN python3 -m manage collectstatic
