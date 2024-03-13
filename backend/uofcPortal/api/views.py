
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import Student, Faculty, Department, Program, Course, Instructor, Lecture, Grade, Enrollment, Address, Transaction
from .serializers import StudentSerializer, UserSerializer, FacultySerializer, DepartmentSerializer, ProgramSerializer, AddressSerializer
from .serializers import CourseSerializer, InstructorSerializer, LectureSerializer, GradeSerializer, EnrollmentSerializer, PersonalInfoSerializer, TransactionSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     # Assuming the user is linked to the student via a ForeignKey
    #     return Student.objects.filter(user=self.request.user)

class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = PersonalInfoSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class StudentGradeView(APIView):
    # authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    # permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get(self, request):

        student = Student.objects.first()  # Replace with authentication late
        # enrollments = Enrollment.objects.filter(student=student).select_related('course', 'term')
        enrollments = Enrollment.objects.filter(student=student)
        
        activity = {}
        for enrollment in enrollments:
            term = enrollment.lecture.term.term_name
            grades = Grade.objects.filter(enrollment=enrollment)
            if term not in activity:
                activity[term] = {
                    "Units Enrolled": 0,
                    "Program": f"{student.program.program_name}, {student.program.program_degree_level}, {student.program.program_major}",
                    "Level": enrollment.lecture.term.term_year,
                    "Plan": f"{student.program.program_degree_level}, {student.program.program_major}",
                    "TermGPA": 0,
                    "TermLetterGrade": "",
                    "courses": []
                }

            for grade in grades:
                course_info = {
                    "name": enrollment.lecture.course.course_code,
                    "grade": grade.grade,
                    "letter": self.grade_to_letter(grade.grade),
                    "units": enrollment.lecture.course.course_units
                }
                activity[term]["courses"].append(course_info)
                activity[term]["Units Enrolled"] += 3 # Assuming each course is 3 units

        for term, info in activity.items():
            term_gpa, term_letter_grade = self.calculate_term_gpa_and_letter_grade(info['courses'])
            info['TermGPA'] = term_gpa
            info['TermLetterGrade'] = term_letter_grade

        overallGPA = self.calculate_overall_gpa(activity)
        response = {
            "overallGPA": overallGPA,
            "letterGrade": self.gpa_to_letter_grade(overallGPA),
            "activity": activity
        }
        return Response(response)


    def grade_to_letter(self, grade):
        if grade >= 97:
            return 'A+'
        elif grade >= 93:
            return 'A'
        elif grade >= 90:
            return 'A-'
        elif grade >= 87:
            return 'B+'
        elif grade >= 83:
            return 'B'
        elif grade >= 80:
            return 'B-'
        elif grade >= 77:
            return 'C+'
        elif grade >= 73:
            return 'C'
        elif grade >= 70:
            return 'C-'
        elif grade >= 67:
            return 'D+'
        elif grade >= 63:
            return 'D'
        elif grade >= 60:
            return 'D-'
        else:
            return 'F'
        
    # Convert numeric grade to GPA points.
    def grade_to_gpa(self, grade):
        if grade >= 97:
            return 4.0  # A+
        elif grade >= 93:
            return 4.0  # A
        elif grade >= 90:
            return 3.7  # A-
        elif grade >= 87:
            return 3.3  # B+
        elif grade >= 83:
            return 3.0  # B
        elif grade >= 80:
            return 2.7  # B-
        elif grade >= 77:
            return 2.3  # C+
        elif grade >= 73:
            return 2.0  # C
        elif grade >= 70:
            return 1.7  # C-
        elif grade >= 67:
            return 1.3  # D+
        elif grade >= 63:
            return 1.0  # D
        elif grade >= 60:
            return 0.7  # D-
        else:
            return 0.0  # F

    def gpa_to_letter_grade(self, gpa):
        if gpa >= 4.0:
            return 'A+'
        elif gpa >= 3.7:
            return 'A'
        elif gpa >= 3.3:
            return 'A-'
        elif gpa >= 3.0:
            return 'B+'
        elif gpa >= 2.7:
            return 'B'
        elif gpa >= 2.3:
            return 'B-'
        elif gpa >= 2.0:
            return 'C+'
        elif gpa >= 1.7:
            return 'C'
        elif gpa >= 1.3:
            return 'C-'
        elif gpa >= 1.0:
            return 'D+'
        elif gpa >= 0.7:
            return 'D'
        elif gpa >= 0.0:
            return 'F'
        else:
            return 'F'

        
    def calculate_term_gpa_and_letter_grade(self, courses):
        if not courses:
            return 0, 'N/A'  # If no courses taken in a semester, return 0 GPA and N/A as letter grade
        

        total_gpa = sum(self.grade_to_gpa(course['grade']) for course in courses)
        term_gpa = total_gpa / len(courses)
        letter_grade = self.gpa_to_letter_grade(term_gpa)
        return term_gpa, letter_grade


    def calculate_overall_gpa(self, activity):
        total_units = 0
        total_weighted_gpa = 0
        
        for term, info in activity.items():
            # Calculate term GPA if not already done
            if 'TermGPA' not in info or 'Units Enrolled' not in info:
                term_gpa, term_letter_grade = self.calculate_term_gpa_and_letter_grade(info['courses'])
                info['TermGPA'] = term_gpa
                units_enrolled = sum(course.get('units', 3) for course in info['courses'])
                info['Units Enrolled'] = units_enrolled
            else:
                units_enrolled = info['Units Enrolled']
                term_gpa = info['TermGPA']
            
            total_units += units_enrolled
            total_weighted_gpa += term_gpa * units_enrolled

        if total_units == 0:
            return 0  # Avoid division by zero
        overall_gpa = round(total_weighted_gpa / total_units, 2)
        return overall_gpa
    


