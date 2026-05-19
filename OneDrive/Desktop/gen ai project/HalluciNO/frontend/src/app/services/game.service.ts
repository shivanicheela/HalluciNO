import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { ApiService } from './api.service';

// Interface for game state management
export interface GameState {
  sessionId: string | null;
  userId: string | null;
  username: string;
  difficulty: string;
  currentQuestion: number;
  totalQuestions: number;
  score: number;
  streak: number;
  maxStreak: number;
  correctAnswers: number;
  isGameActive: boolean;
}

// Service for managing game state and logic
@Injectable({ providedIn: 'root' })
export class GameService {
  // BehaviorSubjects for reactive state management
  private gameState$ = new BehaviorSubject<GameState>({
    sessionId: null,
    userId: null,
    username: '',
    difficulty: 'beginner',
    currentQuestion: 0,
    totalQuestions: 0,
    score: 0,
    streak: 0,
    maxStreak: 0,
    correctAnswers: 0,
    isGameActive: false
  });

  constructor(private apiService: ApiService) {}

  // ===== State Getters =====

  getGameState() {
    return this.gameState$.asObservable();
  }

  getCurrentState() {
    return this.gameState$.value;
  }

  getScore() {
    return this.gameState$.value.score;
  }

  getStreak() {
    return this.gameState$.value.streak;
  }

  getProgress() {
    const state = this.gameState$.value;
    return state.totalQuestions > 0 ? (state.currentQuestion / state.totalQuestions) * 100 : 0;
  }

  // ===== State Setters =====

  updateGameState(partial: Partial<GameState>) {
    const current = this.gameState$.value;
    this.gameState$.next({ ...current, ...partial });
  }

  // ===== Game Logic =====

  /**
   * Start a new game session
   */
  async startGame(userId: string, username: string, difficulty: string = 'beginner', category?: string, questionCount: number = 10) {
    try {
      const response = await this.apiService.startGame(userId, difficulty, questionCount, username, category);
      
      this.updateGameState({
        sessionId: response.session_id,
        userId,
        username,
        difficulty,
        currentQuestion: 1,
        totalQuestions: response.total_questions,
        score: 0,
        streak: 0,
        maxStreak: 0,
        correctAnswers: 0,
        isGameActive: true
      });

      return response;
    } catch (error) {
      console.error('Failed to start game:', error);
      throw error;
    }
  }

  /**
   * Submit answer and update game state
   */
  async submitAnswer(questionId: number, userAnswer: boolean, timeTaken: number) {
    const state = this.gameState$.value;
    
    if (!state.sessionId) {
      throw new Error('No active game session');
    }

    try {
      const response = await this.apiService.submitAnswer(state.sessionId, {
        question_id: questionId,
        user_answer: userAnswer,
        time_taken: timeTaken
      });

      // Update score and streak
      if (response.is_correct) {
        this.updateGameState({
          score: response.current_score,
          streak: response.streak,
          correctAnswers: state.correctAnswers + 1,
          currentQuestion: state.currentQuestion + 1,
          maxStreak: Math.max(state.maxStreak, response.streak)
        });
      } else {
        this.updateGameState({
          streak: 0,
          currentQuestion: state.currentQuestion + 1
        });
      }

      return response;
    } catch (error) {
      console.error('Failed to submit answer:', error);
      throw error;
    }
  }

  /**
   * Get final score
   */
  async getFinalScore() {
    const state = this.gameState$.value;
    
    if (!state.sessionId) {
      throw new Error('No active game session');
    }

    try {
      const response = await this.apiService.getFinalScore(state.sessionId);
      
      this.updateGameState({
        isGameActive: false
      });

      return response;
    } catch (error) {
      console.error('Failed to get final score:', error);
      throw error;
    }
  }

  /**
   * Reset game state for restart
   */
  resetGameState() {
    this.gameState$.next({
      sessionId: null,
      userId: null,
      username: '',
      difficulty: 'beginner',
      currentQuestion: 0,
      totalQuestions: 0,
      score: 0,
      streak: 0,
      maxStreak: 0,
      correctAnswers: 0,
      isGameActive: false
    });
  }
}
