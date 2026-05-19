"""
Achievement badges system for HalluciNO
"""

def get_achievements(streak: int, correct_answers: int, total_answers: int, score: int) -> list:
    """
    Calculate earned achievements based on game stats.
    
    Returns:
        list: List of achieved badges with names, icons, and descriptions
    """
    achievements = []
    
    # Achievement definitions
    all_achievements = {
        "streak_master": {
            "name": "Streak Master",
            "icon": "🎯",
            "description": "5 consecutive correct answers",
            "earned": streak >= 5
        },
        "on_fire": {
            "name": "On Fire",
            "icon": "🔥",
            "description": "10 consecutive correct answers",
            "earned": streak >= 10
        },
        "unstoppable": {
            "name": "Unstoppable",
            "icon": "💪",
            "description": "7 consecutive correct answers",
            "earned": streak >= 7
        },
        "master_level": {
            "name": "Master Level",
            "icon": "🏆",
            "description": "10 hallucinations detected perfectly",
            "earned": streak >= 10
        },
        "legendary": {
            "name": "Legendary",
            "icon": "👑",
            "description": "15 consecutive correct answers",
            "earned": streak >= 15
        },
        "unbeatable": {
            "name": "Unbeatable",
            "icon": "🌟",
            "description": "20 consecutive correct answers",
            "earned": streak >= 20
        },
        "perfect_game": {
            "name": "Perfect Game",
            "icon": "💯",
            "description": "100% accuracy in a game",
            "earned": total_answers > 0 and correct_answers == total_answers
        },
        "high_scorer": {
            "name": "High Scorer",
            "icon": "⚡",
            "description": "Score 100+ points in one game",
            "earned": score >= 100
        },
        "accuracy_king": {
            "name": "Accuracy King",
            "icon": "🎖️",
            "description": "90%+ accuracy in a game",
            "earned": total_answers > 0 and (correct_answers / total_answers) >= 0.9
        },
        "speed_learner": {
            "name": "Speed Learner",
            "icon": "⚡",
            "description": "Complete 10 questions",
            "earned": total_answers >= 10
        }
    }
    
    # Collect earned achievements
    for badge_id, badge_info in all_achievements.items():
        if badge_info["earned"]:
            achievements.append({
                "id": badge_id,
                "name": badge_info["name"],
                "icon": badge_info["icon"],
                "description": badge_info["description"]
            })
    
    return achievements


def get_achievement_message(achievements: list) -> str:
    """
    Generate motivational message based on earned achievements.
    
    Returns:
        str: Celebration message
    """
    if not achievements:
        return "Great effort! Keep playing to earn badges! 🚀"
    
    if len(achievements) == 1:
        return f"Awesome! You earned: {achievements[0]['icon']} {achievements[0]['name']}!"
    
    if len(achievements) >= 3:
        return f"🎉 Incredible! You earned {len(achievements)} badges! You're on fire! 🔥"
    
    return f"Great work! You earned {len(achievements)} badges! 🏆"
