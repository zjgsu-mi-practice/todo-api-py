from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import todo, category, tag, reminder, memo
from app.database import init_db
import app.models  # Import all models to ensure they're registered

app = FastAPI(
    title="Todo App API",
    description="A complete API for managing todos with reminders, categories, tags, and memos.",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todo.router)
app.include_router(category.router)
app.include_router(tag.router)
app.include_router(reminder.router)
app.include_router(memo.router)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Todo API is running"}