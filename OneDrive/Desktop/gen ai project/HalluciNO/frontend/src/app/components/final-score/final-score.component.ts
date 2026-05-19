import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { GameService } from '../../services/game.service';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

// Final score page component
@Component({
  selector: 'app-final-score',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './final-score.component.html',
  styleUrls: ['./final-score.component.scss']
})
export class FinalScoreComponent implements OnInit {
  finalScore: any = null;
  isLoading: boolean = true;
  username: string = '';
  achievements: any[] = [];
  showShareModal: boolean = false;

  constructor(
    private gameService: GameService,
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit() {
    // Get current user
    const user = this.authService.getCurrentUserSync();
    if (!user) {
      this.router.navigate(['/login']);
      return;
    }
    
    this.username = user.username;
    this.loadFinalScore();
  }

  /**
   * Load final score from game service
   */
  async loadFinalScore() {
    try {
      this.finalScore = await this.gameService.getFinalScore();
      // Extract achievements from response
      this.achievements = this.finalScore.achievements || [];
    } catch (error) {
      console.error('Failed to load final score:', error);
      // Fallback if no game session
      this.router.navigate(['/home']);
    } finally {
      this.isLoading = false;
    }
  }

  /**
   * Get accuracy status message
   */
  getAccuracyMessage(): string {
    if (!this.finalScore) return '';
    
    const acc = this.finalScore.accuracy_percentage;
    if (acc >= 90) return '🌟 Perfect! You are an AI expert!';
    if (acc >= 80) return '💪 Excellent! Great AI knowledge!';
    if (acc >= 70) return '✨ Good! Keep improving!';
    if (acc >= 60) return '👍 Not bad! Try again!';
    return '🎮 Keep playing to improve!';
  }

  /**
   * Share score on social media
   */
  shareScore() {
    if (!this.finalScore) return;
    
    const text = `I scored ${this.finalScore.final_score} points on HalluciNO! 
Accuracy: ${this.finalScore.accuracy_percentage}% ${this.finalScore.badge}
Can you spot more AI hallucinations? 🤖🎮`;
    
    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`;
    window.open(twitterUrl, '_blank');
  }

  /**
   * Generate shareable score card
   */
  getShareText(): string {
    if (!this.finalScore) return '';
    
    let shareText = `🎯 I just scored on HalluciNO!\n\n`;
    shareText += `Score: ${this.finalScore.final_score} points\n`;
    shareText += `Accuracy: ${this.finalScore.accuracy_percentage}%\n`;
    shareText += `Streak: 🔥 ${this.finalScore.max_streak}\n`;
    shareText += `${this.finalScore.badge}\n\n`;
    
    // Add achievements
    if (this.achievements.length > 0) {
      shareText += `Badges Earned:\n`;
      this.achievements.forEach(achievement => {
        shareText += `${achievement.icon} ${achievement.name}\n`;
      });
      shareText += `\n`;
    }
    
    shareText += `Can you beat my score? Play now! 🚀`;
    
    return shareText;
  }

  /**
   * Copy share text to clipboard
   */
  copyShareText() {
    navigator.clipboard.writeText(this.getShareText());
  }

  /**
   * Share on Twitter/X
   */
  shareOnTwitter() {
    const text = this.getShareText();
    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`;
    window.open(twitterUrl, '_blank');
  }

  /**
   * Share on LinkedIn
   */
  shareOnLinkedIn() {
    const text = this.getShareText();
    const linkedInUrl = `https://www.linkedin.com/feed/?showShareModal=true`;
    // Note: LinkedIn share is limited, just open profile
    window.open(linkedInUrl, '_blank');
  }

  /**
   * Toggle share modal
   */
  toggleShareModal() {
    this.showShareModal = !this.showShareModal;
  }

  /**
   * Copy score to clipboard
   */
  copyScore() {
    const text = `HalluciNO Score: ${this.finalScore.final_score}pts | Accuracy: ${this.finalScore.accuracy_percentage}% ${this.finalScore.badge}`;
    navigator.clipboard.writeText(text);
  }

  /**
   * Play again
   */
  playAgain() {
    this.gameService.resetGameState();
    this.router.navigate(['/home']);
  }

  /**
   * View leaderboard
   */
  viewLeaderboard() {
    this.router.navigate(['/leaderboard']);
  }

  /**
   * Go home
   */
  goHome() {
    this.gameService.resetGameState();
    this.router.navigate(['/home']);
  }
}
