# syntax=docker/dockerfile:1

# Dockerfile, Image, Container

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

# RUN pip install flask pytest
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP=market.py

CMD [ "python3", "market.py"]


# build -> docker build -t name .
# run -> docker run -p 8000:8000 name
#see -> localhost