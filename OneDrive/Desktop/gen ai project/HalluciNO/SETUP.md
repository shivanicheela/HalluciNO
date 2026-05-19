# 📖 HalluciNO - Setup Guide

Step-by-step guide to set up HalluciNO locally for development.

## 📋 Prerequisites

Before starting, ensure you have:

- **Node.js** 18.0 or higher
  - Download: https://nodejs.org/
  - Verify: `node --version`

- **Python** 3.8 or higher
  - Download: https://www.python.org/
  - Verify: `python --version`

- **Git** (optional but recommended)
  - Download: https://git-scm.com/

- **Code Editor** (recommended: VS Code)
  - Download: https://code.visualstudio.com/

## 🔧 Installation Steps

### 1️⃣ Clone or Download Project

```bash
# Option 1: Clone from GitHub (if available)
git clone https://github.com/yourusername/halluci-no.git
cd HalluciNO

# Option 2: Download ZIP and extract
# Extract the ZIP file to your desired location
cd HalluciNO
```

### 2️⃣ Backend Setup

#### Windows

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

#### macOS/Linux

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### 3️⃣ Run Backend

```bash
# Make sure virtual environment is activated
# (you should see (venv) in your terminal)

# Run the FastAPI server
python run.py

# Or alternatively:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [12345]
```

**Backend is ready at:** http://localhost:8000

### 4️⃣ Frontend Setup

Open a **NEW terminal** window and:

```bash
# Navigate to frontend folder (from project root)
cd frontend

# Install Node dependencies
npm install

# This will take 2-3 minutes...
# You'll see lots of progress messages - this is normal!
```

**Expected Output:**

```
added XXX packages, and audited XXX packages
```

### 5️⃣ Run Frontend

```bash
# Make sure you're in the frontend folder
# Start the development server
npm start

# Or use ng command directly
ng serve
```

**Expected Output:**

```
⠙ Building...
✔ Compiled successfully. [XX% complete]
```

**Frontend is ready at:** http://localhost:4200

The app should automatically open in your browser!

## ✅ Testing Your Setup

### Backend API Testing

1. Open http://localhost:8000 in browser
   - Should see welcome message ✅

2. Open http://localhost:8000/docs
   - Interactive API documentation ✅
   - You can test endpoints here!

3. Test health endpoint
   ```bash
   curl http://localhost:8000/health
   ```
   Expected response: `{"status":"healthy"}`

### Frontend Testing

1. Open http://localhost:4200 in browser
   - Should see HalluciNO login page ✅
   - Try entering a username
   - Click "Let's Play!" button

2. Check browser console for errors
   - Press F12 to open DevTools
   - Go to Console tab
   - Should be no red errors ✅

### Full Gameplay Test

1. Login with any username
2. Select difficulty level
3. Click "Let's Play!"
4. Answer a question
5. See feedback and score
6. Complete the game
7. View final score
8. Check leaderboard

## 🛠️ Troubleshooting

### "Port 8000 already in use"

**Problem**: Another app using port 8000

**Solutions**:

```bash
# Find what's using port 8000
# Windows:
netstat -ano | findstr :8000

# macOS/Linux:
lsof -i :8000

# Use different port:
python run.py --port 8001
```

### "Port 4200 already in use"

**Problem**: Another app using port 4200

**Solutions**:

```bash
# Use different port:
ng serve --port 4300

# Visit http://localhost:4300
```

### "ModuleNotFoundError: No module named 'fastapi'"

**Problem**: Dependencies not installed

**Solutions**:

```bash
# Make sure virtual environment is activated
# (you should see (venv) in your terminal)

# Reinstall:
pip install -r requirements.txt
```

### "Cannot find module '@angular/core'"

**Problem**: Frontend dependencies not installed

**Solutions**:

