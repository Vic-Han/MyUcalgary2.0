from django.db import models

class Faculty(models.Model):
    faculty_id = models.IntegerField(unique=True, primary_key=True)
    faculty_name = models.CharField(max_length=100, unique=True)

class Department(models.Model):
    department_id = models.IntegerField(unique=True, primary_key=True)
    department_name = models.CharField(max_length=100, unique=True)
    faculty_id = models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)

class Program(models.Model):
    class ProgramYear(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4

    PROGRAM_YEAR_CHOICES = {
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
    program_year = models.IntegerField(choices=ProgramYear, default=1)
    program_load = models.CharField(max_length=2, choices=PROGRAM_YEAR_CHOICES, DEFAULT = "FT")
    program_stream = models.CharField(max_length=4, choices=PROGRAM_STREAM_CHOICES, DEFAULT = "BA")
    program_major = models.CharField(max_length=100, default="na")
    program_minor = models.CharField(max_length=100, default="na")
    program_honors = models.BooleanField(default=False)
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
    


# class User(models.Model):
#     email = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email

# class Course(models.Model):
#     course_id = models.IntegerField(unique=True, primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     units = models.IntegerField()
#     prerequisites = models.ManyToManyField('self')
#     antirequisites = models.ManyToManyField('self')