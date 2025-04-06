from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI()

# Include the main API router
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Cargo Stowage Management API"}