from django.contrib import admin
from .models import Student, Requirement, Faculty, Department, Tutorial, Program, Term, Course, Transaction, Instructor, Lecture, Grade, Enrollment, Address, EmergencyContact, StudentApplications


admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Term)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Lecture)
admin.site.register(Tutorial)
admin.site.register(Grade)
admin.site.register(Enrollment)
admin.site.register(Address)
admin.site.register(EmergencyContact)
admin.site.register(Transaction)
admin.site.register(StudentApplications)
admin.site.register(Requirement)