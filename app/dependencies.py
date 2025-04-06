from fastapi import Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from .database import get_db  # Assuming you have a database module
from .auth import verify_token  # Assuming you have an auth module
import logging

logger = logging.getLogger("my_logger")

def get_database_session() -> Session:
    db = get_db()  # This function should return a database session
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)  # This function should verify the token
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def common_query_params(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Maximum number of items to return"),
):
    return {"skip": skip, "limit": limit}

async def log_request(request: Request):
    logger.info(f"Request: {request.method} {request.url}")
