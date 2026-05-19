"""
HalluciNO - AI Hallucination Detector
Backend Entry Point

To run the backend:
1. Install dependencies: pip install -r requirements.txt
2. Run: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
3. Access API docs: http://localhost:8000/docs
"""

from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
