from flask import Flask, jsonify, request
from models import University, Student, Teacher, Course

app = Flask(__name__)
university = University()

# Error handler for ValueError
@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({"error": str(error)}), 400

# Student endpoints
@app.route('/students', methods=['GET', 'POST'])
def handle_students():
    if request.method == 'POST':
        data = request.get_json()
        try:
            student = Student(
                name=data['name'],
                contact_info=data['contact_info']
            )
            student_id = university.add_student(student)
            return jsonify({"id": student_id}), 201
        except (KeyError, ValueError) as e:
            return jsonify({"error": str(e)}), 400
    
    # GET method
    return jsonify({
        "students": [student.to_dict() for student in university.students.values()]
    })

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Get a specific student's details"""
    # TODO: Implement get_student endpoint
    # 1. Check if student exists
    # 2. Return student data or 404 error
    student = university.students.get(student_id)
    if not student:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student.to_dict())

# Teacher endpoints
@app.route('/teachers', methods=['GET', 'POST'])
def handle_teachers():
    """Handle teacher creation and listing"""
    # TODO: Implement handle_teachers endpoint
    # For POST:
    # 1. Get JSON data
    # 2. Create Teacher instance with name, contact_info, and specializations
    # 3. Add teacher to university
    # 4. Return teacher ID
    # For GET:
    # 1. Return list of all teachers

    #POST method
    if request.method == 'POST':
        data = request.get_json()
        try:
            teacher = Teacher(
                name=data['name'],
                contact_info=data['contact_info'],
                specializations = data['specializations']
            )
            teacher_id = university.add_teacher(teacher)
            return jsonify({"id": teacher_id}), 201
        except (KeyError, ValueError) as e:
            return jsonify({"error": str(e)}), 400

    # GET method
    return jsonify({
        "teachers": [teacher.to_dict() for teacher in university.teachers.values()]
    })


# Course endpoints
@app.route('/courses', methods=['GET', 'POST'])
def handle_courses():
    """Handle course creation and listing"""
    # TODO: Implement handle_courses endpoint
    # For POST:
    # 1. Get JSON data
    # 2. Extract course type and create appropriate course arguments
    # 3. Create Course instance
    # 4. Add course to university
    # 5. Return course ID
    # For GET:
    # 1. Return list of all courses
    #POST method
    if request.method == 'POST':
        data = request.get_json()
        try:
            course_type = data["type"]
            if course_type == "math":
                course = Course(
                    # id and enrollment are generated internally, not in POST method
                    name = data["name"],
                    course_type= course_type,
                    max_capacity= data["max_capacity"],
                    difficulty_level= data["difficulty_level"]
                )
            elif course_type == "art":
                course = Course(
                    name=data["name"],
                    course_type=course_type,
                    max_capacity=data["max_capacity"],
                    materials_required=data["materials_required"]
                )

            course_id = university.add_course(course)
            return jsonify({"id": course.id}), 201
        except (KeyError, ValueError, TypeError) as e:
            return jsonify({"error": str(e)}), 400

    # GET method
    return jsonify({
        "courses": [course.to_dict() for course in university.courses.values()]
    })

# Enrollment endpoints
@app.route('/courses/<course_id>/students/<student_id>', methods=['POST', 'DELETE'])
def handle_enrollment(course_id, student_id):
    """Handle student enrollment and withdrawal"""
    # TODO: Implement handle_enrollment endpoint
    # For POST:
    # 1. Try to enroll student in course
    # 2. Return success/failure message
    # For DELETE:
    # 1. Try to withdraw student from course
    # 2. Return success/failure message
    # POST method
    if request.method == 'POST':
        try:
            university.enroll_student(student_id, course_id)
            return jsonify({'message':"Enrollment successful"}), 201
        except (KeyError, ValueError, TypeError) as e:
            return jsonify({"error": str(e)}), 400
    # DELETE method
    elif request.method == 'DELETE':
        try:
            university.withdraw_student(student_id, course_id)
            return jsonify({'message': "Withdrawal successful"}), 201
        except (KeyError, ValueError, TypeError) as e:
            return jsonify({"error": str(e)}), 400

# Course assignment endpoint
@app.route('/courses/<course_id>/teacher/<teacher_id>', methods=['POST'])
def assign_teacher_to_course(course_id, teacher_id):
    """Assign a teacher to a course"""
    # TODO: Implement assign_teacher_to_course endpoint
    # 1. Try to assign teacher to course
    # 2. Return success/failure message
    if request.method =='POST':
        try:
            university.assign_teacher(teacher_id, course_id)
            return jsonify({'message': "Assignment successful"}), 201
        except (KeyError, ValueError, TypeError) as e:
            return jsonify({"error": str(e)}), 400

# Attendance endpoints
@app.route('/courses/<course_id>/attendance', methods=['POST'])
def record_attendance(course_id):
    """Record attendance for a course"""
    # TODO: Implement record_attendance endpoint
    # 1. Get JSON data with date and present students
    # 2. Try to record attendance
    # 3. Return success/failure message
    if request.method =='POST':
        data = request.get_json()
        try:
            date = data['date']
            present_student_ids = set(data['present_student_ids'])
            university.record_attendance(course_id,date,present_student_ids)
            return jsonify({'message': "Record successful"}), 201
        except (KeyError, ValueError, TypeError) as e:
            return jsonify({"error": str(e)}), 400

# Grade endpoints
@app.route('/courses/<course_id>/grades/<student_id>', methods=['POST'])
def assign_grade(course_id, student_id):
    """Assign a grade to a student"""
    # TODO: Implement assign_grade endpoint
    # 1. Get JSON data with grade
    # 2. Try to assign grade
    # 3. Return success/failure message
    if request.method =='POST':
        data = request.get_json()
        try:
            grade= float(data['grade'])
            university.assign_grade(course_id,student_id, grade)
            return jsonify({'message': "Grade assignation successful"}), 201
        except (KeyError, ValueError, TypeError) as e:
            return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)