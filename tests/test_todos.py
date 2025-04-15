import pytest
from datetime import datetime, timedelta

def test_create_todo(client):
    response = client.post(
        "/todos",
        json={
            "title": "Test Todo",
            "description": "Test Description",
            "status": "pending",
            "due_date": (datetime.now() + timedelta(days=1)).isoformat(),
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "Test Description"
    assert data["status"] == "pending"
    assert "id" in data

def test_get_todo(client):
    # First create a todo
    create_response = client.post(
        "/todos",
        json={"title": "Test Todo"}
    )
    todo_id = create_response.json()["id"]

    # Then get it
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["id"] == todo_id

def test_list_todos(client):
    # Create multiple todos
    for i in range(3):
        client.post(
            "/todos",
            json={"title": f"Test Todo {i}", "status": "pending"}
        )

    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 3
    assert data["pagination"]["total"] == 3
    assert data["pagination"]["page"] == 1
    assert data["pagination"]["limit"] == 20

def test_update_todo(client):
    # Create a todo
    create_response = client.post(
        "/todos",
        json={"title": "Original Title"}
    )
    todo_id = create_response.json()["id"]

    # Update it
    response = client.put(
        f"/todos/{todo_id}",
        json={"title": "Updated Title", "status": "completed"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["status"] == "completed"

def test_delete_todo(client):
    # Create a todo
    create_response = client.post(
        "/todos",
        json={"title": "To be deleted"}
    )
    todo_id = create_response.json()["id"]

    # Delete it
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    # Verify it's deleted
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 404

def test_todo_not_found(client):
    response = client.get("/todos/non-existent-id")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found" 