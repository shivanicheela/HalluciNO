# 📑 HalluciNO - File Index & Navigation Guide

Quick reference guide to all files in the HalluciNO project.

## 📖 Documentation Files (START HERE!)

| File                                        | Purpose                         | Read First? |
| ------------------------------------------- | ------------------------------- | ----------- |
| [README.md](../README.md)                   | Project overview and features   | ✅ YES      |
| [PROJECT_SUMMARY.md](../PROJECT_SUMMARY.md) | Complete implementation summary | ✅ YES      |
| [SETUP.md](../SETUP.md)                     | Step-by-step setup guide        | ✅ NEXT     |
| [DEPLOY.md](../DEPLOY.md)                   | Deployment instructions         | After Setup |

---

## 🔧 Backend Files

### Entry Points

- `backend/main.py` - FastAPI application entry point
- `backend/run.py` - Backend startup script

### Routes (API Endpoints)

- `backend/app/routes/auth.py` - Login and authentication endpoints
  - `POST /api/auth/login` - User login
  - `GET /api/auth/validate/{user_id}` - Session validation

- `backend/app/routes/game.py` - Game logic and endpoints
  - `POST /api/game/start/{user_id}` - Start new game
  - `GET /api/game/question/{session_id}` - Get next question
  - `POST /api/game/submit-answer/{session_id}` - Submit answer
  - `GET /api/game/final-score/{session_id}` - Get final score
  - `GET /api/game/leaderboard` - Get top scores
  - More endpoints...

### Data & Models

- `backend/app/models/models.py` - Pydantic data models
  - `User`, `Question`, `GameSession`, `LeaderboardEntry`, etc.

- `backend/app/data/questions.py` - **50+ AI/ML questions**
  - Categories: ML, GenAI, Agents, Prompt Engineering, LangChain, RAG, etc.
  - Difficulty levels: Beginner, Intermediate, Expert

### Configuration

- `backend/requirements.txt` - Python dependencies
- `backend/.env.example` - Environment variables template

---

## 🎨 Frontend Files

### Main Application

- `frontend/src/main.ts` - Angular bootstrap
- `frontend/src/app/app.component.ts` - Root component
- `frontend/src/app/app.routes.ts` - Routing configuration
- `frontend/src/index.html` - HTML entry point

### Components (Pages)

#### Login Component

- `frontend/src/app/components/login/login.component.ts` - Logic
- `frontend/src/app/components/login/login.component.html` - Template
- `frontend/src/app/components/login/login.component.scss` - Styles

#### Home Component

- `frontend/src/app/components/home/home.component.ts` - Logic
- `frontend/src/app/components/home/home.component.html` - Template
- `frontend/src/app/components/home/home.component.scss` - Styles

#### Game Component (Quiz)

- `frontend/src/app/components/game/game.component.ts` - Quiz logic
- `frontend/src/app/components/game/game.component.html` - Quiz UI
- `frontend/src/app/components/game/game.component.scss` - Quiz styling

#### Final Score Component

- `frontend/src/app/components/final-score/final-score.component.ts` - Score logic
- `frontend/src/app/components/final-score/final-score.component.html` - Score UI
- `frontend/src/app/components/final-score/final-score.component.scss` - Score styling

#### Leaderboard Component

- `frontend/src/app/components/leaderboard/leaderboard.component.ts` - Leaderboard logic
- `frontend/src/app/components/leaderboard/leaderboard.component.html` - Leaderboard UI
- `frontend/src/app/components/leaderboard/leaderboard.component.scss` - Leaderboard styling

### Services (Business Logic)

- `frontend/src/app/services/api.service.ts` - HTTP API calls
  - `login()`, `startGame()`, `getNextQuestion()`, `submitAnswer()`, etc.

- `frontend/src/app/services/game.service.ts` - Game state management
  - `startGame()`, `submitAnswer()`, `getFinalScore()`, `resetGameState()`

- `frontend/src/app/services/auth.service.ts` - Authentication state
  - `setLoggedIn()`, `logout()`, `isUserLoggedIn()`, `getCurrentUser()`

### Styling & Assets

