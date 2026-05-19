import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

// Leaderboard component
@Component({
  selector: 'app-leaderboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.scss']
})
export class LeaderboardComponent implements OnInit {
  leaderboard: any[] = [];
  isLoading: boolean = true;
  totalPlayers: number = 0;

  constructor(
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit() {
    this.loadLeaderboard();
  }

  /**
   * Load leaderboard data
   */
  async loadLeaderboard() {
    try {
      const response = await this.apiService.getLeaderboard(20);
      this.leaderboard = response.leaderboard;
      this.totalPlayers = response.total_players;
    } catch (error) {
      console.error('Failed to load leaderboard:', error);
    } finally {
      this.isLoading = false;
    }
  }

  /**
   * Get medal icon for rank
   */
  getMedalIcon(rank: number): string {
    switch (rank) {
      case 1:
        return '🥇';
      case 2:
        return '🥈';
      case 3:
        return '🥉';
      default:
        return `#${rank}`;
    }
  }

  /**
   * Get color class for rank
   */
  getRankClass(rank: number): string {
    switch (rank) {
      case 1:
        return 'rank-gold';
      case 2:
        return 'rank-silver';
      case 3:
        return 'rank-bronze';
      default:
        return 'rank-default';
    }
  }

  /**
   * Go back to home
   */
  goHome() {
    this.router.navigate(['/home']);
  }
}
