# Student Management System

## Implementation Tasks

Follow these steps to implement the system:

1. **Understand and Test Student APIs** (Already implemented)
   - Examine the working student endpoints in `app.py`
   - Study the Student class implementation in `models/person.py`
   - Test the /students endpoints using the example requests below or the implemented api calls in "university_test.py"

2. **Implement Teacher APIs**
   - Implement Teacher class methods in `models/person.py`:
     * get_role
     * validate_specializations
     * assign_course
     * remove_course
     * to_dict
   - Implement teacher endpoints in `app.py`:
     * handle_teachers (GET, POST)
   - Test using similar patterns as student APIs

3. **Implement Course APIs**
   - Implement Course class methods in `models/course.py`:
     * validate
     * take_attendance
     * assign_grade
     * to_dict
   - Implement course endpoints in `app.py`:
     * handle_courses (GET, POST)
   - Test course creation and listing

4. **Implement System Logic**
   - Implement remaining University class methods in `models/university.py`:
     * add_teacher, add_course
     * enroll_student, withdraw_student
     * assign_teacher
     * get_course_roster, get_teacher_courses, get_student_courses
     * record_attendance, assign_grade
     * get_course_grades, get_student_grades
   - Implement remaining endpoints in `app.py`:
     * Course enrollment (POST, DELETE)
     * Teacher assignment (POST)
     * Attendance recording (POST)
     * Grade assignment (POST)

A RESTful API for managing students, teachers, courses, and related academic operations using Flask.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```
or by using the "Run" button in Pycharm.

## API Endpoints

### Students

- `GET /students` - List all students
- `POST /students` - Create a new student
  ```json
  {
    "name": "John Doe",
    "contact_info": {
      "email": "john@example.com",
      "phone": "123-456-7890"
    }
  }
  ```
- `GET /students/<student_id>` - Get student details

### Teachers

- `GET /teachers` - List all teachers
- `POST /teachers` - Create a new teacher
  ```json
  {
    "name": "Jane Smith",
    "contact_info": {
      "email": "jane@example.com",
      "phone": "123-456-7890"
    },
    "specializations": ["math", "physics"]
  }
  ```

### Courses

- `GET /courses` - List all courses
- `POST /courses` - Create a new course
  
  For math courses:
  ```json
  {
    "type": "math",
    "name": "Advanced Calculus",
    "max_capacity": 30,
    "difficulty_level": "advanced"
  }
  ```
  
  For art courses:
  ```json
  {
    "type": "art",
    "name": "Introduction to Painting",
    "max_capacity": 20,
    "materials_required": ["canvas", "paint brushes", "acrylic paint"]
  }
  ```

### Enrollment

- `POST /courses/<course_id>/students/<student_id>` - Enroll student in course
- `DELETE /courses/<course_id>/students/<student_id>` - Withdraw student from course

### Course Assignment

- `POST /courses/<course_id>/teacher/<teacher_id>` - Assign teacher to course

### Attendance

- `POST /courses/<course_id>/attendance` - Record attendance
  ```json
  {
    "date": "2025-04-08",
    "present_students": ["student_id1", "student_id2"]
  }
  ```

### Grades

- `POST /courses/<course_id>/grades/<student_id>` - Assign grade
  ```json
  {
    "grade": 95.5
  }
  ```

## Data Models

### Person (Base Class)
- id: UUID string
- name: string
- contact_info: dictionary with email and phone

### Student
- Inherits from Person
- enrolled_courses: set of course IDs
- attendance: dictionary mapping course IDs to dates present

### Teacher
- Inherits from Person
- specializations: list of strings
- assigned_courses: set of course IDs

### Course
- id: UUID string
- name: string
- course_type: string ('math' or 'art')
- max_capacity: integer
- difficulty_level: string (required for math courses: 'beginner'/'intermediate'/'advanced')
- materials_required: set of strings (required for art courses)
- students: set of student IDs
- teacher_id: string (nullable)
- attendance: dictionary mapping dates to present student IDs
- grades: dictionary mapping student IDs to grades

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request (invalid input)
- 404: Not Found

Error responses include a JSON object with an "error" message:
```json
{
  "error": "Description of what went wrong"
}