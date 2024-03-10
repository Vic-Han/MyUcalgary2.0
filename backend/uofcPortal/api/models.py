from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
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
    program_degree_level = models.CharField(max_length=30) #bach vs masters vs phd
    program_major = models.CharField(max_length=30)
    program_minor = models.CharField(max_length=30, blank=True, null=True)
    program_honor = models.BooleanField()

    major_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="major_program")
    minor_department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True, related_name="minor_program")

    # To show Program's name in admin panel
    def __str__(self):
        return self.program_name

class Term(models.Model):
    term_key = models.CharField(max_length=7, unique=True, primary_key=True)  # Example: Fal2023
    term_name = models.CharField(max_length=20)
    term_year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.term_key
    
class EmergencyContact(models.Model):
    emergency_contact_name = models.CharField(max_length=30)
    emergency_contact_phone = models.CharField(max_length=15)
    emergency_contact_relationship = models.CharField(max_length=30)

    def __str__(self):
        return self.emergency_contact_name
    
class Address(models.Model):
    address_street_address = models.CharField(max_length=30)
    address_postal_code = models.CharField(max_length=10)
    address_city = models.CharField(max_length=30)
    address_province = models.CharField(max_length=30)
    address_country = models.CharField(max_length=30)

    def __str__(self):
        return self.address_street_address

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    citizenship_status = models.CharField(max_length=30)

    home_phone_number = models.CharField(blank=True, max_length=15)
    mobile_phone_number = models.CharField(blank=True, max_length=15)
    other_phone_number = models.CharField(blank=True, max_length=15)
    preferred_phone = models.CharField(default="home", max_length=6)

    personal_email = models.EmailField()
    school_email = models.EmailField()
    preferred_email = models.CharField(default="personal", max_length=8)

    preferred_emergency_contact = models.CharField(default="1", max_length=1)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    emergency_contact1 = models.ForeignKey(EmergencyContact, on_delete=models.CASCADE, null=True, related_name="contact1")
    emergency_contact2 = models.ForeignKey(EmergencyContact, on_delete=models.CASCADE, null=True, related_name="contact2")
    emergency_contact3 = models.ForeignKey(EmergencyContact, on_delete=models.CASCADE, null=True, related_name="contact3")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)

    # To show Student's name in admin panel
    def __str__(self):
        return f"{self.student_id} - {self.student_last_name}, {self.student_first_name}"
    

class Course(models.Model):
    course_code = models.CharField(max_length=7, unique=True, primary_key=True) # e.g. SENG401
    course_title = models.CharField(max_length=60) # e.g. Software Architecture
    course_description = models.CharField(max_length=300)
    course_prerequisites = models.CharField(max_length=50, blank=True, null=True)
    course_antirequisites = models.CharField(max_length=50, blank=True, null=True)
    course_units = models.IntegerField()
    course_notes = models.CharField(max_length=100, blank=True, null=True)
    course_repeatability = models.BooleanField(default=False)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    # To show Course's name in admin panel
    def __str__(self):
        return f"{self.course_code} - {self.course_title}"
    
class Instructor(models.Model):
    instructor_id = models.CharField(max_length=10)
    instructor_first_name = models.CharField(max_length=30)
    instructor_last_name = models.CharField(max_length=30)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    # To show Instructor's name in admin panel
    def __str__(self):
        return f"{self.instructor_id} - {self.instructor_last_name}, {self.instructor_first_name}"

class Lecture(models.Model):
    lecture_id = models.CharField(max_length=10) # e.g. L01
    lecture_days = models.CharField(max_length=10)
    lecture_starttime = models.CharField(max_length=4)
    lecture_endtime = models.CharField(max_length=4)
    lecture_roomnumber = models.CharField(max_length=10)

    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.course} - {self.lecture_id}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('student', 'lecture')  # Avoid duplicate enrollments

    def __str__(self):
        return f"{self.student} | {self.lecture}"

class Grade(models.Model):
    grade = models.FloatField(validators=[MaxValueValidator(100)])
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.enrollment.student}: {self.grade}"

