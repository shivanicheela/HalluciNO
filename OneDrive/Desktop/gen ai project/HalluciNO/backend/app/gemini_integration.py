"""
Gemini 2.0 Flash API Integration for Dynamic Question Generation
Generates AI hallucination quiz questions using Google's Gemini API
"""

import google.generativeai as genai
import os
import json
import re
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.0-flash"

CATEGORIES = [
    "Machine Learning",
    "Generative AI",
    "AI Agents",
    "Prompt Engineering",
    "LangChain",
    "LangGraph",
    "RAG",
    "Hallucinations",
    "Neural Networks",
    "Open Source LLMs"
]

DIFFICULTIES = ["beginner", "intermediate", "expert"]


async def generate_question(
    category: str = None,
    difficulty: str = "intermediate",
    topic: str = None
) -> Optional[Dict]:
    """
    Generate a dynamic AI hallucination question using Gemini 2.0 Flash
    
    Args:
        category: Question category (optional)
        difficulty: Difficulty level (beginner, intermediate, expert)
        topic: Custom topic for question generation (optional)
    
    Returns:
        Dictionary with question, category, is_hallucination, explanation, difficulty
    """
    if not GEMINI_API_KEY:
        return None
    
    try:
        # Select category if not provided
        if not category:
            import random
            category = random.choice(CATEGORIES)
        
        # Build prompt for Gemini
        difficulty_prompt = {
            "beginner": "simple and introductory level",
            "intermediate": "moderate complexity with some technical depth",
            "expert": "advanced and challenging, requiring deep knowledge"
        }.get(difficulty, "moderate")
        
        topic_text = f" about {topic}" if topic else ""
        
        prompt = f"""You are an AI expert creating quiz questions about AI hallucinations and misconceptions.

Generate ONE question{topic_text} in the category: {category}
Difficulty level: {difficulty_prompt}

The question should be a statement that the user must identify as either:
- TRUE (a correct fact about AI/ML)
- HALLUCINATION (a false or misleading statement about AI/ML)

Return ONLY valid JSON (no markdown, no extra text) with this exact structure:
{{
    "question": "The statement/claim to evaluate",
    "is_hallucination": true or false,
    "explanation": "Why this statement is true/false and what the correct understanding is",
    "category": "{category}",
    "difficulty": "{difficulty}"
}}

Important: 
- is_hallucination should be true if it's a false/misleading statement, false if it's true
- Make the explanation educational and clear
- Return ONLY the JSON object, nothing else"""

        # Call Gemini 2.0 Flash
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        
        # Parse response
        response_text = response.text.strip()
        
        # Clean up response if it has markdown code blocks
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
            response_text = response_text.strip()
        
        # Parse JSON
        question_data = json.loads(response_text)
        
        # Validate required fields
        required_fields = ["question", "is_hallucination", "explanation", "category", "difficulty"]
        if all(field in question_data for field in required_fields):
            # Add unique ID
            question_data["id"] = f"gemini_{hash(question_data['question']) % 10000}"
            return question_data
        
        return None
    
    except json.JSONDecodeError:
        print(f"Failed to parse Gemini response as JSON")
        return None
    except Exception as e:
        print(f"Error generating question from Gemini: {str(e)}")
        return None


async def generate_questions_batch(
    count: int = 5,
    category: str = None,
    difficulty: str = "intermediate"
) -> List[Dict]:
    """
    Generate multiple questions at once
    
    Args:
        count: Number of questions to generate
        category: Question category (optional)
        difficulty: Difficulty level
    
    Returns:
        List of generated questions
    """
    questions = []
    
    for i in range(count):
        question = await generate_question(category, difficulty)
        if question:
            questions.append(question)
    
    return questions


def is_gemini_available() -> bool:
    """Check if Gemini API is configured and available"""
    return bool(GEMINI_API_KEY)


async def get_question_with_fallback(
    fallback_question: Dict,
    category: str = None,
    difficulty: str = "intermediate"
) -> Dict:
    """
    Try to get a Gemini-generated question, fall back to static question if fails
    
    Args:
        fallback_question: Static question to use if Gemini fails
        category: Question category (optional)
        difficulty: Difficulty level
    
    Returns:
        Generated or fallback question
    """
    if not is_gemini_available():
        return fallback_question
    
    generated = await generate_question(category, difficulty)
    return generated if generated else fallback_question
