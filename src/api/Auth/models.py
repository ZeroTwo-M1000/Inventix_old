from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    role: str


class CreateUser(BaseUser):
    hash_password: str
    img: Optional[str] = None


class LoginUser(BaseUser):
    password: str
    role: Optional[str] = None


class MeUser(BaseUser):
    img: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str
