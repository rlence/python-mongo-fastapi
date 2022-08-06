from fastapi import APIRouter
from server.src.db.mongo import user

router = APIRouter( prefix="/user", tags=["user"])

@router.get("/")
async def get_user():
    try:
        user.insert_one({"name": "emily", "lastname": "marquez"})
        return {"name": "emily", "lastname": "marquez"}
    except Exception as err:
        print(err)
        return "ERROR TO INSERT USER"
