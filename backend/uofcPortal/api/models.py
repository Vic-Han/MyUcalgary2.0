from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=30, unique=True, primary_key=True)

    # To show Faculty's name in admin panel
    def __str__(self):
        return self.faculty_name


class Department(models.Model):
    department_name = models.CharField(max_length=30, unique=True, primary_key=True)

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    # To show Department's name in admin panel
    def __str__(self):
        return self.department_name

class Program(models.Model):
    program_name = models.CharField(max_length=10, unique=True, primary_key=True)
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
        return self.program_name

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    email = models.EmailField()
    year = models.DateField()
    gpa = models.FloatField()

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # To show Student's name in admin panel
    def __str__(self):
        return self.student_id
    

class Course(models.Model):
    course_name = models.CharField(max_length=4, unique=True, primary_key=True)
    course_title = models.CharField(max_length=60)
    course_number = models.IntegerField()
    course_description = models.CharField(max_length=300)
    course_prerequisites = models.CharField(max_length=50)
    course_antirequisites = models.CharField(max_length=50)
    course_units = models.IntegerField()
    course_notes = models.CharField(max_length=100)
    course_repeatability = models.BooleanField(default=False)
    course_type = models.CharField(max_length=20)

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    # To show Course's name in admin panel
    def __str__(self):
        return self.course_name
    
class Instructor(models.Model):
    instructor_id = models.CharField(max_length=10)
    instructor_first_name = models.CharField(max_length=30)
    instructor_last_name = models.CharField(max_length=30)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    # To show Instructor's name in admin panel
    def __str__(self):
        return self.instructor_id

class Lecture(models.Model):
    lecture_id = models.CharField(max_length=10)
    lecture_term = models.CharField(max_length=10)
    lecture_starttime = models.CharField(max_length=4)
    lecture_endtime = models.CharField(max_length=4)
    lecture_roomnumber = models.CharField(max_length=10)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)
    grade = models.FloatField()