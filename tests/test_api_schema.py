
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


def test_students_list_json_schema(client):
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

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 2

    for student in data:
        assert set(student.keys()) == {
            "name",
            "roll_no",
            "average"
        }

        assert isinstance(student["name"], str)
        assert isinstance(student["roll_no"], int)
        assert isinstance(student["average"], (int, float))
