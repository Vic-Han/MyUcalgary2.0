from django.db import models

class Faculty(models.Model):
    faculty_id = models.IntegerField(unique=True, primary_key=True)
    faculty_name = models.CharField(max_length=100, unique=True) #could also make a CharChoice for this

class Department(models.Model):
    department_id = models.IntegerField(unique=True, primary_key=True)
    department_name = models.CharField(max_length=100, unique=True) #could also make a CharChoice for this
    faculty_id = models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)
#not sure if we want "null" and CASCADE for foreign keys just doing it for now

class Program(models.Model):
    class ProgramYearChoices(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4

    PROGRAM_LOAD_CHOICES = {
        "FT": "Full Time",
        "PT": "Part Time"
    }

    PROGRAM_STREAM_CHOICES = {
        "BA": "Bachelor of Arts",
        "BSC": "Bachelor of Science",
        "BFA": "Bachelor of Fine Arts",
        "BCOM": "Bachelor of Commerce",
        "BED": "Bachelor of Education",
        "MA": "Master of Arts",
        "MSC": "Master of Science",
        "MFA": "Master of Fine Arts",
        "MBA": "Master of Business Administration",
        "MED": "Master of Education",
    }

    program_id = models.IntegerField(unique=True, primary_key=True)
    program_year = models.IntegerField(choices=ProgramYearChoices, default=1)
    program_load = models.CharField(max_length=2, choices=PROGRAM_LOAD_CHOICES, DEFAULT = "FT")
    program_stream = models.CharField(max_length=4, choices=PROGRAM_STREAM_CHOICES, DEFAULT = "BA")
    program_major = models.CharField(max_length=100, default="na") #could also make a CharChoice for this
    program_minor = models.CharField(max_length=100, default="na") #could also make a CharChoice for this
    program_honors = models.BooleanField(default=False) #not sure what this is/if boolean works here
    faculty_id = models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.IntegerField(unique=True, primary_key=True)
    student_email = models.CharField(max_length=100, default="example@mail.com")
    student_first_name = models.CharField(max_length=100, default="Jane")
    student_last_name = models.CharField(max_length=100, default="Doe")
    student_date_of_birth = models.CharField(max_length=10, default="2000/01/01")
    student_phone_number = models.CharField(max_length=11, default="11234567890")
    student_address = models.CharField(max_length=100, default="1 1st Street NW Calgary, Alberta A1B 2C3")
    student_citizenship = models.CharField(max_length=100, default = "Canadian")
    student_residency = models.BooleanField(default=False)
    program_id = models.ForeignKey(Program, null=True, on_delete=models.CASCADE)
 #just realized we're going to have an individual Program entry for every slight variation of a program, might be a better way
    
class Course(models.Model):
    course_id = models.IntegerField(unique=True, primary_key=True)
    course_name = models.CharField(max_length=4, default="AAAA")
    course_title = models.CharField(max_length=100, default="Basket Weaving for Dummies")
    course_number = models.IntegerField(default=101)
    course_description = models.IntegerField(max_length=300, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque libero semper congue imperdiet. Pellentesque at risus metus. Mauris scelerisque, elit et ullamcorper lacinia, enim purus molestie mauris, sodales imperdiet tellus nunc ac tortor. Sed eget metus augue. Praesent ultricies, eros sit amet iaculis interdum, tortor nisl tempus mauris, id commodo elit sem nec dui. Quisque varius urna et nisi viverra, in efficitur metus ullamcorper. Vivamus a risus purus. Aliquam tincidunt ornare sapien. Nullam aliquet purus nec tortor viverra iaculis. Sed quis interdum nisl, quis venenatis diam. Nulla facilisi. Duis vitae enim sit amet augue euismod tempor quis quis elit.")
    course_prerequisite = models.IntegerChoices() #how to add multiple
    course_antirequisite = models.IntegerChoices() #how to add multiple
    course_units = models.IntegerField(default=3)
    course_notes = models.CharField(max_length=300, default="N/A")
    course_is_repeatable = models.BooleanField(default=False)
    course_type = models.IntegerField(default=1) #what is this?
    department_id = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

class Instructor(models.Model):
    instructor_id = models.IntegerField(unique=True, primary_key=True)
    instructor_first_name = models.CharField(max_length=50, default="Jerry")
    instructor_last_name = models.CharField(max_length=50, default="Seinfeld")
    department_id = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

class Lecture(models.Model):
    LECTURE_TERM_CHOICES = {
        "FAL": "Fall",
        "SPR": "Spring", 
        "SUM": "Summer",
        "WIN": "Winter"
    }

    lecture_id = models.IntegerField(unique=True, primary_key=True)
    lecture_term = models.CharField(max_length=3, choices=LECTURE_TERM_CHOICES, default="FAL")
    course_id = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, null=True, on_delete=models.CASCADE)

class Grade(models.Model):
    GRADE_GPA_CHOICES = {
        "0.0": "F",
        "1.0": "D", 
        "1.3": "D+",
        "1.7": "C-", 
        "2.0": "C",
        "2.3": "C+", 
        "2.7": "B-",
        "3.0": "B",
        "3.3": "B+", 
        "3.7": "A-",
        "4.0": "A",
    }
    
    grade_gpa = models.CharField(max_length=3, choices=GRADE_GPA_CHOICES, default="4.0")
    student_id = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Lecture, null=True, on_delete=models.CASCADE)

# what is this? do we need it?
#     def __str__(self):
#         return self.email