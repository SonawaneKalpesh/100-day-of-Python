from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Rahul",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Amit",
        "marks": 90
    }
]


# GET - View all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# GET - View one student
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


# POST - Add a student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "marks": data["marks"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


# DELETE - Delete a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({
                "message": "Student deleted successfully"
            })

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)