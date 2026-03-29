FROM python:3.12-slim

# uv 설치
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# 의존성 먼저 복사 (레이어 캐시 활용)
COPY pyproject.toml uv.lock ./

# 의존성 설치 (가상환경 없이 시스템에 직접)
RUN uv sync --frozen --no-dev

# 소스 복사
COPY src/ ./src/

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.app:application", "--host", "0.0.0.0", "--port", "8000"]