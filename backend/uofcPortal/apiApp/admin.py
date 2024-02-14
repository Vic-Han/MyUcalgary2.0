from django.contrib import admin
from .models import Faculty, Department, Program, Student, Course, Instructor, Lecture, Grade

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Lecture)
admin.site.register(Grade)