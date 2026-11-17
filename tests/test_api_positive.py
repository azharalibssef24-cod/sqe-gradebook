
import pytest

from src.api.app import create_app
from src.gradebook.gradebook import Student


@pytest.fixture
def client():
    Student.student_ids.clear()

    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client

    Student.student_ids.clear()


def test_create_student(client):
    response = client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    assert response.status_code == 201
    assert response.get_json() == {
        "name": "Ali",
        "roll_no": 101,
        "average": 0.0
    }


def test_get_student(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    response = client.get("/students/101")

    assert response.status_code == 200
    assert response.get_json() == {
        "name": "Ali",
        "roll_no": 101,
        "average": 0.0
    }


def test_add_student_score(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    response = client.post(
        "/students/101/scores",
        json={"score": 80}
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Score added successfully",
        "roll_no": 101,
        "score": 80
    }


def test_get_student_average(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    client.post("/students/101/scores", json={"score": 80})
    client.post("/students/101/scores", json={"score": 90})

    response = client.get("/students/101/average")

    assert response.status_code == 200
    assert response.get_json() == {
        "roll_no": 101,
        "average": 85.0
    }


def test_get_all_students(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    client.post(
        "/students",
        json={"name": "Ahmed", "roll_no": 102}
    )

    response = client.get("/students")

    assert response.status_code == 200
    assert response.get_json() == [
        {
            "name": "Ali",
            "roll_no": 101,
            "average": 0.0
        },
        {
            "name": "Ahmed",
            "roll_no": 102,
            "average": 0.0
        }
    ]
