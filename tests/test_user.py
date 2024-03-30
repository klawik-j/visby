from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)
user_data = {"name": "John Doe", "user_id": 1}


def test_create_user():
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [user_data]


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == user_data


def test_update_user():
    updated_user_data = {"name": "Jane Doe", "user_id": 1}
    response = client.put("/users/1", json=updated_user_data)
    assert response.status_code == 200
    assert response.json() == updated_user_data


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Jane Doe", "user_id": 1}
