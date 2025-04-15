from datetime import datetime, timedelta

def test_create_reminder(client):
    # First create a todo
    todo_response = client.post(
        "/todos",
        json={"title": "Test Todo"}
    )
    todo_id = todo_response.json()["id"]

    # Then create a reminder for it
    response = client.post(
        f"/todos/{todo_id}/reminders",
        json={
            "time": (datetime.now() + timedelta(days=1)).isoformat(),
            "notify_method": "email"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["todo_id"] == todo_id
    assert data["notify_method"] == "email"
    assert "id" in data

def test_list_reminders(client):
    # Create a todo
    todo_response = client.post(
        "/todos",
        json={"title": "Test Todo"}
    )
    todo_id = todo_response.json()["id"]

    # Create multiple reminders
    for i in range(3):
        client.post(
            f"/todos/{todo_id}/reminders",
            json={
                "time": (datetime.now() + timedelta(days=i+1)).isoformat(),
                "notify_method": "push"
            }
        )

    response = client.get(f"/todos/{todo_id}/reminders")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert all(item["todo_id"] == todo_id for item in data)
    assert all("time" in item for item in data)
    assert all("notify_method" in item for item in data) 