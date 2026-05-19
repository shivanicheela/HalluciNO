"""
Authentication routes for HalluciNO
Handles user login and session management
"""

from fastapi import APIRouter, HTTPException
from app.models import User
import uuid

# Create router instance for auth routes
router = APIRouter()

# In-memory storage for active users (in production, use a database)
active_users = {}

@router.post("/login")
async def login(user: User):
    """
    Login endpoint - creates a new game session for a user
    
    Args:
        user: User object with username
        
    Returns:
        User ID and session token
    """
    # Validate username
    if not user.username or len(user.username.strip()) == 0:
        raise HTTPException(status_code=400, detail="Username cannot be empty")
    
    if len(user.username) > 30:
        raise HTTPException(status_code=400, detail="Username too long (max 30 characters)")
    
    # Generate unique user ID
    user_id = str(uuid.uuid4())[:8]
    
    # Store user
    active_users[user_id] = {
        "username": user.username.strip(),
        "created_at": user_id
    }
    
    # Return user info and token
    return {
        "success": True,
        "user_id": user_id,
        "username": user.username.strip(),
        "message": f"Welcome {user.username}! Let's play HalluciNO! 🎮"
    }

@router.get("/validate/{user_id}")
async def validate_user(user_id: str):
    """
    Validate if a user session is still active
    
    Args:
        user_id: The user ID to validate
        
    Returns:
        User validation status
    """
    if user_id in active_users:
        return {
            "valid": True,
            "username": active_users[user_id]["username"]
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
