# 🚀 HalluciNO Deployment Guide - Complete Steps

## STEP 1: GITHUB PUSH (5 minutes)

### 1.1 Initialize Git (if not done)

```bash
cd "C:\Users\shiva\OneDrive\Desktop\gen ai project\HalluciNO"
git init
git remote add origin https://github.com/YOUR_USERNAME/HalluciNO.git
```

### 1.2 Add, Commit, Push

```bash
git add .
git commit -m "HalluciNO game with QR code, dark mode fixes, and deployment configs"
git branch -M main
git push -u origin main
```

**What to do:**

1. Create repo on GitHub.com (Settings → New repository)
2. Name it "HalluciNO"
3. Copy the HTTPS URL
4. Replace `https://github.com/YOUR_USERNAME/HalluciNO.git` with your URL
5. Run commands above in PowerShell

---

## STEP 2: VERCEL DEPLOYMENT - FRONTEND (5-7 minutes)

### 2.1 Connect Vercel to GitHub

1. Go to https://vercel.com
2. Click "Sign up" → "Continue with GitHub"
3. Authorize Vercel to access your GitHub

### 2.2 Import Project

1. Click "Add New..." → "Project"
2. Select your "HalluciNO" repository
3. Click "Import"

### 2.3 Configure Build Settings

- **Framework Preset:** Angular
- **Build Command:** `npm run build`
- **Output Directory:** `dist`
- **Install Command:** `npm install`

### 2.4 Set Environment Variables

Before deploying, add:

| Name           | Value                                               |
| -------------- | --------------------------------------------------- |
| `VITE_API_URL` | `http://localhost:8000` (dev) or Railway URL (prod) |

1. Click "Environment Variables"
2. Add the above
3. Click "Deploy"

**Wait for deployment to complete** ✅ (Green checkmark)

### 2.5 Get Your Frontend URL

- After deployment, Vercel shows: `https://halluci-no.vercel.app`
- Copy this URL - you'll need it for Railway

---

## STEP 3: RAILWAY DEPLOYMENT - BACKEND (5-7 minutes)

### 3.1 Create Railway Account

1. Go to https://railway.app
2. Sign up with GitHub
3. Authorize Railway

### 3.2 Create New Project

1. Click "Create New Project"
2. Select "Deploy from GitHub"
3. Find and select your "HalluciNO" repository
4. Select `backend` as the root directory

### 3.3 Configure Environment

Railway should auto-detect Python/FastAPI.

**Add Environment Variables:**

1. Click "Variables"
2. Add:

| Name             | Value                                                  |
| ---------------- | ------------------------------------------------------ |
| `GEMINI_API_KEY` | Your Gemini API key (optional, uses fallback if empty) |
| `DATABASE_URL`   | `sqlite:///./halluci_no.db`                            |

3. Click "Deploy"

**Wait for deployment** ✅ (Green status)

### 3.4 Get Your Backend URL

- In Railway Dashboard, click your project
- Find "Service URL" (looks like: `https://your-app-randomid.up.railway.app`)
- Copy this URL

---

## STEP 4: CONNECT FRONTEND TO BACKEND

### 4.1 Update Vercel Environment Variable

1. Go back to Vercel Dashboard
2. Click your project
3. Click "Settings" → "Environment Variables"
4. Update `VITE_API_URL` to your Railway URL:
   ```
   https://your-app-randomid.up.railway.app
   ```
5. Click "Save" → Vercel auto-redeploys

### 4.2 Verify Connection

1. Open your Vercel URL
2. Login and play a game
3. If it works → ✅ Connected!

---

## QUICK COMMAND REFERENCE

### Git Push

```bash
cd HalluciNO
git add .
git commit -m "Deploy with QR code and dark mode"
git push
```

### Test Locally (Before Deploying)

```bash
# Terminal 1 - Backend
cd backend
python run.py

# Terminal 2 - Frontend
cd frontend
npm install
npm start
# Open: http://localhost:50783
```

---

## ✅ VERIFICATION CHECKLIST

- [ ] GitHub repository created and pushed
- [ ] Vercel frontend deployed (green checkmark)
- [ ] Railway backend deployed (green status)
- [ ] Vercel env var set to Railway URL
- [ ] Can login on frontend
- [ ] Can play game (questions load)
- [ ] QR code displays on home page
- [ ] Dark mode text visible on buttons

---

## 🎯 FINAL DEPLOYMENT URLS

**Frontend:** https://halluci-no.vercel.app (or your custom domain)
**Backend:** https://your-app-randomid.up.railway.app
**QR Code:** Points to https://halluci-no.vercel.app

---

## TROUBLESHOOTING

### Frontend shows "Cannot GET /"

- Vercel build failed → Check build logs in Vercel dashboard
- Click "Deployments" → View logs

### Backend returns 500 error

- Database issue → Railway redeploys and recreates DB
- API key invalid → Gemini fallback works (uses hardcoded questions)
- Check Railway logs in "Recent Deploys"

### QR code not showing

- Refresh page (Ctrl+Shift+R)
- Check browser console (F12 → Console tab)

---

## ⏱️ TOTAL TIME: ~20 minutes

1. GitHub: 5 min
2. Vercel: 5-7 min
3. Railway: 5-7 min
4. Connect & Test: 3-5 min

**Go! 🚀**
