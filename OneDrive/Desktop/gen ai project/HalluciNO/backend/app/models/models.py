"""
Data models for HalluciNO game
Using Pydantic models for data validation and serialization
"""

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class DifficultyLevel(str, Enum):
    """Difficulty levels for the game"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"


class User(BaseModel):
    """User model for login"""
    username: str
    user_id: Optional[str] = None  # Can be auto-generated


class Question(BaseModel):
    """Question model for quiz"""
    id: int
    question: str
    category: str  # e.g., "Machine Learning", "Generative AI", etc.
    is_hallucination: bool  # True if the statement is a hallucination
    explanation: str  # Why this is true/false
    difficulty: DifficultyLevel  # Difficulty level
    hints: Optional[List[str]] = None  # Optional hints (max 2)


class Answer(BaseModel):
    """User's answer to a question"""
    question_id: int
    user_answer: bool  # True if user thinks it's hallucination, False if truthful
    time_taken: int  # Time taken in seconds


class GameSession(BaseModel):
    """Game session data"""
    session_id: str
    username: str
    difficulty: DifficultyLevel
    score: int = 0
    total_questions: int = 0
    correct_answers: int = 0
    streak: int = 0
    max_streak: int = 0
    answers: List[Answer] = []


class LeaderboardEntry(BaseModel):
    """Leaderboard entry"""
    rank: int
    username: str
    score: int
    category: str  # Which category they scored most in
    streak: int


class SubmitAnswerRequest(BaseModel):
    """Request model for submitting an answer"""
    question_id: int
    user_answer: bool
    time_taken: int


class FinalScoreResponse(BaseModel):
    """Response model for final score"""
    session_id: str
    username: str
    score: int
    total_questions: int
    correct_answers: int
    max_streak: int
    accuracy_percentage: float
    category_breakdown: dict  # Scores by category
    badge: str  # Achievement badge name
