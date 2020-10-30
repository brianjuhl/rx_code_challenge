from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def find_nearest_pharmacy():
    return "Hello World"