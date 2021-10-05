import json

import pytest

from app import app
from fastapi.testclient import TestClient


client = TestClient(app.app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_ping():
    response = client.get("/ping")
    assert response.status_code == 200

def test_read_ping_ping():
    response = client.get("/ping/ping")
    assert response.status_code == 200

def test_read_ping_ping():
    response = client.get("/ping/poing")
    assert response.status_code == 404
