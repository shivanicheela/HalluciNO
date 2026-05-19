# 🤖 HalluciNO - AI Hallucination Detector Game

A fun, interactive full-stack web game where players test their AI knowledge by identifying whether statements about Generative AI, Machine Learning, and related technologies are truthful or hallucinations.

## 📋 Features

### 🎮 Gameplay
- **50+ Diverse Questions** covering GenAI, ML, LLMs, Prompt Engineering, and more
- **3 Difficulty Levels**: Beginner, Intermediate, Expert
- **Timed Questions**: 30-second countdown timer for each question
- **Streak System**: Build consecutive correct answers for bonus excitement
- **Real-time Feedback**: AI-generated funny responses for answers
- **Progress Tracking**: Visual progress bar and question counter

### 👥 Social Features
- **Global Leaderboard**: Compete with other players
- **Share Scores**: Tweet your achievements
- **Badges & Achievements**: Unlock badges based on performance
- **Player Statistics**: Accuracy percentage, max streak, and category breakdown

### 🎨 UI/UX
- **Dark Modern Theme**: Eye-friendly, gaming-inspired interface
- **Smooth Animations**: Transitions and visual effects
- **Mobile Responsive**: Fully optimized for all devices
- **Real-time Stats**: Live score and streak display
- **Category System**: Questions organized by AI/ML topics

## 📁 Project Structure

```
HalluciNO/
├── frontend/                    # Angular Application
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/     # Angular components
│   │   │   │   ├── login/      # Login page
│   │   │   │   ├── home/       # Home/menu page
│   │   │   │   ├── game/       # Main game/quiz
│   │   │   │   ├── leaderboard/# Leaderboard
│   │   │   │   └── final-score/# End game results
│   │   │   ├── services/       # API & state management
│   │   │   ├── app.routes.ts   # Routing configuration
│   │   │   └── app.component.ts# Root component
│   │   ├── styles.scss         # Global styles
│   │   └── index.html          # Entry HTML
│   ├── package.json            # Dependencies
│   ├── angular.json            # Angular config
│   └── tsconfig.json           # TypeScript config
│
├── backend/                     # FastAPI Application
│   ├── app/
│   │   ├── main.py            # FastAPI app entry
│   │   ├── models/
│   │   │   └── models.py      # Pydantic models
│   │   ├── routes/
│   │   │   ├── auth.py        # Authentication endpoints
│   │   │   └── game.py        # Game endpoints
│   │   ├── data/
│   │   │   └── questions.py   # 50+ quiz questions
│   │   └── __init__.py
│   ├── requirements.txt        # Python dependencies
│   ├── run.py                 # Entry point
│   └── .env                   # Environment variables
│
├── README.md                   # This file
├── SETUP.md                    # Setup instructions
└── DEPLOY.md                   # Deployment guide
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Git

### Backend Setup

```bash
# 1. Navigate to backend folder
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the backend
python run.py
```

Backend will be available at: **http://localhost:8000**
- API Docs: http://localhost:8000/docs

### Frontend Setup

```bash
# 1. Navigate to frontend folder
cd frontend

# 2. Install dependencies
npm install

# 3. Run development server
npm start
```

Frontend will be available at: **http://localhost:4200**

## 🎯 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `GET /api/auth/validate/{user_id}` - Validate session

### Game
- `GET /api/game/categories` - Get question categories
- `POST /api/game/start/{user_id}` - Start new game
- `GET /api/game/question/{session_id}` - Get next question
- `POST /api/game/submit-answer/{session_id}` - Submit answer
- `GET /api/game/final-score/{session_id}` - Get final score
- `GET /api/game/leaderboard` - Get top scores
- `POST /api/game/restart/{session_id}` - Restart game

## 📚 Question Categories

1. **Machine Learning** - Core ML concepts
2. **Generative AI** - LLMs, transformers, GANs
3. **AI Agents** - Autonomous systems and decision-making
4. **Prompt Engineering** - Techniques to optimize LLM outputs
5. **LangChain** - Framework for building LLM applications
6. **LangGraph** - Graph-based stateful workflows
7. **RAG (Retrieval-Augmented Generation)** - Knowledge base integration
8. **Hallucinations** - AI model limitations
9. **Neural Networks** - Deep learning fundamentals
10. **Open Source LLMs** - Community models and tools

## 🎮 Game Mechanics

### Scoring
- Correct answer: +10 points
- Streak bonus: Extra points for consecutive correct answers
- Difficulty multiplier: Higher difficulty = more points

### Streak System
- 🔥 Visible streak counter during gameplay
- Max streak tracked and displayed
- Resets on wrong answer

### Accuracy Badges
- 🏆 AI Master: 90%+ accuracy
- 🥇 Hallucination Detective: 80-89%
- 🥈 AI Spotter: 70-79%
- 🥉 Beginner Skeptic: 60-69%
- 🤖 AI Fell for It: Below 60%

## 🛠️ Technology Stack

### Frontend
- **Angular 17** - Modern web framework
- **TypeScript** - Type-safe JavaScript
- **SCSS** - Advanced styling
- **RxJS** - Reactive programming

### Backend
- **FastAPI** - High-performance Python web framework
- **Pydantic** - Data validation
- **Python 3.8+** - Programming language
- **Uvicorn** - ASGI server

### Optional
- **Gemini API** - For dynamic question generation
- **Docker** - Containerization

## 📱 Responsive Design

The app is fully responsive and works on:
- 📱 Mobile phones (iOS, Android)
- 📱 Tablets
- 💻 Desktops
- 🖥️ Large monitors

## 🔒 Security

- CORS enabled for cross-origin requests
- Input validation on frontend and backend
- No sensitive data stored in localStorage
- Session IDs are temporary and non-persistent

## 🎨 Customization

### Change Colors
Edit `frontend/src/styles.scss` - CSS variables in `:root` section:
```scss
--primary: #FF006E;      /* Change main theme color */
--secondary: #00D9FF;    /* Change accent color */
```

### Add More Questions
Edit `backend/app/data/questions.py` - add to `QUESTIONS` list

### Adjust Difficulty
Modify scoring in `backend/app/routes/game.py`

## 📊 Monitoring

### Backend Logs
```bash
# Run with verbose logging
python run.py
```

### Frontend Console
Open browser DevTools (F12) to see frontend logs

## 🚢 Deployment

See [DEPLOY.md](DEPLOY.md) for:
- Vercel (Frontend)
- Render (Backend)
- Docker deployment
- Environment variable setup

## 🤝 Contributing

Feel free to fork and submit pull requests with improvements!

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Credits

Built with ❤️ for AI enthusiasts and learners!

## 📞 Support

For issues or questions:
1. Check the [SETUP.md](SETUP.md) guide
2. Review error messages in browser console
3. Check backend logs
4. Open an issue on GitHub

---

**Enjoy testing your AI knowledge! Can you spot the hallucinations? 🤖🎮**
