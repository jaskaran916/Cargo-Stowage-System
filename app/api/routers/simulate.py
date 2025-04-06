from fastapi import APIRouter

router = APIRouter()

@router.post("/day")
async def simulate_day(num_of_days: int):
    # Logic to simulate the passage of days
    return {"message": f"Simulated {num_of_days} days"}