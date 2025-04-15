def test_create_category(client):
    response = client.post(
        "/categories",
        json={
            "name": "Test Category",
            "color": "#FF5733"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Category"
    assert data["color"] == "#FF5733"
    assert "id" in data

def test_list_categories(client):
    # Create multiple categories
    for i in range(3):
        client.post(
            "/categories",
            json={"name": f"Test Category {i}"}
        )

    response = client.get("/categories")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert all("name" in item for item in data)
    assert all("id" in item for item in data) 