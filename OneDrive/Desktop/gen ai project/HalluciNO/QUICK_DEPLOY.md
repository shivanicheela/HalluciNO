# 📋 QUICK DEPLOYMENT CHECKLIST

## ⚡ 3-STEP DEPLOYMENT

### STEP 1️⃣: GITHUB (Do First)
```
1. Go to github.com
2. Click "+" → "New repository"
3. Name: HalluciNO
4. Click "Create repository"
5. Copy the HTTPS URL

In PowerShell:
cd HalluciNO
git init
git remote add origin [paste-url-here]
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---

### STEP 2️⃣: VERCEL (Frontend)
```
1. Go to vercel.com
2. Click "Sign up" → "GitHub"
3. Click "Add New" → "Project"
4. Select HalluciNO repo
5. Keep defaults, click "Deploy"
6. Wait for ✅ green checkmark
7. Copy your URL: https://halluci-no.vercel.app
```

---

### STEP 3️⃣: RAILWAY (Backend)
```
1. Go to railway.app
2. Click "Sign up" → "GitHub"
3. Click "Create New Project"
4. Select "Deploy from GitHub"
5. Select HalluciNO repo
6. Set "Root Directory" to: backend
7. Add env vars (copy from Variables section):
   - GEMINI_API_KEY = your-key (optional)
   - DATABASE_URL = sqlite:///./halluci_no.db
8. Click "Deploy"
9. Wait for green status ✅
10. Copy "Service URL": https://your-app-xxx.up.railway.app
```

---

### STEP 4️⃣: CONNECT
```
Back in Vercel:
1. Click your project
2. Settings → Environment Variables
3. Find VITE_API_URL
4. Change value to Railway URL (from Step 3)
5. Save → Auto redeploys
6. Wait for green ✅
```

---

## 🧪 TEST
```
1. Open: https://halluci-no.vercel.app
2. Login with username
3. Play game
4. See QR code on home page
5. ✅ All working!
```

---

## 📱 SHARE
```
QR Code Link: https://halluci-no.vercel.app
Scan to play HalluciNO!
```

---

## ❌ IF SOMETHING BREAKS

**Frontend not loading?**
- Click "Deployments" in Vercel → View logs
- Look for red errors

**Backend error 500?**
- Check Railway Recent Deploys
- Database auto-recreates on deploy

**Questions not loading?**
- Backend URL wrong in Vercel env var
- Gemini API key missing (use fallback hardcoded Q's)

---

## ✅ YOU'RE DONE!

Frontend: Online ✅
Backend: Online ✅
QR Code: Working ✅
Database: Auto-created ✅
