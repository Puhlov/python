import requests
import pytest

# Настройки
BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "надо заменить"  # Замените на свой токен доступа

# Заголовки для авторизации
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def create_project(project_data):
    """Создает проект с переданными данными."""
    response = requests.post(f"{BASE_URL}/projects", json=project_data, headers=HEADERS)
    return response

def update_project(project_id, project_data):
    """Обновляет проект с указанным ID."""
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=project_data, headers=HEADERS)
    return response

def get_project(project_id):
    """Получает проект по указанному ID."""
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    return response

@pytest.fixture
def project_payload():
    """Фикстура для создания тестового проекта."""
    return {
        "name": "Test Project",
        "description": "This is a test project",
        "status": "active",  # Убедитесь, что статус соответствует документации
    }

@pytest.fixture
def project_id(project_payload):
    """Создает проект и возвращает его ID для тестирования обновления и получения."""
    response = create_project(project_payload)
    assert response.status_code == 201  # Убедитесь, что проект создан
    return response.json()["id"]

def test_create_project_positive(project_payload):
    """Тест на создание проекта (позитивный сценарий)."""
    response = create_project(project_payload)
    assert response.status_code == 201
    assert response.json()["name"] == project_payload["name"]

def test_create_project_negative():
    """Тест на создание проекта (негативный сценарий) без обязательного поля."""
    invalid_payload = {
        "description": "Missing name"
    }
    response = create_project(invalid_payload)
    assert response.status_code == 400  # Ожидаем ошибку 400 за отсутствие обязательного поля

def test_update_project_positive(project_id):
    """Тест на обновление проекта (позитивный сценарий)."""
    updated_payload = {
        "name": "Updated Project Name",
        "description": "Updated description"
    }
    response = update_project(project_id, updated_payload)
    assert response.status_code == 200
    assert response.json()["name"] == updated_payload["name"]

def test_update_project_negative():
    """Тест на обновление проекта (негативный сценарий) с неверным ID."""
    invalid_project_id = "invalid_id"
    updated_payload = {
        "name": "New Project Name"
    }
    response = update_project(invalid_project_id, updated_payload)
    assert response.status_code == 404  # Ожидаем ошибку 404 за несуществующий проект

def test_get_project_positive(project_id):
    """Тест на получение проекта (позитивный сценарий)."""
    response = get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_get_project_negative():
    """Тест на получение проекта (негативный сценарий) с неверным ID."""
    invalid_project_id = "invalid_id"
    response = get_project(invalid_project_id)
    assert response.status_code == 404  # Ожидаем ошибку 404 за несуществующий проект