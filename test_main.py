from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users_initially_empty():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_user():
    new_user = {
        "Username": "testuser",
        "Email": "test@example.com",
        "Password": "secure123",
    }
    response = client.post("/users", json=new_user)
    assert response.status_code == 200
    assert response.json()["message"] == "SUCCESS : User added"
