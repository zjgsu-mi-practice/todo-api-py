# Todo API in Python

A FastAPI-based Todo application with full CRUD functionality, built with Python 3.11 and SQLite.

[![Tests](https://github.com/zjgsu-mi-practice/todo-api-py/actions/workflows/tests.yml/badge.svg)](https://github.com/zjgsu-mi-practice/todo-api-py/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/zjgsu-mi-practice/todo-api-py/branch/main/graph/badge.svg)](https://codecov.io/gh/zjgsu-mi-practice/todo-api-py)

## Features

- RESTful API endpoints for Todo management
- Async database operations with SQLAlchemy
- JWT authentication (to be implemented)
- Automatic API documentation (Swagger & ReDoc)
- Database migrations with Alembic
- Dependency management with Rye
- Comprehensive test coverage

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy (async)
- SQLite (with option for PostgreSQL)
- Alembic for migrations
- Pydantic for data validation
- pytest for testing
- pytest-asyncio for async tests
- pytest-cov for coverage reporting

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

### Categories
- `GET /categories` - List all categories
- `POST /categories` - Create a new category

### Tags
- `GET /tags` - List all tags
- `POST /tags` - Create a new tag

### Reminders
- `GET /todos/{todoId}/reminders` - Get reminders for a todo
- `POST /todos/{todoId}/reminders` - Create a reminder

### Memos
- `GET /memos/{memoId}` - Get a memo
- `PUT /memos/{memoId}` - Update a memo

## Testing

The project includes comprehensive tests for all endpoints. To run the tests:

```bash
# Install test dependencies
rye add --dev pytest pytest-asyncio pytest-cov httpx

# Run tests with coverage
rye run pytest --cov=app tests/ --cov-report=term-missing
```

The test suite includes:
- Unit tests for all endpoints
- Integration tests for database operations
- Test fixtures for database and FastAPI client
- Coverage reporting

Tests are automatically run via GitHub Actions on every push to the repository. See the [GitHub Actions workflow](.github/workflows/tests.yml) for details.

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

## Continuous Integration

This project uses GitHub Actions for continuous integration:

- Automated tests run on every push and pull request
- Tests run on multiple operating systems (Ubuntu, macOS, Windows)
- Tests run on multiple Python versions (3.8, 3.9, 3.10, 3.11)
- Code coverage is reported to Codecov

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
│   ├── conftest.py       # Test configuration
│   ├── test_todos.py     # Todo endpoint tests
│   ├── test_categories.py # Category endpoint tests
│   ├── test_tags.py      # Tag endpoint tests
│   ├── test_reminders.py # Reminder endpoint tests
│   └── test_memos.py     # Memo endpoint tests
└── requirements.lock      # Locked dependencies
