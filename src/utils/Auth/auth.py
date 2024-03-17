from typing import Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext

from api.Auth.repo import AuthRepo
from core.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
get_bearer_token = HTTPBearer(auto_error=False)


class Auth:
    @staticmethod
    def encode_token(payload):
        return jwt.encode(payload, config.SECRET_KEY, algorithm=config.ALGORITHM)

    @staticmethod
    def decode_token(token):
        return jwt.decode(token, config.SECRET_KEY, algorithms=config.ALGORITHM)

    @staticmethod
    def encrypt_password(password):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    async def get_current_user(
        auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
    ):
        if auth is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        try:
            name = Auth.decode_token(auth.credentials)["sub"]
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        user = await AuthRepo.get_user_by_name(name)

        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        else:
            return user


auth = Auth()

# from typing import Optional
#
# import bcrypt
# import jwt
# from fastapi import Depends, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from starlette import status
#
# from API.User.repo.UserRepo import UserRepo
# from Config.connection import config
# from Response.Response import Response
#
# get_bearer_token = HTTPBearer(auto_error=False)
#
#
# def decode_token(token: str):
#     return jwt.decode(token.encode("utf-8"), config.env.get("SECRET_KEY"), algorithms=["HS256"])
#
#
# def encode_token(name: str):
#     return jwt.encode({"name": name}, config.env.get("SECRET_KEY"), algorithm="HS256")
#
#
# def hashing_password(password: str):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
#
#     return hashed_password
#
#
# async def get_token(
#         auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
# ) -> str:
#     if auth is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED
#         )
#     try:
#         name = decode_token(auth.credentials)["name"]
#     except:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED
#         )
#     user = await UserRepo.get_me(name)
#
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED
#         )
#
#     else:
#         return auth.credentials
