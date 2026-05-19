"""
HalluciNO - AI Hallucination Detector Backend
FastAPI Backend for the interactive quiz game about AI hallucinations

This backend provides APIs for:
- User authentication (login)
- Fetching quiz questions
- Submitting answers and calculating scores
- Managing leaderboard (persistent with SQLite)
- Optional Gemini API integration for dynamic questions
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, game
from app.data import questions
from app.database import engine, Base

# Initialize FastAPI app
app = FastAPI(
    title="HalluciNO API",
    description="AI Hallucination Detector Backend",
    version="1.0.0"
)

# Add CORS middleware to allow Angular frontend requests
# This allows the frontend to make requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route modules
# These routes handle different aspects of the game
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(game.router, prefix="/api/game", tags=["Game"])

# Root endpoint - just for testing
@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to HalluciNO - AI Hallucination Detector",
        "version": "1.0.0"
    }

# Health check endpoint - useful for deployment monitoring
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    # Run the server on localhost:8000
    # To access the interactive docs, go to http://localhost:8000/docs
    uvicorn.run(app, host="0.0.0.0", port=8000)
