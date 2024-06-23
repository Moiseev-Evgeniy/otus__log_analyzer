FROM python:3.12-slim

WORKDIR /opt/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends

RUN pip install poetry==1.7.1

COPY pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install

RUN apt-get install make

COPY src src
COPY tests tests
COPY log_analyzer.py .
COPY makefile .

CMD ["sleep", "infinity"]
