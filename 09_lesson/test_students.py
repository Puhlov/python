import pytest  
from sqlalchemy.orm import sessionmaker  
from models import Student, engine

@pytest.fixture(scope='module')
def db_session():
    """Создает сессию для тестов и удаляет данные после тестов."""
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session  # Тесты могут использовать эту сессию

    session.close()
    transaction.rollback()
    connection.close()

def test_add_student(db_session):
    new_student = Student(name='John Doe')
    db_session.add(new_student)
    db_session.commit()

    assert new_student.id is not None  # Проверяем, что ID был создан

def test_update_student(db_session):
    student = db_session.query(Student).filter_by(name='John Doe').first()
    student.name = 'Jane Doe'
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(id=student.id).first()
    assert updated_student.name == 'Jane Doe'  # Проверяем, что имя изменилось

def test_delete_student(db_session):
    student = db_session.query(Student).filter_by(name='Jane Doe').first()
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(id=student.id).first()
    assert deleted_student is None  # Проверяем, что студент был удален