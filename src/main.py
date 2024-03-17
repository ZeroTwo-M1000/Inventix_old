from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.config import config
from core.routers.api_routers import api_router
from core.routers.client_router import client_router
from core.routers.media_router import media_router


def init_app():
    app = FastAPI()

    app.mount("/assets", StaticFiles(directory="build/assets"), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    async def on_startup():
        await config.prisma_connection.connect()

    async def on_shutdown():
        await config.prisma_connection.disconnect()

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    app.include_router(api_router, prefix="/api")
    app.include_router(media_router, prefix="/media")
    app.include_router(client_router)

    return app


app = init_app()
