"""
Database configuration and models for HalluciNO
Uses SQLite for persistent data storage
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database setup
DATABASE_URL = "sqlite:///./halluci_no.db"
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    """User model for storing player information"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class GameSession(Base):
    """Game session model for storing game state"""
    __tablename__ = "game_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, unique=True, index=True)
    user_id = Column(String, index=True)
    username = Column(String)
    score = Column(Integer, default=0)
    questions = Column(JSON)  # Store question IDs
    answers = Column(JSON, default=list)  # Store all answers
    current_question = Column(Integer, default=0)
    streak = Column(Integer, default=0)
    max_streak = Column(Integer, default=0)
    difficulty = Column(String)
    completed = Column(Integer, default=0)  # 0 = in progress, 1 = completed
    # New fields for enhanced features
    score_history = Column(JSON, default=list)  # [{points: 10, reason: 'correct'}, ...]
    correct_answers = Column(Integer, default=0)  # Count of correct answers
    wrong_answers = Column(Integer, default=0)  # Count of wrong answers
    achievements = Column(JSON, default=lambda: [])  # Store earned badges
    created_at = Column(DateTime, default=datetime.utcnow)


class LeaderboardEntry(Base):
    """Leaderboard model for storing final scores"""
    __tablename__ = "leaderboard"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    score = Column(Integer)
    accuracy = Column(Float)
    max_streak = Column(Integer)
    badge = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Create tables
Base.metadata.create_all(bind=engine)


def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
