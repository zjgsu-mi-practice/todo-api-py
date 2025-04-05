from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import todo
from app.database import init_db
import app.models  # Import all models to ensure they're registered

app = FastAPI(
    title="Todo App API",
    description="A complete API for managing todos with reminders, categories, tags, and memos.",
    version="1.0.0",
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

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Todo API is running"}