class StudentFinancesView(APIView):
    # authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    # permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get(self, request):
       
        # student = get_object_or_404(Student, user=request.user)

        student = Student.objects.first()  # Replace with authentication later
        if not student:
            return Response({"error": "No student found"}, status=404)


        # Fetch all transactions for the student, ordered by term
        transactions = Transaction.objects.filter(student=student).order_by('term__term_year', 'term__term_name')
        
        activity = {}
        for transaction in transactions:
            term_name = transaction.term.term_name + " " + str(transaction.term.term_year)
            if term_name not in activity:
                activity[term_name] = []
            
            # Initialize Credit and Debit categories if they don't exist
            if not any("Credit" in entry for entry in activity[term_name]):
                activity[term_name].append({"Credit": []})
            if not any("Debit" in entry for entry in activity[term_name]):
                activity[term_name].append({"Debit": []})

            transaction_entry = {
                "name": transaction.transaction_name,
                "date": transaction.transaction_posted_date,
                "amount": transaction.transaction_amount,
                "type": transaction.transaction_type,
            }

            # Determine if the transaction is a Credit or Debit and add it to the correct category
                # If amount > 0, it's a Credit
                # If amount < 0, it's a Debit
            if transaction.transaction_amount > 0:
                activity[term_name][0]["Credit"].append(transaction_entry)
            else:
                activity[term_name][1]["Debit"].append(transaction_entry)


        # Calculate financial summary
        total_paid = sum(transaction.transaction_amount for transaction in transactions if transaction.transaction_amount > 0)
        total_awards = sum(transaction.transaction_amount for transaction in transactions if transaction.transaction_type == "award")
        total_due = sum(transaction.transaction_amount for transaction in transactions if transaction.transaction_amount < 0)
        due_by_date = "Jan 1, 2024 (HARDCODED)"  # Ask Vic about this? what's the overall due date mean?

        # Prepare response data
        response_data = {
            "paid": total_paid,
            "awards": total_awards,
            "due": total_due*-1, # Convert negative due amount to positive
            "dueBy": due_by_date,
            "activity": activity
        }

        return Response(response_data)