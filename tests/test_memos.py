import json
import pytest
from app.models.memo import Memo

def test_get_memo(client):
    # First create a memo via a POST request
    create_response = client.post(
        "/memos",
        json={
            "content": "Test Memo Content",
            "attachments": ["https://example.com/file.pdf"]
        }
    )
    assert create_response.status_code == 201
    memo_id = create_response.json()["id"]

    # Then get it
    response = client.get(f"/memos/{memo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Test Memo Content"
    assert data["attachments"] == ["https://example.com/file.pdf"]
    assert data["id"] == memo_id

def test_update_memo(client):
    # Create a memo
    create_response = client.post(
        "/memos",
        json={"content": "Original Content"}
    )
    assert create_response.status_code == 201
    memo_id = create_response.json()["id"]

    # Update it
    response = client.put(
        f"/memos/{memo_id}",
        json={
            "content": "Updated Content",
            "attachments": ["https://example.com/new.pdf"]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Updated Content"
    assert data["attachments"] == ["https://example.com/new.pdf"]

def test_memo_not_found(client):
    response = client.get("/memos/non-existent-id")
    assert response.status_code == 404
    assert response.json()["detail"] == "Memo not found" 