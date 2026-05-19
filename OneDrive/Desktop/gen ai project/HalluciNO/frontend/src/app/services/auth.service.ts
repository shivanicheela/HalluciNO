import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

// Service for managing user authentication
@Injectable({ providedIn: 'root' })
export class AuthService {
  // Observable for tracking login state
  private isLoggedIn$ = new BehaviorSubject<boolean>(false);
  private currentUser$ = new BehaviorSubject<any>(null);

  constructor() {
    // Check for stored session on initialization
    this.restoreSession();
  }

  /**
   * Restore user session from localStorage
   */
  private restoreSession() {
    const storedUserId = localStorage.getItem('userId');
    const storedUsername = localStorage.getItem('username');

    if (storedUserId && storedUsername) {
      this.isLoggedIn$.next(true);
      this.currentUser$.next({
        userId: storedUserId,
        username: storedUsername
      });
    }
  }

  /**
   * Set user as logged in
   */
  setLoggedIn(userId: string, username: string) {
    // Save to localStorage for persistence
    localStorage.setItem('userId', userId);
    localStorage.setItem('username', username);

    this.isLoggedIn$.next(true);
    this.currentUser$.next({ userId, username });
  }

  /**
   * Log out user
   */
  logout() {
    localStorage.removeItem('userId');
    localStorage.removeItem('username');
    
    this.isLoggedIn$.next(false);
    this.currentUser$.next(null);
  }

  /**
   * Get login status observable
   */
  getIsLoggedIn() {
    return this.isLoggedIn$.asObservable();
  }

  /**
   * Get current user observable
   */
  getCurrentUser() {
    return this.currentUser$.asObservable();
  }

  /**
   * Get current user synchronously
   */
  getCurrentUserSync() {
    return this.currentUser$.value;
  }

  /**
   * Check if user is logged in
   */
  isUserLoggedIn(): boolean {
    return this.isLoggedIn$.value;
  }
}
