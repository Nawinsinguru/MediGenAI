from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

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
    allow_origins=["*"],  # Change this to your domain later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(report_router)
app.include_router(upload_router)

# ==========================
# Serve Vue Frontend
# ==========================
STATIC_DIR = Path(__file__).parent / "static"

if STATIC_DIR.exists():
    assets_dir = STATIC_DIR / "assets"

    if assets_dir.exists():
        app.mount(
            "/assets",
            StaticFiles(directory=assets_dir),
            name="assets"
        )

    @app.get("/", include_in_schema=False)
    async def serve_home():
        return FileResponse(STATIC_DIR / "index.html")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_vue(full_path: str):
        # Don't intercept API or Swagger routes
        api_prefixes = (
            "auth",
            "chat",
            "reports",
            "upload",
            "docs",
            "redoc",
            "openapi.json"
        )

        if full_path.startswith(api_prefixes):
            return {"detail": "Not Found"}

        return FileResponse(STATIC_DIR / "index.html")
else:
    @app.get("/")
    def home():
        return {
            "project": APP_NAME,
            "version": APP_VERSION,
            "status": "Running"
        }