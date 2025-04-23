from typing import Dict, List, Optional, Set
from datetime import datetime
from .person import Student, Teacher
from .course import Course

class University:
    def __init__(self):
        self.students: Dict[str, Student] = {}  # ID to Student mapping
        self.teachers: Dict[str, Teacher] = {}  # ID to Teacher mapping
        self.courses: Dict[str, Course] = {}  # ID to Course mapping
    
    def add_student(self, student: Student) -> str:
        """Add a student and return their ID"""
        self.students[student.id] = student
        return student.id
    
    def add_teacher(self, teacher: Teacher) -> str:
        """Add a teacher and return their ID"""
        # TODO: Implement add_teacher method
        # 1. Add the teacher to the teachers dictionary using their ID as the key
        # 2. Return the teacher's ID
        self.teachers[teacher.id] = teacher
        return teacher.id
    
    def add_course(self, course: Course) -> str:
        """Add a course and return its ID"""
        # TODO: Implement add_course method
        # 1. Add the course to the courses dictionary using its ID as the key
        # 2. Return the course's ID
        self.courses[course.id] = course
        return course.id
    
    def enroll_student(self, student_id: str, course_id: str) -> bool:
        """Enroll a student in a course"""
        # TODO: Implement enroll_student method
        # 1. Check if student_id and course_id exist
        # 2. Check if course has available capacity
        # 3. Add student to course's student set
        # 4. Update student's enrolled courses
        # 5. Return True if successful, False otherwise

        if not student_id in self.students or not course_id in self.courses:
            return False

        course = self.courses[course_id]
        student = self.students[student_id]

        if course.max_capacity <= len(course.students):
            return False

        course.students.add(student_id)
        student.enroll_in_course(course_id)
        return True


    
    def assign_teacher(self, teacher_id: str, course_id: str) -> bool:
        """Assign a teacher to a course"""
        # TODO: Implement assign_teacher method
        # 1. Check if teacher_id and course_id exist
        # 2. If course already has a teacher, remove course from their assignments
        # 3. Set new teacher_id for course
        # 4. Add course to teacher's assigned courses
        # 5. Return True if successful, False otherwise
        if teacher_id not in self.teachers or course_id not in self.courses:
            return False

        course = self.courses[course_id]
        teacher = self.teachers[teacher_id]

        #using teacher methods for easier handling
        if course.teacher_id:
            previous_teacher = self.teachers[course.teacher_id]
            previous_teacher.remove_course(course_id)

        course.teacher_id = teacher_id

        teacher.assign_course(course_id)
        return True
    
    def withdraw_student(self, student_id: str, course_id: str) -> bool:
        """Withdraw a student from a course"""
        # TODO: Implement withdraw_student method
        # 1. Check if student_id and course_id exist
        # 2. Check if student is enrolled in the course
        # 3. Remove student from course's student set
        # 4. Update student's enrolled courses
        # 5. Return True if successful, False otherwise
        if not student_id in self.students or not course_id in self.courses:
            return False

        course = self.courses[course_id]
        student = self.students[student_id]

        if course_id not in student.enrolled_courses:
            return False

        course.students.remove(student_id)
        student.withdraw_from_course(course_id)
        return True
    
    def get_course_roster(self, course_id: str) -> Optional[List[Dict]]:
        """Get a list of students enrolled in a course"""
        # TODO: Implement get_course_roster method
        # 1. Check if course_id exists
        # 2. Get all students enrolled in the course
        # 3. Return list of student dictionaries
        if not course_id in self.courses:
            return None
        course = self.courses[course_id]
        roster = []

        for i in course.students:
            student = self.students[i]
            roster.append(student.to_dict())

        return roster
    
    def get_teacher_courses(self, teacher_id: str) -> Optional[List[Dict]]:
        """Get a list of courses assigned to a teacher"""
        # TODO: Implement get_teacher_courses method
        # 1. Check if teacher_id exists
        # 2. Get all courses assigned to the teacher
        # 3. Return list of course dictionaries
        if not teacher_id in self.teachers:
            return None
        teacher = self.teachers[teacher_id]
        courses: list = []
        for id in teacher.assigned_courses:
            if id in self.courses: # avoid KeyError
                course = self.courses[id]
                courses.append(course.to_dict())
        return courses


    def get_student_courses(self, student_id: str) -> Optional[List[Dict]]:
        """Get a list of courses a student is enrolled in"""
        # TODO: Implement get_student_courses method
        # 1. Check if student_id exists
        # 2. Get all courses the student is enrolled in
        # 3. Return list of course dictionaries
        if not student_id in self.students:
            return None

        student = self.students[student_id]
        courses: list =[]

        for course_id in student.enrolled_courses:
            if course_id in self.courses:
                course = self.courses[course_id]
                courses.append(course.to_dict())

        return courses
    
    def record_attendance(self, course_id: str, date: datetime, present_student_ids: Set[str]) -> bool:
        """Record attendance for a course on a specific date"""
        # TODO: Implement record_attendance method
        # 1. Check if course_id exists
        # 2. Try to record attendance using course's take_attendance method
        # 3. Return True if successful, False otherwise
        if not course_id in self.courses:
            return False
        course = self.courses[course_id]
        course.take_attendance(date,present_student_ids)
        return True
    
    def assign_grade(self, course_id: str, student_id: str, grade: float) -> bool:
        """Assign a grade to a student for a course"""
        # TODO: Implement assign_grade method
        # 1. Check if course_id and student_id exist
        # 2. Try to assign grade using course's assign_grade method
        # 3. Return True if successful, False otherwise
        if not course_id in self.courses or not student_id in self.students:
            return False
        course = self.courses[course_id]
        course.assign_grade(student_id, grade)
        return True
            
    def get_course_grades(self, course_id: str) -> Optional[Dict[str, float]]:
        """Get all grades for a course"""
        # TODO: Implement get_course_grades method
        # 1. Check if course_id exists
        # 2. Return copy of course's grades dictionary
        if course_id not in self.courses:
            return None
        course = self.courses[course_id]
        return course.grades.copy() #return copy to ensure safety
    
    def get_student_grades(self, student_id: str) -> Optional[Dict[str, float]]:
        """Get all grades for a student across all courses"""
        # TODO: Implement get_student_grades method
        # 1. Check if student_id exists
        # 2. Get student's grades from all enrolled courses
        # 3. Return dictionary mapping course IDs to grades
        if student_id not in self.students:
            return None
        student = self.students[student_id]
        all_grades: dict = {}
        for course_id in student.enrolled_courses:
            if course_id in self.courses: # avoid KeyError
                course = self.courses[course_id]
                all_grades[course_id] = course.grades[student_id]

        return all_grades