- `frontend/src/styles.scss` - **Global styles and theme**
  - CSS variables, animations, buttons, cards, responsive design
- `frontend/src/assets/` - Static assets folder (for images, sounds, etc.)

### Configuration

- `frontend/package.json` - NPM dependencies
- `frontend/angular.json` - Angular build config
- `frontend/tsconfig.json` - TypeScript config
- `frontend/tsconfig.app.json` - App-specific TypeScript config

---

## 🎯 Key Files to Modify

### To Add More Questions

Edit: `backend/app/data/questions.py`

- Add new `Question()` objects to the `QUESTIONS` list
- Follow existing pattern for category, difficulty, explanation

### To Change Theme Colors

Edit: `frontend/src/styles.scss`

- Modify CSS variables in `:root` section
- Colors: `--primary`, `--secondary`, `--success`, etc.

### To Adjust Scoring

Edit: `backend/app/routes/game.py`

- Look for scoring logic in `submitAnswer()` function
- Modify point values as needed

### To Add Custom Features

- Add routes in `backend/app/routes/`
- Add components in `frontend/src/app/components/`
- Add services in `frontend/src/app/services/`

---

## 🔐 Security Files

- `.gitignore` - Git ignore rules (don't commit sensitive files)
- `backend/.env.example` - Environment template (don't commit actual .env)

---

## 🚀 Deployment Files

### For Render (Backend)

```
Key file: backend/requirements.txt
Build: pip install -r requirements.txt
Start: uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### For Vercel (Frontend)

```
Key files: frontend/package.json, frontend/angular.json
Build: npm run build
Output: dist/halluci-no
```

---

## 📊 File Organization Summary

```
Backend Organization:
├── routes/        - API endpoints (organized by feature)
├── models/        - Data models (Pydantic)
├── data/          - Static data (questions)
└── main.py        - FastAPI app configuration

Frontend Organization:
├── components/    - Page components (one folder per page)
├── services/      - Business logic services
├── styles.scss    - Global styles
└── app.routes.ts  - Routing configuration
```

---

## 🎓 Code Reading Order (for Beginners)

1. **Start**: `PROJECT_SUMMARY.md` (overview)
2. **Setup**: `SETUP.md` (installation)
3. **Backend**:
   - `backend/app/main.py` (entry point)
   - `backend/app/routes/auth.py` (simple endpoints)
   - `backend/app/routes/game.py` (game logic)
4. **Frontend**:
   - `frontend/src/app/app.routes.ts` (routing)
   - `frontend/src/app/services/api.service.ts` (API calls)
   - `frontend/src/app/components/login/` (simple component)
   - `frontend/src/app/components/game/` (complex component)

---

## 🔍 Finding Things

### Need to...

**Add a new API endpoint?**
→ Edit `backend/app/routes/game.py`

**Change game questions?**
→ Edit `backend/app/data/questions.py`

**Fix UI styling?**
→ Edit `frontend/src/styles.scss` or component `.scss` file

**Add new page?**
→ Create folder in `frontend/src/app/components/`

**Modify scoring logic?**
→ Edit `backend/app/routes/game.py` `submitAnswer()` function

**Change authentication?**
→ Edit `frontend/src/app/services/auth.service.ts`

**Connect to real database?**
→ Replace in-memory storage in `backend/app/routes/game.py`

---

## 📞 Quick Links

- **API Documentation**: http://localhost:8000/docs (when running)
- **Angular Documentation**: https://angular.io/docs
- **FastAPI Documentation**: https://fastapi.tiangolo.com/docs
- **TypeScript Documentation**: https://www.typescriptlang.org/

---

## ✅ Checklist: Important Files to Know

- [ ] Read README.md
- [ ] Read SETUP.md
- [ ] Understand backend/app/main.py
- [ ] Understand frontend/src/app/app.component.ts
- [ ] Review backend/app/routes/auth.py
- [ ] Review backend/app/routes/game.py
- [ ] Review frontend/src/app/components/game/
- [ ] Understand frontend/src/app/services/api.service.ts
- [ ] Customize backend/app/data/questions.py
- [ ] Customize frontend/src/styles.scss

---

**Now you know where everything is! Happy coding! 🚀**
