from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    program = models.CharField(max_length=30)
    year = models.IntegerField()
    gpa = models.FloatField()

    # To show Student's name in admin panel
    def __str__(self):
        return self.student_id