import os

from pydantic import Field
from pydantic_settings import BaseSettings

from core.db_helper import PrismaConnection


class Config(BaseSettings):
    prisma_connection: PrismaConnection = PrismaConnection()
    PROJECT_ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(..., env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")


config = Config()
