# 🚀 HalluciNO - Developer Quick Reference

Quick copy-paste reference for common commands and code snippets.

## ⚡ Quick Commands

### Backend Setup & Run

```bash
# Windows
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py

# macOS/Linux
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Frontend Setup & Run

```bash
cd frontend
npm install
npm start
```

### Stop Servers

```bash
# Backend: Press Ctrl+C in terminal
# Frontend: Press Ctrl+C in terminal
```

### Build for Production

```bash
# Backend: Already production-ready
# Frontend:
cd frontend
npm run build
```

---

## 🔗 Local URLs

```
Frontend (Dev):        http://localhost:4200
Backend (Dev):         http://localhost:8000
API Docs (Swagger):    http://localhost:8000/docs
API Alternative Docs:  http://localhost:8000/redoc
Health Check:          http://localhost:8000/health
```

---

## 📝 Common Code Snippets

### Add New Question (Backend)

```python
# File: backend/app/data/questions.py
# Add to QUESTIONS list:

Question(
    id=51,  # Must be unique
    question="Is this statement true or false?",
    category="Generative AI",  # Pick existing category
    is_hallucination=False,  # True if false statement
    explanation="This is true because...",
    difficulty=Difficulty.BEGINNER  # BEGINNER, INTERMEDIATE, EXPERT
),
```

### Change Theme Color (Frontend)

```scss
// File: frontend/src/styles.scss
// Edit :root section:

:root {
  --primary: #ff006e; /* Main color */
  --secondary: #00d9ff; /* Accent */
  --success: #00ff88; /* Success */
  --warning: #ffb60f; /* Warning */
  --bg-primary: #0a0e27; /* Dark background */
}
```

### Make API Call (Frontend)

```typescript
// In a component:
const response = await this.apiService.login(username);

// Available methods in api.service.ts:
await this.apiService.login(username);
await this.apiService.getCategories();
await this.apiService.startGame(userId, difficulty);
await this.apiService.getNextQuestion(sessionId);
await this.apiService.submitAnswer(sessionId, answerData);
await this.apiService.getFinalScore(sessionId);
await this.apiService.getLeaderboard(limit);
```

### Add New Angular Component

```bash
# Generate component structure
cd frontend
ng generate component components/my-component

# Folder structure created:
# src/app/components/my-component/
# ├── my-component.component.ts
# ├── my-component.component.html
# └── my-component.component.scss
```

### Access Game State (Frontend)

```typescript
// In any component:
import { GameService } from '../../services/game.service';

constructor(private gameService: GameService) {}

// Get state as Observable
this.gameService.getGameState().subscribe(state => {
  console.log(state);
});

// Get state synchronously
const state = this.gameService.getCurrentState();
console.log(state.score);
```

### Add New API Endpoint (Backend)

```python
# File: backend/app/routes/game.py
# Add to router:

@router.get("/my-endpoint/{param}")
async def my_endpoint(param: str):
    """
    Description of what this does
    """
    return {
        "status": "success",
        "data": "response"
    }

