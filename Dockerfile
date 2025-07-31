FROM ghcr.io/astral-sh/uv:python3.12-bookworm

RUN mkdir -p /app
WORKDIR /app
COPY uv.lock pyproject.toml .dlt /app/
ENV UV_INDEX=https://pypi.org/simple/
RUN uv sync --locked

