# Todo API Project Plan

This document outlines the plan for creating the Python Todo API project.

**1. Information Gathering & Confirmation:**

*   Reviewed `instructions/openapi.yaml` for API endpoints and schemas.
*   Reviewed `instructions/README.md` for functionality and suggested technology stack.
*   **Confirmed:** Use **FastAPI** as the primary web framework.

**2. Project Initialization & Structure:**

*   Use `rye init` to initialize the project.
*   Establish the following project structure:
    ```
    .
    ├── .gitignore
    ├── instructions/
    │   ├── openapi.yaml
    │   └── README.md
    ├── PLAN.md         <-- This file
    ├── pyproject.toml  <-- Rye configuration and dependencies
    ├── README.md       <-- Project-specific README
    ├── src/
    │   └── todo_api_py/  <-- Main application package
    │       ├── __init__.py
    │       ├── main.py       <-- FastAPI app instance and core setup
    │       ├── core/         <-- Config, DB connection (later)
    │       │   └── __init__.py
    │       ├── models/       <-- Pydantic models (matching OpenAPI schemas)
    │       │   └── __init__.py
    │       │   └── todo.py
    │       │   └── category.py
    │       │   └── tag.py
    │       │   └── reminder.py
    │       │   └── memo.py
    │       ├── routers/      <-- API endpoint definitions
    │       │   └── __init__.py
    │       │   └── todos.py
    │       │   └── categories.py
    │       │   └── tags.py
    │       │   └── reminders.py
    │       │   └── memos.py
    │       └── dependencies/ <-- Reusable dependencies (e.g., auth - later)
    │           └── __init__.py
    └── tests/          <-- Unit/Integration tests (later)
        └── __init__.py
    ```

**3. Initial Dependency Installation:**

*   Use `rye add` to install:
    *   `fastapi`
    *   `uvicorn[standard]`
    *   `pydantic`

**4. Basic Application Setup:**

*   Create initial FastAPI app instance in `src/todo_api_py/main.py`.
*   Define basic Pydantic models in `src/todo_api_py/models/`.
*   Create placeholder API routers in `src/todo_api_py/routers/`.

**5. Next Steps (Post-Initial Setup):**

*   Database integration (SQLAlchemy, asyncpg, Alembic).
*   Implementing endpoint logic.
*   Adding JWT authentication.
*   Setting up testing (`pytest`).
*   Containerization (Docker).

**6. Proposed Structure Diagram:**

```{mermaid}
graph TD
    A[todo-api-py] --> B(pyproject.toml);
    A --> C(README.md);
    A --> D(src/);
    A --> E(tests/);
    A --> F(instructions/);
    A --> P(PLAN.md);
    F --> F1(openapi.yaml);
    F --> F2(README.md);

    D --> G(todo_api_py/);
    G --> H(__init__.py);
    G --> I(main.py);
    G --> J(core/);
    G --> K(models/);
    G --> L(routers/);
    G --> M(dependencies/);

    K --> K1(todo.py);
    K --> K2(category.py);
    K --> K3(tag.py);
    K --> K4(reminder.py);
    K --> K5(memo.py);

    L --> L1(todos.py);
    L --> L2(categories.py);
    L --> L3(tags.py);
    L --> L4(reminders.py);
    L --> L5(memos.py);
```