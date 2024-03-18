from fastapi import APIRouter
from fastapi.responses import FileResponse

client_router = APIRouter()


@client_router.get("/{full_path:path}")
async def other(full_path: str):
    if not full_path.startswith("api") and not full_path.startswith("media"):
        return FileResponse("build/index.html")
