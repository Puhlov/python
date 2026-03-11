import requests
from conftest import HEADERS
from conftest import BASE_URL


def create_project(project_data):
    return requests.post(f"{BASE_URL}/projects", json=project_data, headers=HEADERS)


def update_project(project_id, project_data):
    return requests.put(f"{BASE_URL}/projects/{project_id}", json=project_data, headers=HEADERS)


def get_project(project_id):
    return requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)


def test_create_project_positive(project_payload):
    response = create_project(project_payload)
    assert response.status_code == 201

def test_create_project_negative():
    response = create_project({"description": "Missing title"})  # нет поля title
    assert response.status_code == 400

def test_update_project_positive(project_id):
    updated_payload = {"title": "Updated Project Title"}
    update_response = update_project(project_id, updated_payload)
    assert update_response.status_code == 200
    get_response = get_project(project_id)
    assert get_response.status_code == 200
    actual_title = get_response.json().get("title") or get_response.json().get("name")
    assert actual_title == updated_payload["title"]



def test_update_project_negative(nonexistent_id):
    response = update_project(nonexistent_id, {"title": "Ghost"})  # "name" → "title"
    assert response.status_code == 404


def test_get_project_positive(project_id):
    response = get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative(nonexistent_id):
    response = get_project(nonexistent_id)
    assert response.status_code == 404