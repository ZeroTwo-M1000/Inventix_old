from fastapi import APIRouter, File, UploadFile, Depends, HTTPException

from api.Auth.models import CreateUser, LoginUser, Token, MeUser
from api.Auth.repo import AuthRepo
from utils.Auth.auth import auth
from utils.Auth.image import save_image, delete_image

router = APIRouter()


@router.post("/register")
async def register(user: CreateUser = Depends(), file: UploadFile = File(...)):
    user.hash_password = auth.encrypt_password(user.hash_password)
    user.img = save_image(file)

    await AuthRepo.create_user(user)

    return Token(
        access_token=auth.encode_token({"sub": user.name}), token_type="bearer"
    )


@router.post("/login")
async def login(user: LoginUser):
    user_db = await AuthRepo.get_user_by_name(user.name)
    if not user_db:
        raise HTTPException(status_code=200, detail="User not found")

    if not auth.verify_password(user.password, user_db.hash_password):
        raise HTTPException(status_code=200, detail="Incorrect password")

    return Token(
        access_token=auth.encode_token({"sub": user_db.name}), token_type="bearer"
    )


@router.delete("/delete")
async def delete(user=Depends(auth.get_current_user)):
    await AuthRepo.delete_user(user.name)
    delete_image(user.img)
    return {"message": "User deleted"}


@router.get("/me")
async def me(user=Depends(auth.get_current_user)):
    return MeUser(**user.dict())
