# 🚀 HalluciNO - Deployment Guide

Complete guide for deploying HalluciNO to production.

## 📋 Table of Contents

1. [Local Deployment](#local-deployment)
2. [Docker Deployment](#docker-deployment)
3. [Vercel (Frontend)](#vercel-frontend)
4. [Render (Backend)](#render-backend)
5. [Environment Setup](#environment-setup)

---

## 📍 Local Deployment

### Prerequisites

- Node.js 18+
- Python 3.8+
- Virtual environment tool

### Step 1: Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py
```

**Backend Running**: http://localhost:8000

### Step 2: Frontend Setup

```bash
# Open new terminal, navigate to frontend
cd frontend

# Install dependencies
npm install

# Run development server
npm start
```

**Frontend Running**: http://localhost:4200

### Step 3: Test

1. Open http://localhost:4200 in your browser
2. Login with any username
3. Select difficulty and start playing
4. Check http://localhost:8000/docs for API documentation

---

## 🐳 Docker Deployment

### Prerequisites

- Docker installed
- Docker Compose installed

### Backend Docker Setup

Create `backend/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend Docker Setup

Create `frontend/Dockerfile`:

```dockerfile
# Build stage
FROM node:18-alpine as builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Production stage
FROM nginx:alpine

COPY --from=builder /app/dist/halluci-no /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

Create `frontend/nginx.conf`:

```nginx
server {
  listen 80;
  location / {
    root /usr/share/nginx/html;
    index index.html index.htm;
    try_files $uri $uri/ /index.html;
  }
}
```

### Docker Compose

Create `docker-compose.yml` in root:

```yaml
version: "3.8"

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    environment:
      - API_URL=http://backend:8000

volumes:
  backend_data:
```

### Run with Docker Compose

```bash
# Start all services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild
docker-compose up -d --build
```

---

## 🌐 Vercel (Frontend)

### Prerequisites

- Vercel account (free at vercel.com)
- GitHub repository

### Step 1: Prepare Frontend

```bash
cd frontend

# Update API URL in services
# File: src/app/services/api.service.ts
# Change: private apiUrl = 'http://localhost:8000/api';
# To: private apiUrl = 'https://your-backend-url/api';
```

### Step 2: Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# From frontend directory
vercel

# Follow prompts:
# - Connect GitHub account
# - Select project
# - Set build command: npm run build
# - Set output directory: dist/halluci-no
```

### Step 3: Configure Environment

In Vercel dashboard:

1. Go to Settings → Environment Variables
2. Add: `NG_API_URL=https://your-backend-url/api`

### Step 4: Update Frontend Build

Update `frontend/angular.json` build configuration:

```json
"build": {
  "configurations": {
    "production": {
      "fileReplacements": [
        {
          "replace": "src/environments/environment.ts",
          "with": "src/environments/environment.prod.ts"
        }
      ]
    }
  }
}
```

---

## 🎯 Render (Backend)

### Prerequisites

- Render account (free at render.com)
- GitHub repository

### Step 1: Create Web Service

1. Log in to Render
2. Click "New +"
3. Select "Web Service"
4. Connect your GitHub repository
5. Select the backend folder

### Step 2: Configure Service

```
Name: halluci-no-backend
Runtime: Python 3.11
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Step 3: Environment Variables

In Render dashboard, add under Environment:

```
PYTHONUNBUFFERED=1
CORS_ORIGINS=https://your-vercel-url.vercel.app
```

### Step 4: Deploy

1. Click "Create Web Service"
2. Wait for deployment (2-3 minutes)
3. Get the URL from Render dashboard

### Step 5: Update Frontend

Update `frontend/src/app/services/api.service.ts`:

```typescript
private apiUrl = 'https://your-render-url/api';
```

Redeploy frontend to Vercel.

---

## 🔧 Environment Setup

### Backend Environment Variables

Create `backend/.env`:

```env
# Server
DEBUG=False
HOST=0.0.0.0
PORT=8000

# CORS
CORS_ORIGINS=http://localhost:4200,https://your-vercel-url.vercel.app

# Optional: Gemini API
GEMINI_API_KEY=your_gemini_api_key
ENABLE_GEMINI=False

# Database (for future use)
DATABASE_URL=sqlite:///./halluci_no.db
```

### Frontend Environment Variables

Create `frontend/.env`:

```env
NG_APP_API_URL=http://localhost:8000/api
NG_APP_ENVIRONMENT=development
```

Create `frontend/src/environments/environment.prod.ts`:

```typescript
export const environment = {
  production: true,
  apiUrl: "https://your-backend-url/api",
};
```

---

## 📊 Production Checklist

- [ ] Update API URLs in frontend
- [ ] Enable CORS in backend for production domain
- [ ] Set DEBUG=False in backend
- [ ] Configure environment variables
- [ ] Test all API endpoints
- [ ] Test leaderboard functionality
- [ ] Test answer submission
- [ ] Test mobile responsiveness
- [ ] Monitor performance
- [ ] Set up error logging

---

## 🔍 Monitoring

### Backend Monitoring (Render)

- View logs in Render dashboard
- Check health endpoint: `https://your-url/health`
- Monitor request logs

### Frontend Monitoring (Vercel)

- View analytics in Vercel dashboard
- Check error logs
- Monitor page load times

---

## 🐛 Troubleshooting

### CORS Errors

**Problem**: "Access to XMLHttpRequest blocked by CORS"

**Solution**: Update CORS in `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-vercel-url.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### API Not Found

**Problem**: 404 on API endpoints

**Solution**: Verify backend URL in frontend:

```typescript
// Check in browser console
const apiUrl = "https://your-backend-url/api";
```

### Build Failures

**Problem**: Vercel/Render build fails

**Solution**:

1. Check build logs
2. Verify dependencies in package.json / requirements.txt
3. Check for environment variables

---

## 📈 Scaling

### For High Traffic

1. **Frontend**: Vercel automatically scales
2. **Backend**: Upgrade Render plan or use a load balancer
3. **Database**: Consider migrating from in-memory to PostgreSQL
4. **Caching**: Implement Redis for leaderboard

### Database Migration

Replace in-memory storage with PostgreSQL:

```bash
# Install dependencies
pip install sqlalchemy psycopg2-binary

# Update models.py and routes
```

---

## 🔐 Security

### HTTPS

- Vercel provides free HTTPS
- Render provides free HTTPS
- No additional setup needed

### API Rate Limiting

Add to `backend/app/main.py`:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
```

### Input Validation

Already implemented with Pydantic models.

---

## 📞 Support

For deployment issues:

1. Check Render/Vercel logs
2. Verify environment variables
3. Test API endpoints manually
4. Check CORS configuration

---

**Happy Deploying! 🚀**