```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Frontend shows blank page

**Problem**: Frontend not connecting to backend

**Solutions**:

1. Check backend is running (http://localhost:8000/health)
2. Check browser console (F12) for errors
3. Verify API URL in `frontend/src/app/services/api.service.ts`

### CORS Error in console

**Problem**: Frontend and backend on different ports

**Solution**: This is normal in development

- Backend already has CORS enabled
- Should work without additional config
- If still having issues, check `backend/app/main.py` CORS config

### Questions not loading

**Problem**: Backend not returning questions

**Solutions**:

1. Check backend logs for errors
2. Verify `/api/game/question/{session_id}` endpoint
3. Check if session was created properly

## 📁 Project Structure Review

```
HalluciNO/
├── frontend/
│   ├── src/
│   │   ├── app/            # Angular components and services
│   │   ├── styles.scss     # Global styles
│   │   └── index.html      # Entry page
│   ├── package.json        # npm dependencies
│   └── angular.json        # Angular config
│
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI app
│   │   ├── routes/         # API endpoints
│   │   ├── models/         # Data models
│   │   └── data/           # Questions database
│   ├── requirements.txt    # Python dependencies
│   └── run.py              # Entry point
│
├── README.md               # Main documentation
├── SETUP.md                # This file
└── DEPLOY.md               # Deployment guide
```

## 🎮 Gameplay Features

Once running, you can test:

- ✅ Login with any username
- ✅ Select difficulty (Beginner, Intermediate, Expert)
- ✅ Answer 5, 10, 15, or 20 questions
- ✅ See instant feedback
- ✅ View final score
- ✅ Check leaderboard
- ✅ Share your score

## 🔄 Stopping the Servers

### Backend

Press `CTRL + C` in the terminal running the backend

### Frontend

Press `CTRL + C` in the terminal running the frontend

## 📝 Common Commands

### Backend

```bash
# Activate virtual environment (Windows)
cd backend && venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
cd backend && source venv/bin/activate

# Run server
python run.py

# View requirements
pip list

# Update single package
pip install --upgrade fastapi
```

### Frontend

```bash
# Navigate to frontend
cd frontend

# Start dev server
npm start

# Build for production
npm run build

# Run tests
npm test

# Check for issues
ng lint
```

## 🚀 Next Steps

1. **Customize Questions**: Edit `backend/app/data/questions.py`
2. **Change Theme**: Edit `frontend/src/styles.scss`
3. **Add Features**: Follow Angular and FastAPI patterns in existing code
4. **Deploy**: Follow `DEPLOY.md` guide

## 📚 Learning Resources

### Angular

- https://angular.io/
- https://angular.io/guide/components
- https://angular.io/guide/routing

### FastAPI

- https://fastapi.tiangolo.com/
- https://fastapi.tiangolo.com/tutorial/
- https://pydantic-docs.helpmanual.io/

### TypeScript

- https://www.typescriptlang.org/docs/
- https://www.typescriptlang.org/play

### Python

- https://docs.python.org/3/
- https://realpython.com/

## 💡 Tips for Development

1. **Use VS Code**: Get extensions for Angular and Python
   - Angular: "Angular Language Service"
   - Python: "Python" by Microsoft

2. **Hot Reload**: Both frontend and backend auto-reload on file changes
   - Frontend: ng serve with --poll flag
   - Backend: run.py with --reload flag

3. **Debugging**:
   - Frontend: F12 DevTools
   - Backend: Add print statements or use debugger

4. **Code Organization**: Follow existing patterns
   - Services for API calls
   - Components for UI
   - Models for data structures

## 🆘 Still Having Issues?

1. Check error messages carefully
2. Review console logs (F12 for browser, terminal for backend)
3. Verify all prerequisites are installed
4. Try deleting and reinstalling node_modules/venv
5. Check internet connection
6. Try restarting your computer

## 📞 Support

- Check README.md for project overview
- Check DEPLOY.md for deployment help
- Review code comments for implementation details
- Google the error message - usually someone has solved it!

---

**You're all set! Happy coding! 🚀**
