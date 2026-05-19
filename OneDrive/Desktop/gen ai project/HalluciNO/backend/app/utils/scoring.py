"""
Scoring and probability calculation utilities for HalluciNO
"""

def calculate_hallucination_probability(
    streak: int,
    correct_answers: int,
    wrong_answers: int,
    is_correct: bool,
    difficulty: str = "beginner"
) -> float:
    """
    Calculate the hallucination probability based on performance metrics.
    
    This represents how likely the AI thinks it's a hallucination (0-100).
    Used as a confidence/uncertainty metric.
    
    Parameters:
        streak: Current streak count
        correct_answers: Total correct answers so far
        wrong_answers: Total wrong answers so far
        is_correct: Whether the current answer was correct
        difficulty: Game difficulty level
    
    Returns:
        float: Probability value between 0 and 100
    """
    
    # Base probability on overall accuracy
    total_answers = correct_answers + wrong_answers
    if total_answers == 0:
        base_accuracy = 50.0
    else:
        base_accuracy = (correct_answers / total_answers) * 100
    
    # Streak multiplier (confidence boost)
    streak_multiplier = 1.0 + (streak * 0.05)  # +5% per streak
    
    # Difficulty adjustment
    difficulty_factors = {
        "beginner": 0.8,      # Easier to identify hallucinations
        "intermediate": 1.0,  # Standard difficulty
        "expert": 1.2         # Harder to identify
    }
    difficulty_factor = difficulty_factors.get(difficulty.lower(), 1.0)
    
    # Calculate confidence (inverse of uncertainty)
    # Higher accuracy = higher confidence in hallucination detection
    confidence = (base_accuracy / 100.0) * streak_multiplier * difficulty_factor
    
    # Clamp between 15 and 95 (never 0 or 100, always some uncertainty)
    probability = min(95, max(15, confidence * 100))
    
    # Add slight randomness for realism (±5%)
    import random
    probability = probability + random.uniform(-5, 5)
    
    return round(max(0, min(100, probability)), 1)


def calculate_score_change(is_correct: bool) -> tuple:
    """
    Calculate score change for an answer.
    
    Returns:
        tuple: (points_change, reason_text)
    """
    if is_correct:
        return (10, "correct_answer")
    else:
        return (-3, "wrong_answer")


def get_streak_bonus(streak: int) -> int:
    """
    Calculate bonus points for streak milestones.
    
    Returns:
        int: Bonus points (0 if no milestone reached)
    """
    # Milestone bonuses: 2, 3, 5, 7, 10, 15, 20
    milestones = {
        2: 2,
        3: 3,
        5: 5,
        7: 7,
        10: 10,
        15: 15,
        20: 20,
    }
    
    return milestones.get(streak, 0)


def get_streak_message(streak: int) -> str:
    """
    Get motivational message for streak achievement.
    
    Returns:
        str: Motivational message or empty string
    """
    milestone_messages = {
        2: "🎯 2 In a Row! Nice!",
        3: "🔥 3-Hallucination Streak! On Fire!",
        5: "⚡ 5 In a Row! You're a Pro!",
        7: "💪 7-Streak! Unstoppable!",
        10: "🏆 10-Hallucinations Detected! Master Level!",
        15: "👑 15-Streak! You're Legendary!",
        20: "🌟 20 Perfect Answers! Unbeatable!",
    }
    
    return milestone_messages.get(streak, "")


def calculate_accuracy(correct_answers: int, total_answers: int) -> float:
    """
    Calculate accuracy percentage.
    
    Returns:
        float: Accuracy percentage (0-100)
    """
    if total_answers == 0:
        return 0.0
    return round((correct_answers / total_answers) * 100, 2)
