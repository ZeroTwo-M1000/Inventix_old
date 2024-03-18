import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from core.config import config

media_router = APIRouter()


@media_router.get("/{file_name}", response_class=FileResponse)
async def media(file_name):
    if os.path.exists(config.PROJECT_ROOT_DIR + "/media/" + file_name):
        return FileResponse(
            config.PROJECT_ROOT_DIR + "/media/" + file_name, filename=file_name
        )
    else:
        raise HTTPException(status_code=404)
