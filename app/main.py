from fastapi import FastAPI
import uvicorn

from app.api.router import api_router


def get_app() -> FastAPI:
    app = FastAPI(docs_url="/api/docs")
    app.include_router(api_router)

    return app


if __name__ == "__main__":
    uvicorn.run("app.main:get_app", factory=True)
