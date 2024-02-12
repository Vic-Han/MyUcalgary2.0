from rest_framework import serializers
from .models import Faculty, Department, Program

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
        fields = ['program_id', 'program_year', 'program_load', 'program_stream', 'program_major', 'program_minor', 'program_honors']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'email', 'role', 'department']

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['course_id', 'name']