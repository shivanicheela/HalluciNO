import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ThemeService } from './services/theme.service';

// Root component - main app shell
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'HalluciNO';
  isDarkMode$ = this.themeService.darkMode$;

  constructor(private themeService: ThemeService) {}

  ngOnInit() {
    // Initialize theme on app startup
    this.themeService.isDarkMode();
  }

  toggleTheme() {
    this.themeService.toggleDarkMode();
  }
}
