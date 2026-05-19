import { Injectable } from '@angular/core';

// Service for API communication with backend
// This service handles all HTTP requests to the FastAPI backend

@Injectable({ providedIn: 'root' })
export class ApiService {
  // Backend API URL - proxied through dev server
  // In production, update to full URL: 'http://your-domain.com/api'
  private apiUrl = '/api';

  constructor() {}

  /**
   * Generic fetch wrapper for API calls
   * Handles error cases and JSON parsing
   */
  private async fetchApi(endpoint: string, method: string = 'GET', body?: any) {
    const url = `${this.apiUrl}${endpoint}`;
    const options: any = {
      method,
      headers: { 'Content-Type': 'application/json' }
    };

    if (body) {
      options.body = JSON.stringify(body);
    }

    try {
      const response = await fetch(url, options);
      if (!response.ok) {
        throw new Error(`API Error: ${response.statusText}`);
      }
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }

  // ===== Authentication APIs =====

  /**
   * Login with username
   * Returns user_id and session token
   */
  async login(username: string) {
    return this.fetchApi('/auth/login', 'POST', { username });
  }

  /**
   * Validate if user session is still active
   */
  async validateUser(userId: string) {
    return this.fetchApi(`/auth/validate/${userId}`, 'GET');
  }

  // ===== Game APIs =====

  /**
   * Get all available question categories
   */
  async getCategories() {
    return this.fetchApi('/game/categories', 'GET');
  }

  /**
   * Start a new game session - always generates fresh questions via Gemini
   */
  async startGame(userId: string, difficulty: string = 'beginner', questionCount: number = 10, username: string = '', category?: string) {
    let url = `/game/start/${userId}?difficulty=${difficulty}&question_count=${questionCount}&username=${encodeURIComponent(username)}`;
    if (category && category !== 'all') {
      url += `&category=${encodeURIComponent(category)}`;
    }
    return this.fetchApi(url, 'POST');
  }

  /**
   * Get the next question in the game
   */
  async getNextQuestion(sessionId: string) {
    return this.fetchApi(`/game/question/${sessionId}`, 'GET');
  }

  /**
   * Submit answer to a question
   */
  async submitAnswer(sessionId: string, answerData: any) {
    return this.fetchApi(`/game/submit-answer/${sessionId}`, 'POST', answerData);
  }

  /**
   * Get final score and statistics
   */
  async getFinalScore(sessionId: string) {
    return this.fetchApi(`/game/final-score/${sessionId}`, 'GET');
  }

  /**
   * Get leaderboard
   */
  async getLeaderboard(limit: number = 10) {
    return this.fetchApi(`/game/leaderboard?limit=${limit}`, 'GET');
  }

  /**
   * Restart game by deleting session
   */
  async restartGame(sessionId: string) {
    return this.fetchApi(`/game/restart/${sessionId}`, 'POST');
  }
}
