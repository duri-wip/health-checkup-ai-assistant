import uvicorn
from fastapi import FastAPI

from src.routers import routers


def application() -> FastAPI:
    app = FastAPI(name="Sagak-Agent-Application")

    for router in routers:
        app.include_router(router)
    return app


def main():
    app = application()
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()