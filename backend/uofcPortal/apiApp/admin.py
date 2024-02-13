from django.contrib import admin
from .models import Faculty, Department, Program, Student

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Student)

# admin.site.register(User)
# admin.site.register(Course)