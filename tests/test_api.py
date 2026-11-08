from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_features():
    r = client.post("/features", json={"url": "https://github.com"})
    assert r.status_code == 200
    assert r.json()["uses_https"] is True


def test_empty_url_rejected():
    r = client.post("/features", json={"url": ""})
    assert r.status_code == 422


def test_too_long_url_rejected():
    r = client.post("/features", json={"url": "a" * 3000})
    assert r.status_code == 422

def test_short_but_valid_url_accepted():
    r = client.post("/features", json={"url": "abc"})
    assert r.status_code == 200
    assert r.json()["url_length"] == 3
