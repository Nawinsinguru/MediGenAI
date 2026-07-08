from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.core.settings import APP_NAME, APP_VERSION
from app.database.database import Base, engine
from app.models.user import User
from app.api.auth import router as auth_router
from app.api.reports import router as report_router
from app.api.upload import router as upload_router
from app.models.chat_history import ChatHistory

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(report_router)
app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "project": APP_NAME,
        "version": APP_VERSION,
        "status": "Running"
    }