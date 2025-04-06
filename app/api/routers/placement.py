from fastapi import APIRouter

router = APIRouter()

@router.get("/placement")
async def get_placement():
    return {"message": "Placement endpoint"} 
