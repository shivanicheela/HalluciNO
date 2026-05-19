import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

// Login page component
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  username: string = '';
  isLoading: boolean = false;
  errorMessage: string = '';

  constructor(
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
  ) {}

  /**
   * Handle login form submission
   */
  async handleLogin() {
    // Validate input
    if (!this.username.trim()) {
      this.errorMessage = 'Please enter a username!';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';

    try {
      // Call login API
      const response = await this.apiService.login(this.username);
      
      // Save auth state
      this.authService.setLoggedIn(response.user_id, response.username);
      
      // Navigate to home page
      this.router.navigate(['/home']);
    } catch (error) {
      this.errorMessage = 'Login failed. Please try again.';
      console.error('Login error:', error);
    } finally {
      this.isLoading = false;
    }
  }

  /**
   * Handle Enter key press
   */
  handleKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter' && !this.isLoading) {
      this.handleLogin();
    }
  }
}
