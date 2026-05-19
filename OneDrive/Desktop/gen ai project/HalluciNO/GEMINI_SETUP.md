# 🎮 HalluciNO - Gemini Integration Setup Guide

## ✨ What's New

- **Dynamic question generation** using Gemini 2.0 Flash API
- **No more hardcoded questions** - fresh questions every game
- **Free tier support** - 15 requests/minute included
- **Fallback system** - Static questions available if Gemini fails

---

## 🔑 Step 1: Get Your Free Gemini API Key

1. Go to: **https://aistudio.google.com/app/apikey**
2. Click **"Create API Key"** (free, no credit card required!)
3. Copy your API key

---

## 🔧 Step 2: Add API Key to `.env` File

1. Open: `backend/.env`
2. Replace `your_api_key_here` with your actual API key:
   ```
   GEMINI_API_KEY=sk-...your-api-key-here...
   ```
3. Save the file (backend server will auto-reload)

---

## 🎯 Step 3: Use Dynamic Questions in Frontend

### Option A: Start Game with Dynamic Questions

When calling `/start/{user_id}`, add:

```javascript
POST /game/start/user123?use_dynamic=true&difficulty=intermediate&question_count=10
```

### Option B: Generate Single Question

```javascript
GET /game/generate-question?category=Generative%20AI&difficulty=intermediate
```

### Option C: Generate Batch (5 questions)

```javascript
GET /game/generate-batch?count=5&difficulty=expert
```

---

## 📊 Gemini 2.0 Flash Specs

| Feature           | Details                       |
| ----------------- | ----------------------------- |
| **Model**         | gemini-2.0-flash              |
| **Free Tier**     | 15 requests/min, 1500/day     |
| **Response Time** | ~1-2 seconds per question     |
| **Cost**          | FREE (with free tier)         |
| **Quality**       | Excellent for AI/ML questions |

---

## 🔄 How It Works

```
User starts game with use_dynamic=true
        ↓
Backend calls Gemini 2.0 Flash
        ↓
Gemini generates AI hallucination question
        ↓
Question saved to database for persistence
        ↓
User plays with fresh, dynamic questions!
```

---

## ❓ Frequently Asked Questions

**Q: What if Gemini API fails?**  
A: Automatically falls back to static questions - game continues seamlessly!

**Q: Will questions repeat?**  
A: No! Gemini generates unique questions each time.

**Q: Do I need to pay?**  
A: No! Free tier includes 1500 requests/day, perfect for quiz games.

**Q: Can I mix static and dynamic?**  
A: Yes! Set `use_dynamic=false` to use static only, `use_dynamic=true` for Gemini.

---

## 🚀 To Test It Now

### Test 1: Generate Single Question

```bash
curl "http://localhost:8000/game/generate-question?category=Generative%20AI&difficulty=beginner"
```

### Test 2: Start Game with Dynamic Questions

```bash
curl -X POST "http://localhost:8000/game/start/testuser?use_dynamic=true&difficulty=intermediate&question_count=5"
```

### Test 3: Check Gemini Status

Look at response to see `"question_source": "gemini-2.0-flash"`

---

## 📝 Frontend Integration Example

In your Angular game component:

```typescript
// Start game with dynamic questions
startGameWithGemini() {
  this.apiService.startGame('user123', 'intermediate', 10, true).subscribe(
    (response) => {
      console.log('Using questions from:', response.question_source);
      this.sessionId = response.session_id;
    }
  );
}
```

---

## ⚙️ Troubleshooting

**Issue: "Gemini API not configured"**

- Solution: Add `GEMINI_API_KEY` to `.env` file

**Issue: Slow question generation**

- Solution: Normal for Gemini (1-2 sec), can cache questions in frontend

**Issue: Questions not changing**

- Solution: Gemini might generate similar questions - it's random!

---

## 🎓 Question Categories Available

- Machine Learning
- Generative AI
- AI Agents
- Prompt Engineering
- LangChain
- LangGraph
- RAG
- Hallucinations
- Neural Networks
- Open Source LLMs

---

## 📚 API Endpoints

| Endpoint                           | Method | Purpose                              |
| ---------------------------------- | ------ | ------------------------------------ |
| `/game/categories`                 | GET    | List all categories                  |
| `/game/generate-question`          | GET    | Get single Gemini question           |
| `/game/generate-batch`             | GET    | Get 5-10 Gemini questions            |
| `/game/start/{user_id}`            | POST   | Start game (add `?use_dynamic=true`) |
| `/game/question/{session_id}`      | GET    | Get next question                    |
| `/game/submit-answer/{session_id}` | POST   | Submit answer                        |
| `/game/final-score/{session_id}`   | GET    | Get score & leaderboard entry        |
| `/game/leaderboard`                | GET    | View all-time leaderboard            |

---

## 🎉 You're All Set!

Your game now uses **Gemini 2.0 Flash** for unlimited, unique, AI-generated questions! 🚀
