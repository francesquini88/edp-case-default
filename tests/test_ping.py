from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_ping_returns_pong() -> None:
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


def test_ping_returns_bad_request() -> None:
    response = client.get("/ping?fail=400")

    assert response.status_code == 400
    assert response.json() == {"error": "requisição inválida simulada"}


def test_ping_returns_internal_server_error() -> None:
    response = client.get("/ping?fail=500")

    assert response.status_code == 500
    assert response.json() == {"error": "erro interno do servidor"}
