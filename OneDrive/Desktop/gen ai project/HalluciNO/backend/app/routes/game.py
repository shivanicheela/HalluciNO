"""
Game routes for HalluciNO - Updated with SQLite Database
Handles quiz gameplay, scoring, and leaderboard
"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import SubmitAnswerRequest, DifficultyLevel
from app.database import get_db, GameSession, LeaderboardEntry
from app.data.questions import (
    QUESTIONS, get_questions_by_difficulty, 
    get_categories
)
from app import gemini_integration
from app.utils.scoring import (
    calculate_hallucination_probability,
    calculate_score_change,
    get_streak_bonus,
    get_streak_message,
    calculate_accuracy
)
from app.utils.achievements import get_achievements, get_achievement_message
import random
from typing import List
import json

# Create router instance for game routes
router = APIRouter()

# Temporary in-memory cache for active sessions (for quick access during gameplay)
_session_cache = {}


@router.get("/categories")
async def get_all_categories():
    """Get all available question categories"""
    categories = get_categories()
    return {
        "categories": categories,
        "total": len(categories)
    }


@router.get("/generate-question")
async def generate_dynamic_question(
    category: str = None,
    difficulty: str = "intermediate",
    topic: str = None
):
    """
    Generate a dynamic question using Gemini 2.0 Flash API
    Falls back to static questions if Gemini is unavailable
    
    Query Parameters:
        category: Question category (optional) - will pick random if not specified
        difficulty: beginner, intermediate, or expert
        topic: Custom topic for question generation
    """
    if not gemini_integration.is_gemini_available():
        return {
            "error": "Gemini API not configured",
            "message": "Add GEMINI_API_KEY to .env file to enable dynamic questions",
            "fallback": "Using static questions instead"
        }
    
    try:
        question = await gemini_integration.generate_question(
            category=category,
            difficulty=difficulty,
            topic=topic
        )
        
        if question:
            return {
                "success": True,
                "source": "gemini-2.0-flash",
                "question": question
            }
        else:
            return {
                "success": False,
                "message": "Failed to generate question, using static fallback"
            }
    
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Gemini generation failed, use static questions"
        }


@router.get("/generate-batch")
async def generate_question_batch(
    count: int = 5,
    category: str = None,
    difficulty: str = "intermediate"
):
    """
    Generate multiple questions at once using Gemini 2.0 Flash
    
    Query Parameters:
        count: Number of questions to generate (1-10)
        category: Question category (optional)
        difficulty: beginner, intermediate, or expert
    """
    if not gemini_integration.is_gemini_available():
        return {
            "error": "Gemini API not configured",
            "message": "Add GEMINI_API_KEY to .env file to enable dynamic questions"
        }
    
    # Limit batch size
    if count > 10:
        count = 10
    if count < 1:
        count = 1
    
    try:
        questions = await gemini_integration.generate_questions_batch(
            count=count,
            category=category,
            difficulty=difficulty
        )
        
        return {
            "success": True,
            "source": "gemini-2.0-flash",
            "generated_count": len(questions),
            "questions": questions
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to generate questions batch"
        }


@router.post("/start/{user_id}")
async def start_game(
    user_id: str, 
    difficulty: str = "beginner", 
    question_count: int = 10,
    username: str = "",
    category: str = None,
    db: Session = Depends(get_db)
):
    """
    Start a new game session with Gemini-generated questions (always fresh & unique)
    
    Parameters:
        user_id: The player's user ID
        difficulty: beginner, intermediate, or expert
        question_count: Number of questions (1-50)
        username: The player's username
        category: Optional category to filter questions
    """
    # Validate difficulty
    try:
        difficulty_level = DifficultyLevel(difficulty.lower())
    except ValueError:
        raise HTTPException(
            status_code=400, 
            detail="Invalid difficulty. Choose from: beginner, intermediate, expert"
        )
    
    # Validate question count
    if question_count > 50:
        question_count = 50
    if question_count < 1:
        question_count = 1
    
    # Get questions - ALWAYS use Gemini for fresh, unique questions
    questions = []
    question_source = "static-fallback"
    
    # Try Gemini first (generates fresh questions every time)
    try:
        gemini_questions = await gemini_integration.generate_questions_batch(
            count=question_count,
            category=category,
            difficulty=difficulty
        )
        
        if gemini_questions and len(gemini_questions) > 0:
            # Convert Gemini questions to Question objects
            class GeminiQuestion:
                def __init__(self, data):
                    self.id = data.get("id", f"gemini_{random.randint(10000, 99999)}")
                    self.question = data.get("question", "")
                    self.category = data.get("category", "Generative AI")
                    self.is_hallucination = data.get("is_hallucination", False)
                    self.explanation = data.get("explanation", "")
                    self.difficulty = data.get("difficulty", difficulty)
                    self.hints = data.get("hints", [])
            
            questions = [GeminiQuestion(q) for q in gemini_questions]
            question_source = "gemini-2.0-flash"
    except Exception as e:
        print(f"Gemini generation error: {e}")
        pass
    
    # Fallback to static questions if Gemini fails
    if not questions:
        questions = QUESTIONS.copy()
        if category and category.lower() != 'all':
            questions = [q for q in questions if q.category.lower() == category.lower()]
        random.shuffle(questions)
        questions = questions[:question_count]
        question_source = "static-fallback"
    
    # Generate session ID
    session_id = f"{user_id}_{random.randint(100000, 999999)}"
    
    # Extract question IDs and save to database
    question_ids = [q.id for q in questions]
    
    db_session = GameSession(
        session_id=session_id,
        user_id=user_id,
        username=username if username else user_id,
        questions=json.dumps(question_ids),
        difficulty=difficulty,
        score=0,
        streak=0,
        max_streak=0,
        completed=0
    )
    db.add(db_session)
    db.commit()
    
    # Cache in memory for quick access
    _session_cache[session_id] = {
        "questions": questions,
        "current_question_index": 0,
        "answers": []
    }
    
    return {
        "session_id": session_id,
        "difficulty": difficulty,
        "total_questions": len(questions),
        "current_question": 1,
        "question_source": question_source,
        "message": f"Game started! Answer {len(questions)} questions! 🚀"
    }


@router.get("/question/{session_id}")
async def get_next_question(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Get the next question in the game"""
    # Check database
    game = db.query(GameSession).filter(GameSession.session_id == session_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Check cache
    if session_id not in _session_cache:
        # Restore from database
        question_ids = json.loads(game.questions)
        questions = [q for q in QUESTIONS if q.id in question_ids]
        _session_cache[session_id] = {
            "questions": questions,
            "current_question_index": len(json.loads(game.answers) if game.answers else []),
            "answers": json.loads(game.answers) if game.answers else []
        }
    
    cache = _session_cache[session_id]
    idx = cache["current_question_index"]
    
    if idx >= len(cache["questions"]):
        raise HTTPException(status_code=400, detail="Game completed")
    
    question = cache["questions"][idx]
    
    return {
        "question_number": idx + 1,
        "total_questions": len(cache["questions"]),
        "category": question.category,
        "question": question.question,
        "question_id": question.id,
        "difficulty": question.difficulty,
        "hints": question.hints if hasattr(question, 'hints') else None
    }


@router.post("/submit-answer/{session_id}")
async def submit_answer(
    session_id: str,
    answer_data: SubmitAnswerRequest,
    db: Session = Depends(get_db)
):
    """Submit an answer and get feedback with advanced scoring"""
    # Get session from database
    game = db.query(GameSession).filter(GameSession.session_id == session_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Get from cache
    if session_id not in _session_cache:
        raise HTTPException(status_code=400, detail="Session expired")
    
    cache = _session_cache[session_id]
    idx = cache["current_question_index"]
    
    if idx >= len(cache["questions"]):
        raise HTTPException(status_code=400, detail="Game already completed")
    
    question = cache["questions"][idx]
    
    # Check if answer is correct
    is_correct = answer_data.user_answer == question.is_hallucination
    
    # Calculate score change (new: -3 for wrong answers)
    points_change, reason = calculate_score_change(is_correct)
    
    # Update counters and score
    if is_correct:
        game.correct_answers = (game.correct_answers or 0) + 1
        game.score += points_change
        game.streak += 1
        game.max_streak = max(game.max_streak, game.streak)
        feedback = random.choice([
            "🔥 Nailed it! You spotted the hallucination!",
            "✨ Brilliant! That's a truth!",
            "🎯 Perfect! You're on fire!",
            "💯 Correct! You know your AI!",
            "🚀 Amazing! No hallucinations can fool you!",
        ])
        # Add streak bonus if milestone reached
        bonus = get_streak_bonus(game.streak)
        if bonus > 0:
            game.score += bonus
            streak_message = get_streak_message(game.streak)
        else:
            streak_message = ""
    else:
        game.wrong_answers = (game.wrong_answers or 0) + 1
        game.score = max(0, game.score + points_change)  # Don't go below 0
        game.streak = 0
        feedback = random.choice([
            "😭 Hallucination detected! AI fooled you!",
            "❌ Oops! The AI got you this time!",
            "🤖 AI wins this round!",
            "😅 Tricky one! Better luck next time!",
            "💫 The AI is good at lying!",
        ])
        streak_message = ""
    
    # Calculate hallucination probability for this player
    total_answers = (game.correct_answers or 0) + (game.wrong_answers or 0)
    hallucination_probability = calculate_hallucination_probability(
        streak=game.streak,
        correct_answers=game.correct_answers or 0,
        wrong_answers=game.wrong_answers or 0,
        is_correct=is_correct,
        difficulty=game.difficulty
    )
    
    # Store answer
    current_answers = cache["answers"]
    current_answers.append({
        "question_id": answer_data.question_id,
        "user_answer": answer_data.user_answer,
        "correct_answer": question.is_hallucination,
        "is_correct": is_correct,
        "category": question.category
    })
    
    game.answers = json.dumps(current_answers)
    
    # Track score history
    score_history = json.loads(game.score_history) if game.score_history else []
    score_history.append({
        "points": points_change,
        "reason": reason,
        "total_score": game.score,
        "is_correct": is_correct
    })
    game.score_history = json.dumps(score_history)
    
    cache["current_question_index"] += 1
    
    # Check if game is completed
    game_completed = cache["current_question_index"] >= len(cache["questions"])
    if game_completed:
        game.completed = 1
    
    db.commit()
    
    return {
        "is_correct": is_correct,
        "feedback": feedback,
        "explanation": question.explanation,
        "current_score": game.score,
        "streak": game.streak,
        "streak_message": streak_message,
        "hallucination_probability": hallucination_probability,
        "points_change": points_change,
        "game_completed": game_completed,
        "progress": f"{cache['current_question_index']}/{len(cache['questions'])}"
    }


@router.get("/final-score/{session_id}")
async def get_final_score(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Get final game score and statistics"""
    game = db.query(GameSession).filter(GameSession.session_id == session_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Parse answers from JSON
    answers = json.loads(game.answers) if game.answers else []
    
    # Get questions
    if session_id in _session_cache:
        questions = _session_cache[session_id]["questions"]
    else:
        question_ids = json.loads(game.questions)
        questions = [q for q in QUESTIONS if q.id in question_ids]
    
    total_questions = len(questions)
    correct_answers = sum(1 for ans in answers if ans["is_correct"])
    accuracy = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    # Category breakdown
    category_scores = {}
    for ans in answers:
        cat = ans["category"]
        if cat not in category_scores:
            category_scores[cat] = {"correct": 0, "total": 0}
        category_scores[cat]["total"] += 1
        if ans["is_correct"]:
            category_scores[cat]["correct"] += 1
    
    # Determine badge
    if accuracy >= 90:
        badge = "🏆 AI Master"
    elif accuracy >= 80:
        badge = "🥇 Hallucination Detective"
    elif accuracy >= 70:
        badge = "🥈 AI Spotter"
    elif accuracy >= 60:
        badge = "🥉 Beginner Skeptic"
    else:
        badge = "🤖 AI Fell for It"
    
    # Calculate achievements (NEW!)
    achievements = get_achievements(
        streak=game.max_streak,
        correct_answers=correct_answers,
        total_answers=total_questions,
        score=game.score
    )
    achievement_message = get_achievement_message(achievements)
    
    # Store achievements in database
    game.achievements = json.dumps(achievements)
    
    # Add to leaderboard in database
    leaderboard_entry = LeaderboardEntry(
        username=game.username,
        score=game.score,
        accuracy=round(accuracy, 2),
        max_streak=game.max_streak,
        badge=badge
    )
    db.add(leaderboard_entry)
    db.commit()
    
    # Build question review
    question_review = []
    for ans in answers:
        question = None
        for q in questions:
            if q.id == ans["question_id"]:
                question = q
                break
        
        if question:
            question_review.append({
                "question": question.question,
                "explanation": question.explanation,
                "user_answer": "Truth" if ans["user_answer"] else "Hallucination",
                "correct_answer": "Truth" if ans["correct_answer"] else "Hallucination",
                "is_correct": ans["is_correct"],
                "category": ans["category"]
            })
    
    return {
        "session_id": session_id,
        "final_score": game.score,
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "accuracy_percentage": round(accuracy, 2),
        "max_streak": game.max_streak,
        "badge": badge,
        "achievements": achievements,
        "achievement_message": achievement_message,
        "category_breakdown": {cat: f"{data['correct']}/{data['total']}" 
                              for cat, data in category_scores.items()},
        "message": f"Game Over! You scored {game.score} points! {badge}",
        "question_review": question_review
    }


@router.get("/leaderboard")
async def get_leaderboard(
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get top scores from leaderboard"""
    # Query top scores from database
    top_scores = db.query(LeaderboardEntry).order_by(
        desc(LeaderboardEntry.score)
    ).limit(limit).all()
    
    leaderboard = []
    for i, entry in enumerate(top_scores, 1):
        leaderboard.append({
            "rank": i,
            "username": entry.username,
            "score": entry.score,
            "accuracy": entry.accuracy,
            "max_streak": entry.max_streak,
            "badge": entry.badge
        })
    
    return {
        "leaderboard": leaderboard,
        "total": len(leaderboard),
        "message": "Top AI Hallucination Detectors! 👑"
    }


@router.post("/restart/{session_id}")
async def restart_game(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Restart the game - clears session cache"""
    if session_id in _session_cache:
        del _session_cache[session_id]
    
    return {"message": "Game restarted! ✨"}
