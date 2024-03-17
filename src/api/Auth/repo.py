from api.Auth.models import CreateUser
from core.config import config


class AuthRepo:
    @staticmethod
    async def create_user(user: CreateUser):
        return await config.prisma_connection.prisma.user.create(data=user.dict())

    @staticmethod
    async def get_user_by_name(name: str):
        return await config.prisma_connection.prisma.user.find_unique(
            where={"name": name}
        )

    @staticmethod
    async def delete_user(name: str):
        return await config.prisma_connection.prisma.user.delete(where={"name": name})
