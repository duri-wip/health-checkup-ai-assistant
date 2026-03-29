FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-dev

COPY src/ ./src/

EXPOSE 8001

CMD ["uv", "run", "uvicorn", "src.app:application", "--factory", "--host", "0.0.0.0", "--port", "8001"]