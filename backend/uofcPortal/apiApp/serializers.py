from rest_framework import serializers
from .models import Faculty, Department, Program, Student

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'faculty_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_id', 'deparment_name', 'faculty_id']

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['program_id', 'program_year', 'program_load', 'program_stream', 'program_major', 'program_minor', 'program_honors', 'faculty_id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'student_email', 'student_first_name', 'student_last_name','student_date_of_birth', 'student_phone_number', 'student_address', 'student_citizenship', 'student_residency', 'program_id']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'email', 'role', 'department']

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['course_id', 'name']