from fastapi import APIRouter
from app.api.routers import search, waste, simulate, import_export, logs

# Create a main API router
api_router = APIRouter()

# Include all the individual routers
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(waste.router, prefix="/waste", tags=["waste"])
api_router.include_router(simulate.router, prefix="/simulate", tags=["simulate"])
api_router.include_router(import_export.router, prefix="/import_export", tags=["import_export"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])