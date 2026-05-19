"""
Game Routes
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Question(BaseModel):
    id: int
    text: str
    options: List[str]
    correct_answer: int

class GameSessionResponse(BaseModel):
    session_id: str
    user_id: str
    total_questions: int

class AnswerSubmission(BaseModel):
    answer: int

class SubmitAnswerResponse(BaseModel):
    correct: bool
    message: str
    score: int

# Sample questions
SAMPLE_QUESTIONS = [
    {
        "id": 1,
        "text": "Is the Earth flat?",
        "options": ["Truth", "Hallucination"],
        "correct_answer": 0
    },
    {
        "id": 2,
        "text": "Can humans breathe underwater naturally?",
        "options": ["Hallucination", "Truth"],
        "correct_answer": 0
    },
    {
        "id": 3,
        "text": "Does the Sun revolve around the Earth?",
        "options": ["Hallucination", "Truth"],
        "correct_answer": 0
    }
]

@router.post("/start/{user_id}", response_model=GameSessionResponse)
async def start_game(user_id: str, question_count: int = 5):
    """
    Start a new game session
    """
    return GameSessionResponse(
        session_id=f"session_{user_id}_{question_count}",
        user_id=user_id,
        total_questions=question_count
    )

@router.get("/question/{session_id}")
async def get_question(session_id: str, question_index: int = 0):
    """
    Get the next question for a session
    """
    if question_index >= len(SAMPLE_QUESTIONS):
        return {"message": "No more questions"}
    
    q = SAMPLE_QUESTIONS[question_index]
    return {
        "question_id": q["id"],
        "text": q["text"],
        "options": q["options"],
        "question_number": question_index + 1,
        "total_questions": len(SAMPLE_QUESTIONS)
    }

@router.post("/submit-answer/{session_id}", response_model=SubmitAnswerResponse)
async def submit_answer(session_id: str, answer: AnswerSubmission, question_index: int = 0):
    """
    Submit an answer and get feedback
    """
    if question_index >= len(SAMPLE_QUESTIONS):
        raise HTTPException(status_code=400, detail="Invalid question index")
    
    correct_answer = SAMPLE_QUESTIONS[question_index]["correct_answer"]
    is_correct = answer.answer == correct_answer
    
    return SubmitAnswerResponse(
        correct=is_correct,
        message="Correct!" if is_correct else "Incorrect!",
        score=10 if is_correct else 0
    )

@router.get("/final-score/{session_id}")
async def get_final_score(session_id: str):
    """
    Get the final score for a session
    """
    return {
        "session_id": session_id,
        "total_score": 50,
        "accuracy": 66.7,
        "message": "Game completed!"
    }

@router.get("/leaderboard")
async def get_leaderboard(limit: int = 10):
    """
    Get the top players leaderboard
    """
    return {
        "leaderboard": [
            {"rank": 1, "username": "Player1", "score": 1000},
            {"rank": 2, "username": "Player2", "score": 950},
            {"rank": 3, "username": "Player3", "score": 900}
        ],
        "total_players": 3
    }