# Access at: GET /api/game/my-endpoint/value
```

---

## 🎨 Common CSS Patterns

### Center Content

```scss
.container {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### Button Style

```scss
.btn {
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-2px);
  }
}
```

### Responsive Grid

```scss
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}
```

### Animation

```scss
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.element {
  animation: slideIn 0.5s ease;
}
```

---

## 🧪 Testing Checklist

```bash
# 1. Start both servers
# Terminal 1:
cd backend && python run.py

# Terminal 2:
cd frontend && npm start

# 2. Test in browser
# - Login page loads
# - Can enter username
# - Can click "Let's Play"
# - Game page loads with question
# - Can click answer buttons
# - Score updates
# - Timer counts down
# - Can complete game
# - Final score shows
# - Can view leaderboard

# 3. Check console (F12)
# - No red errors
# - No warnings (if possible)

# 4. Check API (http://localhost:8000/docs)
# - Try endpoints manually
# - Verify responses
```

---

## 🔧 Git Commands

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Add feature description"

# View status
git status

# View log
git log

# Ignore file
# Add to .gitignore
```

---

## 🐛 Debug Tips

### Backend Debugging

```python
# Add debug prints in routes
print(f"Debug: {variable_name}")
print(f"State: {game_sessions}")

# Use Python debugger
import pdb; pdb.set_trace()
```

### Frontend Debugging

```typescript
// Add console logs
console.log("Debug:", data);
console.error("Error:", error);

// Use debugger
debugger; // Breaks execution

// Check state
console.log(this.gameState);
```

### Browser DevTools (F12)

- Network tab: Check API requests/responses
- Console tab: See errors and logs
- Elements tab: Inspect HTML
- Application tab: Check localStorage

---

## 📦 Dependency Updates

### Backend

```bash
cd backend
# List outdated packages
pip list --outdated

# Update single package
pip install --upgrade fastapi

# Update all (be careful!)
pip install --upgrade -r requirements.txt
```

### Frontend

```bash
cd frontend
# Check outdated packages
npm outdated

# Update single package
npm install --upgrade angular

# Update all
npm update
```

---

## 🌐 API Response Examples

### Login

```json
{
  "success": true,
  "user_id": "a1b2c3d4",
  "username": "Player123",
  "message": "Welcome Player123! Let's play HalluciNO!"
}
```

### Get Question

```json
{
  "question_number": 1,
  "total_questions": 10,
  "category": "Machine Learning",
  "question": "Neural networks always perform better...",
  "question_id": 1,
  "difficulty": "beginner"
}
```

### Submit Answer

```json
{
  "is_correct": true,
  "feedback": "🔥 Nailed it!",
  "explanation": "This is false because...",
  "current_score": 10,
  "streak": 1,
  "game_completed": false,
  "progress": "1/10"
}
```

### Final Score

```json
{
  "final_score": 100,
  "total_questions": 10,
  "correct_answers": 10,
  "accuracy_percentage": 100.0,
  "max_streak": 10,
  "badge": "🏆 AI Master",
  "category_breakdown": {
    "Machine Learning": "3/3",
    "Generative AI": "4/4"
  }
}
```

---

## 📋 Environment Variables

### Backend (.env)

```
DEBUG=False
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:4200
```

### Frontend (.env)

```
NG_APP_API_URL=http://localhost:8000/api
```

---

## 🎯 Common Issues & Solutions

| Issue                 | Solution                                               |
| --------------------- | ------------------------------------------------------ |
| Port 8000 in use      | `lsof -i :8000` then kill process                      |
| Port 4200 in use      | Use `ng serve --port 4300`                             |
| Module not found      | Run `npm install` or `pip install -r requirements.txt` |
| CORS error            | Backend already configured, check API URL in frontend  |
| Questions not loading | Check backend is running, verify API endpoint          |
| Blank page            | Check browser console (F12) for errors                 |
| Timeout error         | Check both servers are running                         |

---

## 📚 File Locations

| What       | Where                                       |
| ---------- | ------------------------------------------- |
| Questions  | `backend/app/data/questions.py`             |
| Colors     | `frontend/src/styles.scss`                  |
| Routes     | `frontend/src/app/app.routes.ts`            |
| Auth       | `frontend/src/app/services/auth.service.ts` |
| API        | `frontend/src/app/services/api.service.ts`  |
| Game logic | `backend/app/routes/game.py`                |
| Models     | `backend/app/models/models.py`              |

---

## 🚀 Quick Deploy Checklist

- [ ] Update API URL in frontend for production
- [ ] Set DEBUG=False in backend
- [ ] Update CORS origins in backend
- [ ] Build frontend: `npm run build`
- [ ] Test production build locally
- [ ] Push to GitHub
- [ ] Deploy backend to Render
- [ ] Deploy frontend to Vercel
- [ ] Test deployed app
- [ ] Share with friends!

---

## 📞 Emergency Help

```
Can't run backend?
→ Check Python installed: python --version
→ Check venv activated: should see (venv) in terminal
→ Check dependencies: pip list

Can't run frontend?
→ Check Node installed: node --version
→ Check npm installed: npm --version
→ Check dependencies: npm list

Frontend not connecting to backend?
→ Check backend running: http://localhost:8000/health
→ Check API URL in api.service.ts
→ Check CORS in backend/app/main.py
→ Check browser console (F12) for errors
```

---

**Bookmark this page! You'll need it! 📌**
