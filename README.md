# Todo API in Python

A FastAPI-based Todo application with full CRUD functionality, built with Python 3.11 and SQLite.

## Features

- RESTful API endpoints for Todo management
- Async database operations with SQLAlchemy
- JWT authentication (to be implemented)
- Automatic API documentation (Swagger & ReDoc)
- Database migrations with Alembic
- Dependency management with Rye

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy (async)
- SQLite (with option for PostgreSQL)
- Alembic for migrations
- Pydantic for data validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/zjgsu-mi-practice/todo-api-py.git
cd todo-api-py
```

2. Install dependencies using Rye:
```bash
rye sync
```

3. Set up database:
```bash
rye run alembic upgrade head
```

## Running the Application

Start the development server:
```bash
rye run uvicorn main:app --reload
```

The API will be available at:
- http://localhost:8000

## API Documentation

Interactive documentation is automatically available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

### Todos
- `GET /todos` - List all todos
- `POST /todos` - Create a new todo
- `GET /todos/{id}` - Get a specific todo
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo

## Configuration

Environment variables can be set in `.env` file:
```
DATABASE_URL=sqlite+aiosqlite:///./sql_app.db
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Development

### Running Tests
```bash
rye run pytest
```

### Creating Migrations
```bash
rye run alembic revision --autogenerate -m "migration_message"
rye run alembic upgrade head
```

## Project Structure
```
├── alembic/              # Migration scripts
├── app/                  # Application code
│   ├── config.py         # Configuration settings
│   ├── database.py       # Database connection
│   ├── models/           # Database models
│   ├── routers/          # API routers
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # Main application
├── tests/                # Test cases
└── requirements.lock      # Locked dependencies
