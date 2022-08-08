from distutils.log import error
from fastapi import HTTPException
from fastapi import APIRouter

from server.src.models.user import User
from server.src.app.user import service

from .model import LogginUser

from server.src.responses.response import exception_manager

router = APIRouter( prefix="/user", tags=["user"])

# @router.get("/")
# async def get_user():
#     try:
#         user.insert_one({"name": "emily", "lastname": "marquez"})
#         return {"name": "emily", "lastname": "marquez"}
#     except Exception as err:
#         print(err)
#         return "ERROR TO INSERT USER"


@router.post("/register")
@exception_manager
async def register_user(user: User):
    return await service.create_user(user)


@router.post("/login")
@exception_manager
async def loggin_user(loggin_user: LogginUser):
        return await service.user_login(loggin_user)