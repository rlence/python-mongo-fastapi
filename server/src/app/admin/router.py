from fastapi import APIRouter

router = APIRouter( prefix="/admin", tags=["admin"])

@router.get("/")
async def get_admin():
    return "THE IS ADMIN"