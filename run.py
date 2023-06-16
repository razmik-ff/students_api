from flask import Flask, request, jsonify

app = Flask(__name__)
students_data = [
    {
        "id": 1,
        "name": "Ani",
        "age": 23,
        "grade": 3,
        "points": 87,
    },        
    {
        "id": 2,
        "name": "Hakob",
        "age": 25,
        "grade": 2,
        "points": 46,
    }
]
LAST_ID = 2

@app.route("/")
def home():
    return "Hello"

@app.route("/students", methods=["GET", "POST"])
def students():
    print(request.method)
    if request.method =="GET":
        return jsonify(students_data), 200
    else:
        new_student = request.get_json()
        fields = {"name", "age", "grade", "points"}
        new_fileds = set(new_student.keys())
        if fields != new_fileds:
            return jsonify({"message": "Fields are not correct"}), 400
        global LAST_ID
        LAST_ID += 1
        new_student["id"] = LAST_ID
        students_data.append(new_student)
        return jsonify(new_student), 201

@app.route("/student/<int:id>", methods=["GET", "PATCH", "DELETE"])
def student(id):
    for student in students_data:
        if id == student["id"]:
            return jsonify(student), 200
    return jsonify({"message": "Student not found"}), 404

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
