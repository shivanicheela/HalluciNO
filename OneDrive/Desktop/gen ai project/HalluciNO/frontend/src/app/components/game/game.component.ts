import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { GameService } from '../../services/game.service';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';
import { Subscription } from 'rxjs';

// Main game/quiz component
@Component({
  selector: 'app-game',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit, OnDestroy {
  // Game state
  currentQuestion: any = null;
  gameState: any = null;
  isLoading: boolean = true;
  answeredCorrectly: boolean | null = null;
  feedback: string = '';
  explanation: string = '';
  showAnswer: boolean = false;
  username: string = '';
  showInstantFeedback: boolean = false;
  
  // Hints system
  hintsUsed: number = 0;
  maxHints: number = 2;
  currentHint: string | null = null;
  hintIndex: number = 0;
  
  // New features: Advanced scoring & probability
  hallucination_probability: number = 0;
  points_change: number = 0;
  streak_message: string = '';
  showProbabilityMeter: boolean = false;
  scoreAnimationClass: string = '';
  
  // Timer
  timeRemaining: number = 30;
  private timerInterval: any;
  private gameStateSubscription: Subscription | null = null;

  constructor(
    private gameService: GameService,
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit() {
    // Get username
    const user = this.authService.getCurrentUserSync();
    this.username = user?.username || 'Player';
    
    // Subscribe to game state
    this.gameStateSubscription = this.gameService.getGameState().subscribe(state => {
      this.gameState = state;
    });

    // Load first question
    this.loadNextQuestion();
  }

  /**
   * Load next question
   */
  async loadNextQuestion() {
    this.isLoading = true;
    this.showAnswer = false;
    this.answeredCorrectly = null;
    this.showInstantFeedback = false;
    this.timeRemaining = 30;
    this.hintsUsed = 0;
    this.currentHint = null;
    this.hintIndex = 0;

    try {
      this.currentQuestion = await this.apiService.getNextQuestion(
        this.gameState.sessionId
      );
      
      // Start timer
      this.startTimer();
    } catch (error: any) {
      if (error.message.includes('All questions completed')) {
        // Game completed - navigate to final score
        this.router.navigate(['/final-score']);
      } else {
        console.error('Failed to load question:', error);
      }
    } finally {
      this.isLoading = false;
    }
  }

  /**
   * Start countdown timer
   */
  private startTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    
    this.timerInterval = setInterval(() => {
      this.timeRemaining--;
      
      if (this.timeRemaining <= 0) {
        clearInterval(this.timerInterval);
        // Auto-submit wrong answer on timeout
        this.submitAnswer(false);
      }
    }, 1000);
  }

  /**
   * Submit answer
   */
  async submitAnswer(userAnswer: boolean) {
    if (!this.currentQuestion || this.showAnswer) return;

    // Clear timer
    if (this.timerInterval) clearInterval(this.timerInterval);

    // Calculate time taken
    const timeTaken = 30 - this.timeRemaining;

    this.isLoading = true;
    this.showAnswer = true;

    try {
      const response = await this.gameService.submitAnswer(
        this.currentQuestion.question_id,
        userAnswer,
        timeTaken
      );

      // Show feedback
      this.answeredCorrectly = response.is_correct;
      this.feedback = response.feedback;
      this.explanation = response.explanation;
      
      // New: Show advanced metrics
      this.hallucination_probability = response.hallucination_probability || 0;
      this.points_change = response.points_change || 0;
      this.streak_message = response.streak_message || '';
      this.showProbabilityMeter = true;
      
      // Animate score change
      this.scoreAnimationClass = this.points_change > 0 ? 'score-gain' : 'score-loss';

      // Wait 3 seconds before loading next question (was 2s, now 3s for animations)
      setTimeout(() => {
        if (response.game_completed) {
          this.router.navigate(['/final-score']);
        } else {
          this.loadNextQuestion();
        }
      }, 3500);
    } catch (error) {
      console.error('Failed to submit answer:', error);
      this.isLoading = false;
    }
  }

  /**
   * Get progress percentage
   */
  getProgress(): number {
    if (!this.gameState) return 0;
    return (this.gameState.currentQuestion / this.gameState.totalQuestions) * 100;
  }

  /**
   * Get timer color
   */
  getTimerColor(): string {
    if (this.timeRemaining > 10) return 'green';
    if (this.timeRemaining > 5) return 'orange';
    return 'red';
  }

  /**
   * Get category badge color
   */
  getCategoryBadgeClass(category: string): string {
    const categories = {
      'Machine Learning': 'badge-primary',
      'Generative AI': 'badge-success',
      'AI Agents': 'badge-warning',
      'Prompt Engineering': 'badge-primary',
      'LangChain': 'badge-success',
      'LangGraph': 'badge-warning',
      'RAG': 'badge-primary',
      'Hallucinations': 'badge-danger',
      'Neural Networks': 'badge-success',
      'Open Source LLMs': 'badge-warning'
    };
    return categories[category as keyof typeof categories] || 'badge-primary';
  }

  /**
   * Get next hint
   */
  getHint() {
    if (!this.currentQuestion || this.hintsUsed >= this.maxHints) return;
    
    const hints = this.currentQuestion.hints || [];
    if (hints.length === 0) return;

    if (this.hintIndex < hints.length) {
      this.currentHint = hints[this.hintIndex];
      this.hintIndex++;
      this.hintsUsed++;
      
      // Deduct points for hint
      if (this.gameState) {
        this.gameState.score = Math.max(0, this.gameState.score - 5);
      }
    }
  }

  /**
   * Check if hints are available
   */
  hasMoreHints(): boolean {
    return this.hintsUsed < this.maxHints && 
           this.currentQuestion?.hints && 
           this.hintIndex < this.currentQuestion.hints.length;
  }

  /**
   * Show instant feedback after answer
   */
  showFeedback() {
    return this.answeredCorrectly !== null;
  }

  /**
   * Open learn more resources about the topic
   */
  openLearnMore() {
    if (!this.currentQuestion) return;
    
    // Extract key topic from question or category
    const topic = this.currentQuestion.category || 'AI Learning';
    const searchQuery = `${topic} tutorial AI course`;
    
    // Open Google search in new tab with educational resources
    const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(searchQuery)}&tbm=vid`;
    window.open(searchUrl, '_blank');
  }

  ngOnDestroy() {
    // Cleanup
    if (this.timerInterval) clearInterval(this.timerInterval);
    if (this.gameStateSubscription) this.gameStateSubscription.unsubscribe();
  }
}
