# HalluciNO Deployment Guide

## Quick Deploy (30 Min)

### 1. Frontend Deployment (Vercel) - 5 min

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy from frontend folder
cd frontend
vercel --prod
```

- Use default settings
- Set `BACKEND_API_URL` environment variable to your Railway backend URL

### 2. Backend Deployment (Railway) - 10 min

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize Railway project
cd backend
railway init

# Deploy
railway up
```

- Railway will automatically detect Python/FastAPI
- Database will be created on Railway

### 3. GitHub Push - 5 min

```bash
# Add, commit, and push
git add .
git commit -m "Add QR code feature and deployment configs"
git push origin main
```

### 4. Link Services - 10 min

- Update frontend env var with Railway backend URL
- Test QR code sharing feature
- Verify database connection

## Key Features

✅ QR code for easy sharing
✅ Dark mode support  
✅ Answer visibility fixed in dark mode
✅ Question count selection working
✅ Database schema fixed

## Env Variables

**Frontend (.env):**

```
VITE_API_URL=https://your-railway-backend.up.railway.app
```

**Backend (.env):**

```
DATABASE_URL=sqlite:///./halluci_no.db
GEMINI_API_KEY=your-key-here
```

## Support

- Vercel docs: https://vercel.com/docs
- Railway docs: https://railway.app/docs
- GitHub docs: https://docs.github.com
