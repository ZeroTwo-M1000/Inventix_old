from typing import Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class OkResponse(BaseModel):
    success: Optional[bool] = True
    message: Optional[str] = "OK"
    data: Optional[T] = None


class ErrorResponse(BaseModel):
    success: Optional[bool] = False
    message: str
