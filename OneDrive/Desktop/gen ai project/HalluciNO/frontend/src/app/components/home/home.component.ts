import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { GameService } from '../../services/game.service';
import { ApiService } from '../../services/api.service';
// @ts-ignore
import QRCode from 'qrcode';

// Home page - game selection and setup
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, AfterViewInit {
  @ViewChild('qrCanvas', { static: false }) qrCanvas!: ElementRef<HTMLCanvasElement>;
  
  username: string = '';
  selectedDifficulty: string = 'beginner';
  selectedCategory: string = 'all';
  isLoading: boolean = false;
  categories: string[] = [];
  showRules: boolean = false;

  // Difficulty options
  difficulties = [
    { value: 'beginner', label: '🌱 Beginner', description: 'Easy questions' },
    { value: 'intermediate', label: '⚡ Intermediate', description: 'Medium difficulty' },
    { value: 'expert', label: '🔥 Expert', description: 'Hard questions' }
  ];

  // Question count options
  questionCounts = [5, 10, 15, 20];
  selectedQuestionCount: number = 10;

  constructor(
    private authService: AuthService,
    private gameService: GameService,
    private apiService: ApiService,
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
    this.loadCategories();
  }

  ngAfterViewInit() {
    // Generate QR code with game URL
    this.generateQRCode();
  }

  /**
   * Generate QR code for sharing game link
   */
  generateQRCode() {
    try {
      const gameUrl = window.location.origin;
      QRCode.toCanvas(
        this.qrCanvas.nativeElement,
        gameUrl,
        {
          width: 200,
          margin: 2,
          color: {
            dark: '#FF006E',
            light: '#0A0E27'
          },
          errorCorrectionLevel: 'H'
        },
        (error: any) => {
          if (error) {
            console.error('Error generating QR code:', error);
          }
        }
      );
    } catch (error) {
      console.error('QR code generation failed:', error);
    }
  }

  /**
   * Load available categories
   */
  async loadCategories() {
    try {
      const response = await this.apiService.getCategories();
      this.categories = response.categories;
    } catch (error) {
      console.error('Failed to load categories:', error);
    }
  }

  /**
   * Start game with selected difficulty and category
   */
  async startGame() {
    this.isLoading = true;

    try {
      const user = this.authService.getCurrentUserSync();
      
      // Start game with category parameter and question count
      await this.gameService.startGame(
        user.userId, 
        user.username, 
        this.selectedDifficulty,
        this.selectedCategory !== 'all' ? this.selectedCategory : undefined,
        this.selectedQuestionCount
      );
      
      // Navigate to game page
      this.router.navigate(['/game']);
    } catch (error) {
      console.error('Failed to start game:', error);
      this.isLoading = false;
    }
  }

  /**
   * View leaderboard
   */
  viewLeaderboard() {
    this.router.navigate(['/leaderboard']);
  }

  /**
   * Logout
   */
  logout() {
    this.authService.logout();
    this.router.navigate(['/login']);
  }

  /**
   * Toggle rules visibility
   */
  toggleRules() {
    this.showRules = !this.showRules;
  }
}
