FROM python:3.12.5-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry
COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock
RUN poetry lock --no-update \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

COPY server /app/server
COPY core /app/core
COPY config.yml /app/config.yml
COPY _env/prod.env /app/.env


EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "server.app:app", "--workers", "1", "--host", "0.0.0.0", "--port", "8000", "--env-file", ".env"]
