# MediGenAI - Full Stack Setup Guide

This guide will help you set up and run both the backend and frontend of the MediGenAI application.

## Project Structure

```
MediGenAI/
├── backend/          # FastAPI backend server
│   ├── app/         # Main application
│   ├── requirements.txt
│   └── main.py
├── frontend/         # Vue 3 frontend application
│   ├── src/
│   ├── package.json
│   └── README.md
└── README.md
```

## Prerequisites

- Python 3.9+
- Node.js 18+ and npm
- Git

## Backend Setup

### 1. Navigate to Backend Directory

```bash
cd backend
```

### 2. Create Virtual Environment (Recommended)

**On Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Backend Server

```bash
uvicorn app.main:app --reload
```

The backend will be available at: **http://localhost:8000**

API Documentation: **http://localhost:8000/docs**

## Frontend Setup

### 1. Navigate to Frontend Directory (in a new terminal)

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run Development Server

```bash
npm run dev
```

The frontend will be available at: **http://localhost:5173**

## Quick Start

### Terminal 1 - Backend

```bash
cd backend
python -m venv venv

# Windows PowerShell
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Terminal 2 - Frontend

```bash
cd frontend
npm install
npm run dev
```

### Access the Application

1. Open your browser and go to: **http://localhost:5173**
2. Register a new account or login
3. Explore the features:
   - 💬 **Chat**: Ask medical questions
   - 📄 **Upload**: Upload PDF documents
   - 📋 **Reports**: Generate medical reports

## Features

### Authentication

- User registration and login
- JWT token-based authentication
- Secure password handling

### Medical Chat

- Real-time AI-powered chat interface
- Medical knowledge base integration
- Context-aware responses

### Document Management

- PDF upload and storage
- Document processing
- Knowledge base enhancement

### Report Generation

- Dynamic medical report creation
- Patient information capture
- AI-enhanced report generation

## API Endpoints

### Authentication

- `POST /auth/register` - Register new user
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user info

### Chat

- `POST /chat` - Send message and get AI response

### Documents

- `POST /upload/pdf` - Upload PDF file

### Reports

- `POST /reports/generate` - Generate medical report

## Building for Production

### Frontend Build

```bash
cd frontend
npm run build
```

Output will be in the `dist/` folder, ready for deployment.

### Backend Deployment

Update the CORS configuration in `backend/app/main.py` with your production domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yourdomain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Troubleshooting

### Port Already in Use

If port 8000 or 5173 is already in use:

```bash
# Backend - use different port
uvicorn app.main:app --reload --port 8001

# Frontend - Vite will automatically use next available port
npm run dev
```

### Module Not Found Errors

**Backend:**

```bash
# Ensure virtual environment is activated
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Then reinstall
pip install -r requirements.txt
```

**Frontend:**

```bash
npm install
```

### Database Issues

Delete the database and restart:

```bash
# Remove chroma_db and vector_db folders if they exist
rm -rf backend/chroma_db backend/vector_db
```

## Technologies Used

### Backend

- FastAPI - Modern Python web framework
- SQLAlchemy - ORM for database
- Pydantic - Data validation
- ChromaDB - Vector database for RAG
- Google Generative AI - LLM integration

### Frontend

- Vue 3 - Progressive JavaScript framework
- TypeScript - Type-safe JavaScript
- Tailwind CSS - Utility-first CSS framework
- Vite - Next generation frontend tooling
- Pinia - State management
- Vue Router - Client-side routing
- Axios - HTTP client

## Development Tips

### Hot Reload

Both the backend (with `--reload`) and frontend (Vite) support hot reload during development.

### API Documentation

Access Swagger UI at: **http://localhost:8000/docs**

### Vue DevTools

Install Vue DevTools extension in your browser for better debugging.

### TypeScript

The frontend uses TypeScript for type safety. Check for types errors:

```bash
cd frontend
npm run build  # Will show TypeScript errors if any
```

## Next Steps

1. Customize the medical knowledge base
2. Add more specialized AI models
3. Implement user roles and permissions
4. Add multi-language support
5. Deploy to production

## Support

For issues or questions, please check:

1. Backend logs in terminal
2. Browser console for frontend errors
3. Backend API docs at http://localhost:8000/docs
4. Ensure both services are running on correct ports

## License

MIT License
