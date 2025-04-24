from abc import ABC, abstractmethod
from operator import truediv
from typing import Dict, Any, Set, List
import uuid

class Person(ABC):
    def __init__(self, name: str, contact_info: Dict[str, str]):
        self.id = str(uuid.uuid4())
        self.name = name
        self.contact_info = contact_info
        self.validate()

    @abstractmethod
    def get_role(self) -> str:
        """Return the role of the person (student/teacher)"""
        pass

    def validate(self):
        """Validate person data"""
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(self.contact_info, dict):
            raise ValueError("Contact info must be a dictionary")
        required_fields = ['email', 'phone']
        for field in required_fields:
            if field not in self.contact_info:
                raise ValueError(f"Contact info must include {field}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert person data to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'contact_info': self.contact_info,
            'role': self.get_role()
        }

class Student(Person):
    def __init__(self, name: str, contact_info: Dict[str, str]):
        super().__init__(name, contact_info)
        self.enrolled_courses: Set[str] = set()  # Set of course IDs
        self.attendance: Dict[str, Set[str]] = {}  # Course ID to set of dates present

    def get_role(self) -> str:
        return "student"

    def enroll_in_course(self, course_id: str):
        """Enroll student in a course"""
        self.enrolled_courses.add(course_id)

    def withdraw_from_course(self, course_id: str):
        """Withdraw student from a course"""
        try:
            self.enrolled_courses.remove(course_id)
        except KeyError:
            raise KeyError("Course not found for this student. Please try again")

    def to_dict(self) -> Dict[str, Any]:
        """Convert student data to dictionary"""
        base_dict = super().to_dict()
        base_dict.update({
            'enrolled_courses': list(self.enrolled_courses)
        })
        return base_dict

class Teacher(Person):
    def __init__(self, name: str, contact_info: Dict[str, str], specializations: List[str]):
        super().__init__(name, contact_info)
        self.specializations = specializations
        self.assigned_courses: Set[str] = set()  # Set of course IDs
        self.validate_specializations()

    def get_role(self) -> str:
        """Return the role of the teacher"""
        # TODO: Implement get_role method
        # Return "teacher" as the role
        return "teacher"

    def validate_specializations(self):
        """Validate teacher specializations"""
        # TODO: Implement validate_specializations method
        # 1. Check if specializations is a list
        # 2. Verify all specializations are strings
        # 3. Ensure teacher has at least one specialization

        # Checking all conditions at once
        if (isinstance(self.specializations,list) and
            all(isinstance(i, str) for i in self.specializations) and
            len(self.specializations) > 0):
            return True

        return False

    def assign_course(self, course_id: str):
        """Assign a course to the teacher"""
        # TODO: Implement assign_course method
        # Add the course_id to the teacher's assigned_courses set

        #use add method for sets
        return self.assigned_courses.add(course_id)

    def remove_course(self, course_id: str):
        """Remove a course assignment from the teacher"""
        # TODO: Implement remove_course method
        # Remove the course_id from the teacher's assigned_courses set
        try:
            self.assigned_courses.remove(course_id)
        except KeyError:
            raise KeyError("Course not found for this teacher. Please try again")

    def to_dict(self) -> Dict[str, Any]:
        """Convert teacher data to dictionary"""
        # TODO: Implement to_dict method
        # 1. Get the base dictionary from parent class
        # 2. Add specializations and assigned_courses to the dictionary
        # 3. Return the complete dictionary

        #get the base dictionary as a blueprint
        teacher_dict = super().to_dict()

        #add variables to contact info
        teacher_dict.update(
            {"specializations": self.specializations,
            "assigned_courses": list(self.assigned_courses)
             }
        )
        return teacher_dict

