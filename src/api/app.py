
from flask import Flask, jsonify, request

from src.gradebook.gradebook import Student, Roster, validate_name


def create_app():
    app = Flask(__name__)

    roster = Roster()

    def find_student(student_id):
        for student in roster.students:
            if str(student.student_id) == str(student_id):
                return student
        return None

    def student_data(student):
        return {
            "name": student.name,
            "roll_no": student.student_id,
            "average": student.average()
        }

    @app.route("/students", methods=["POST"])
    def create_student():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Request body must be valid JSON"}), 400

        if "name" not in data or "roll_no" not in data:
            return jsonify({
                "error": "Both name and roll_no are required"
            }), 400

        name = data["name"]
        roll_no = data["roll_no"]

        if isinstance(roll_no, bool) or not isinstance(roll_no, (int, str)):
            return jsonify({"error": "roll_no must be an integer or string"}), 400

        if isinstance(roll_no, str):
            if not roll_no.isdigit():
                return jsonify({"error": "roll_no must be a positive integer"}), 400
            roll_no = int(roll_no)

        if roll_no <= 0:
            return jsonify({"error": "roll_no must be a positive integer"}), 400

        try:
            validate_name(name)

            student = Student(name, roll_no)
            roster.students.append(student)

            return jsonify(student_data(student)), 201

        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @app.route("/students/<int:student_id>", methods=["GET"])
    def get_student(student_id):
        student = find_student(student_id)

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        return jsonify(student_data(student)), 200

    @app.route("/students/<int:student_id>/scores", methods=["POST"])
    def add_score(student_id):
        student = find_student(student_id)

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        data = request.get_json(silent=True)

        if not isinstance(data, dict) or "score" not in data:
            return jsonify({"error": "Score is required"}), 400

        if isinstance(data["score"], bool):
            return jsonify({"error": "Score must be numeric"}), 400

        if len(student.scores) >= 6:
            return jsonify({
                "error": "Student cannot have more than 6 scores"
            }), 400

        try:
            student.add_score(data["score"])
            return jsonify({
                "message": "Score added successfully",
                "roll_no": student.student_id,
                "score": data["score"]
            }), 200

        except (TypeError, ValueError) as error:
            return jsonify({"error": str(error)}), 400

    @app.route("/students/<int:student_id>/average", methods=["GET"])
    def get_average(student_id):
        student = find_student(student_id)

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({
            "roll_no": student.student_id,
            "average": student.average()
        }), 200

    @app.route("/students", methods=["GET"])
    def get_students():
        students = [
            student_data(student)
            for student in roster.students
        ]

        return jsonify(students), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
