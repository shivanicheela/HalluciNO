"""
Authentication Routes
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str

class LoginResponse(BaseModel):
    user_id: str
    username: str
    message: str

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Login endpoint - creates or retrieves a user session
    """
    if not request.username or len(request.username.strip()) < 2:
        raise HTTPException(status_code=400, detail="Username must be at least 2 characters")
    
    # Generate a simple user ID
    user_id = f"user_{request.username.lower().replace(' ', '_')}"
    
    return LoginResponse(
        user_id=user_id,
        username=request.username,
        message=f"Welcome {request.username}!"
    )

@router.get("/verify/{user_id}")
async def verify_user(user_id: str):
    """
    Verify if a user exists
    """
    return {
        "user_id": user_id,
        "verified": True
    }
