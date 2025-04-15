def test_create_tag(client):
    response = client.post(
        "/tags",
        json={"name": "Test Tag"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Tag"
    assert "id" in data

def test_list_tags(client):
    # Create multiple tags
    for i in range(3):
        client.post(
            "/tags",
            json={"name": f"Test Tag {i}"}
        )

    response = client.get("/tags")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert all("name" in item for item in data)
    assert all("id" in item for item in data) 