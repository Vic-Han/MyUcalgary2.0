from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faculty(models.Model):
    faculty_id = models.CharField(max_length=10, unique=True, primary_key=True)
    faculty_name = models.CharField(max_length=30, unique=True)

    # To show Faculty's name in admin panel
    def __str__(self):
        return self.faculty_id


class Department(models.Model):
    department_id = models.CharField(max_length=10, unique=True, primary_key=True)
    department_name = models.CharField(max_length=30)

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    # To show Department's name in admin panel
    def __str__(self):
        return self.department_id

class Program(models.Model):
    program_id = models.CharField(max_length=10, unique=True, primary_key=True)
    program_year = models.DateField()
    program_load = models.IntegerField() # Let's define what this is
    program_stream = models.CharField(max_length=30)
    program_major = models.CharField(max_length=30)
    program_minor = models.CharField(max_length=30)
    program_honor = models.BooleanField()

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    # To show Program's name in admin panel
    def __str__(self):
        return self.program_id

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    year = models.DateField()
    gpa = models.FloatField()

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # To show Student's name in admin panel
    def __str__(self):
        return self.student_id