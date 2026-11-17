
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


def test_get_unknown_student_returns_404(client):
    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "Student not found"
    }


def test_add_negative_score_returns_400(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    response = client.post(
        "/students/101/scores",
        json={"score": -1}
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Score cannot be negative"
    }


def test_add_score_above_100_returns_400(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    response = client.post(
        "/students/101/scores",
        json={"score": 101}
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Score cannot be greater than 100"
    }


def test_create_student_without_name_returns_400(client):
    response = client.post(
        "/students",
        json={"roll_no": 101}
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_seventh_score_returns_400(client):
    client.post(
        "/students",
        json={"name": "Ali", "roll_no": 101}
    )

    for score in [60, 65, 70, 75, 80, 85]:
        response = client.post(
            "/students/101/scores",
            json={"score": score}
        )
        assert response.status_code == 200

    response = client.post(
        "/students/101/scores",
        json={"score": 90}
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Student cannot have more than 6 scores"
    }
