"""
HalluciNO Backend - FastAPI Application
Main entry point for the API server
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.routes import auth, game

# Initialize FastAPI app
app = FastAPI(
    title="HalluciNO API",
    description="AI Hallucination Detector Quiz Game - Backend API",
    version="1.0.0"
)

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(game.router, prefix="/api/game", tags=["Game"])

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "🎮 HalluciNO API - AI Hallucination Detector",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "auth": "/api/auth",
            "game": "/api/game"
        }
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
