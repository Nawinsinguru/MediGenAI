# 🚀 MediGenAI - Installation & Getting Started

## 🎯 What You Have

A complete, production-ready medical AI application with:

### Backend (Already Exists)

- FastAPI server with medical AI endpoints
- User authentication system
- PDF document processing
- Medical report generation
- AI chat interface

### Frontend (Just Created ✨)

- Vue 3 + TypeScript application
- Modern, responsive UI
- All required pages and features
- State management with Pinia
- API integration with Axios

## 📋 Installation (Step by Step)

### Step 1: Prerequisites Check

Make sure you have installed:

```bash
# Check Node.js (should be 18+)
node --version

# Check npm
npm --version

# Check Python (should be 3.9+)
python --version
```

If missing, install:

- [Node.js 18+](https://nodejs.org/)
- [Python 3.9+](https://www.python.org/)

### Step 2: Backend Setup (If Not Already Running)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

**Backend will run on**: `http://localhost:8000`

### Step 3: Frontend Installation

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install
```

### Step 4: Start Frontend Development Server

```bash
npm run dev
```

**Frontend will run on**: `http://localhost:5173`

### Step 5: Access the Application

Open your browser and go to:

```
http://localhost:5173
```

## ✨ First Time Setup

1. **Create Test Account**
   - Click "Create Account"
   - Fill in: Name, Email, Password
   - Click "Create Account"

2. **Login**
   - Enter your email and password
   - Click "Sign In"

3. **Explore Features**
   - Go to Chat tab → Ask medical questions
   - Go to Upload tab → Upload PDF files
   - Go to Reports tab → Generate medical reports

## 📁 Project Structure

```
MediGenAI/
├── backend/           ← Backend server (already setup)
│   ├── app/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/          ← Frontend (just created)
│   ├── src/
│   ├── package.json
│   └── README.md
│
└── Documentation files
```

## 🎨 Key Features

### Authentication

- ✅ Register new accounts
- ✅ Secure login
- ✅ Password protection
- ✅ Session management

### Chat Interface

- ✅ Real-time AI conversation
- ✅ Medical question answering
- ✅ Chat history
- ✅ Error handling

### Document Upload

- ✅ Drag & drop PDF upload
- ✅ File validation
- ✅ Progress tracking
- ✅ Document management

### Report Generation

- ✅ Patient information form
- ✅ Clinical findings input
- ✅ AI-powered reports
- ✅ Copy & download

## 🔧 Available Commands

### Frontend Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Install dependencies
npm install
```

### Backend Commands (in backend directory)

```bash
# Start server
uvicorn app.main:app --reload

# Access API documentation
# Open: http://localhost:8000/docs
```

## 🌐 API Endpoints

### User Authentication

```
POST   /auth/register          # Create account
POST   /auth/login             # Login user
GET    /auth/me                # Get user info
```

### Medical Chat

```
POST   /chat                   # Send message
```

### Document Upload

```
POST   /upload/pdf             # Upload PDF
```

### Reports

```
POST   /reports/generate       # Generate report
```

## ⚙️ Configuration

### Change Backend URL (if not localhost:8000)

Edit `src/utils/api.ts`:

```typescript
const API_BASE_URL = "http://your-backend-url:8000";
```

### Change Frontend Port

```bash
npm run dev -- --port 3000
```

### Change Backend Port

```bash
uvicorn app.main:app --reload --port 8001
```

## 🐛 Troubleshooting

### Port Already in Use

**For Frontend**:

```bash
npm run dev -- --port 3000
```

**For Backend**:

```bash
uvicorn app.main:app --reload --port 8001
```

### Dependencies Not Installing

```bash
# Clear cache
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

### Backend Connection Failed

1. Make sure backend is running
2. Check backend URL in `src/utils/api.ts`
3. Ensure CORS is enabled in backend
4. Check that ports are correct (8000 for backend, 5173 for frontend)

### Module Not Found (Backend)

```bash
# In backend directory, ensure venv is activated:

# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate

# Then reinstall:
pip install -r requirements.txt
```

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────┐
│              User Browser (localhost:5173)          │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │   Vue 3 Frontend Application                │   │
│  │                                             │   │
│  │  - Login/Register Pages                    │   │
│  │  - Chat Interface                          │   │
│  │  - Upload Manager                          │   │
│  │  - Report Generator                        │   │
│  │  - Dashboard                               │   │
│  └─────────────────────────────────────────────┘   │
│              │                                      │
│              │ HTTP Requests (Axios)               │
│              ▼                                      │
└─────────────────────────────────────────────────────┘
                   │
                   │ REST API
                   │
┌─────────────────────────────────────────────────────┐
│         FastAPI Backend (localhost:8000)            │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │   API Endpoints                             │   │
│  │                                             │   │
│  │  - /auth/* (Authentication)                 │   │
│  │  - /chat (Medical Chat)                     │   │
│  │  - /upload/* (PDF Upload)                   │   │
│  │  - /reports/* (Report Generation)           │   │
│  └─────────────────────────────────────────────┘   │
│              │                                      │
│              │                                      │
│    ┌─────────┼──────────┬──────────┐               │
│    ▼         ▼          ▼          ▼               │
│  ┌────┐  ┌────────┐  ┌────────┐  ┌───────┐       │
│  │ DB │  │ Vector │  │ ChromaDB  │Google │       │
│  │    │  │Storage │  │(RAG)   │  │GenAI  │       │
│  └────┘  └────────┘  └────────┘  └───────┘       │
└─────────────────────────────────────────────────────┘
```

## 🚀 Deployment Options

### Frontend Deployment

- Vercel (recommended for Vite)
- Netlify
- GitHub Pages
- AWS S3 + CloudFront
- Any static hosting

### Backend Deployment

- Heroku
- AWS EC2
- DigitalOcean
- Railway
- Render

## 💡 Tips for Development

1. **Keep DevTools Open**
   - Press F12 to open
   - Check Console for errors
   - Monitor Network requests

2. **Use TypeScript**
   - Get type hints in editor
   - Catch errors before runtime
   - Better code completion

3. **Check API Docs**
   - Backend: http://localhost:8000/docs
   - Useful for testing endpoints

4. **Hot Reload**
   - Frontend: Changes auto-refresh
   - Backend: Changes auto-reload with --reload flag

5. **Environment Variables**
   - Copy `.env.example` to `.env.local`
   - Add your configuration values

## 📚 Documentation Files

In the `frontend` folder:

- `README.md` - Feature documentation
- `DESIGN_SYSTEM.md` - UI guidelines
- `COMPONENT_REFERENCE.md` - Component API
- `PROJECT_SUMMARY.md` - Project overview

In the root folder:

- `SETUP_GUIDE.md` - Detailed setup guide
- `FRONTEND_COMPLETE.md` - Complete documentation

## ✅ Testing the Application

### Test Login

1. Go to `http://localhost:5173/login`
2. Click "Create Account"
3. Fill in test credentials
4. Click "Create Account"
5. Login with your credentials

### Test Chat

1. Go to Chat page
2. Type a medical question
3. Get AI response

### Test Upload

1. Go to Upload page
2. Drag a PDF or click to select
3. See upload progress
4. Confirm success

### Test Reports

1. Go to Reports page
2. Fill in patient information
3. Enter clinical findings
4. Click "Generate Report"
5. Copy or download report

## 🎉 You're Ready!

Everything is set up. Now you can:

1. ✅ Run the frontend
2. ✅ Run the backend
3. ✅ Create user accounts
4. ✅ Use all features
5. ✅ Customize as needed

## 📞 Quick Reference

| Task           | Command                         |
| -------------- | ------------------------------- |
| Start Frontend | `npm run dev`                   |
| Build Frontend | `npm run build`                 |
| Start Backend  | `uvicorn app.main:app --reload` |
| Open App       | `http://localhost:5173`         |
| API Docs       | `http://localhost:8000/docs`    |
| Install Deps   | `npm install`                   |

---

**Ready to go?** Run `npm run dev` and start exploring! 🚀

For detailed setup information, see `SETUP_GUIDE.md`
