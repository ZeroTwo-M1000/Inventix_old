from fastapi import APIRouter, File, UploadFile, Depends

from api.Auth.models import CreateUser, LoginUser, Token, MeUser
from api.Auth.repo import AuthRepo
from response.api_response import OkResponse, ErrorResponse
from utils.Auth.auth import auth
from utils.Auth.image import save_image, delete_image

router = APIRouter()


@router.post("/register")
async def register(user: CreateUser = Depends(), file: UploadFile = File(...)):
    user.hash_password = auth.encrypt_password(user.hash_password)
    if await AuthRepo.get_user_by_name(user.name) is not None:
        return ErrorResponse(message="User already exists")

    user.img = save_image(file)

    await AuthRepo.create_user(user)

    return OkResponse(
        success=True,
        message="User created",
        data=Token(
            access_token=auth.encode_token({"sub": user.name}), token_type="bearer"
        ),
    )


@router.post("/login")
async def login(user: LoginUser):
    if not (user_db := await AuthRepo.get_user_by_name(user.name)):
        return ErrorResponse(message="Invalid login")

    if not auth.verify_password(user.password, user_db.hash_password):
        return ErrorResponse(message="Invalid login")

    return OkResponse(
        message="Login success",
        data=Token(
            access_token=auth.encode_token({"sub": user_db.name}), token_type="bearer"
        ),
    )


@router.delete("/delete")
async def delete(user=Depends(auth.get_current_user)):
    await AuthRepo.delete_user(user.name)
    delete_image(user.img)
    return OkResponse(message="User deleted")


@router.get("/me")
async def me(user=Depends(auth.get_current_user)):
    return OkResponse(data=MeUser(**user.dict()), message="You are logged in")
