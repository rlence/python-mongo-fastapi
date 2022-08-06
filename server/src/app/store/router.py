from fastapi import APIRouter

router = APIRouter( prefix="/store", tags=["store"])

@router.get("/")
async def get_products():
    return "THE LIST OF PRODUTS"