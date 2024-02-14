from rest_framework import serializers
from .models import Faculty, Department, Program, Student, Course, Instructor, Lecture, Grade

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'faculty_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_id', 'deparment_name', 'faculty_id'] #not sure if foreign keys should be included in any/all of these

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['program_id', 'program_year', 'program_load', 'program_stream', 'program_major', 'program_minor', 'program_honors', 'faculty_id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'student_email', 'student_first_name', 'student_last_name','student_date_of_birth', 'student_phone_number', 'student_address', 'student_citizenship', 'student_residency', 'program_id']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_title', 'course_number', 'course_description', 'course_prerequisite', 'course_antirequisite', 'course_units', 'course_notes', 'course_is_repeatable', 'course_type', 'department_id']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['instructor_id', 'instructor_first_name', 'instructor_last_name', 'department_id']

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['lecture_id', 'lecture_term', 'course_id', 'instructor_id']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade_gpa', 'student_id', 'lecture_id']