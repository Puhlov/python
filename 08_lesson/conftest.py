import pytest
import uuid
import requests

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "1772370785850_e1da380936645a3641a4ec73043b56590ccd5e2fb1ac9bb46f77e79dd0f97b80"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def create_project(project_data):
    return requests.post(f"{BASE_URL}/projects", json=project_data, headers=HEADERS)


@pytest.fixture
def project_payload():
    return {"title": "Test Project"}


@pytest.fixture
def project_id(project_payload):
    response = create_project(project_payload)
    assert response.status_code == 201, f"Ошибка создания: {response.status_code} {response.text}"
    return response.json()["id"]


@pytest.fixture
def nonexistent_id():
    return str(uuid.uuid4())