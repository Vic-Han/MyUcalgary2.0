from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

# this signal will automatically create a token for each new user
@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

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
    program_name = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    program_degree_level = models.CharField(max_length=30) #bach vs masters vs phd
    program_honor = models.BooleanField()

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

    # program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

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
    lecture_starttime = models.FloatField(validators=[MaxValueValidator(23.00)])
    lecture_endtime = models.FloatField(validators=[MaxValueValidator(23.83)])
    
    # Float values for lecture start and endtimes are as follow:
    # 12:00am =  0.00
    # 01:05am =  1.08
    # 09:10am =  9.17
    # 10:15am = 10.25
    # 11:20am = 11.33
    # 12:25pm = 12.42
    # 01:30pm = 13.50
    # 07:35pm = 19.58
    # 08:40pm = 20.67
    # 09:45pm = 21.75
    # 10:50pm = 22.83
    # 11:55pm = 23.92

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
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.enrollment.student}: {self.grade}"

class Transaction(models.Model):
    transaction_name = models.CharField(max_length=50) # e.g. Bank of Montreal
    transaction_posted_date = models.DateField()
    transaction_type = models.CharField(max_length=10) # e.g. credit, debit, award
    transaction_amount = models.FloatField()

    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.transaction_type} - {self.transaction_name}: ${self.transaction_amount}"
    
class StudentApplications(models.Model):
    application_status = models.CharField(max_length=30)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    major_program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="major_program")
    minor_program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True, related_name="minor_program")

    concentration = models.BooleanField()
    honors_program = models.BooleanField()

    def __str__(self):
        return f"{self.id} - StudentID:{self.student.student_id} ({self.student.student_first_name} {self.student.student_last_name})"
