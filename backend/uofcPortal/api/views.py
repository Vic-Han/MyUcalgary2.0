
import math
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .mixins import GradeMixins 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import Student, Requirement, Faculty, Department, Program, Course, Instructor, Lecture, Grade, Enrollment, Address, Transaction, StudentApplications
from .serializers import StudentSerializer, RequirementSerializer, UserSerializer, FacultySerializer, DepartmentSerializer, ProgramSerializer, AddressSerializer
from .serializers import CourseSerializer, InstructorSerializer, LectureSerializer, GradeSerializer, EnrollmentSerializer, PersonalInfoSerializer, TransactionSerializer, StudentApplicationsSerializer


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

# To be modifed
class StudentApplicationsViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # def post(self, request):
    #     student = get_object_or_404(Student, user=request.user)
    #     if not student:
    #         return Response({"error": "No student found"}, status=404)

    #     data = request.data
    #     data["student"] = student.pk
    #     serializer = StudentApplicationsSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)


    def delete(self, request):
        student = get_object_or_404(Student, user=request.user)
        if not student:
            return Response({"error": "No student found"}, status=404)

        data = request.data
        application = get_object_or_404(StudentApplications, pk=data["application_id"])
        application.delete()
        return Response({"message": "Application deleted successfully"}, status=200)

    def get(self, request):
        student = get_object_or_404(Student, user=request.user)
        if not student:
            return Response({"error": "No student found"}, status=404)
        applications = StudentApplications.objects.filter(student=student)

        undergrad_applications = [
            {
                "key": application.pk,
                "faculty": application.program.department.faculty.faculty_name,
                "program": application.program.program_name,
                "major": application.major,
                "status": application.application_status,
                "minor": application.minor,
                "concentration": application.concentration if application.concentration else "none",    
            }
            for application in applications.filter(app_type="undergrad")
        ]       

        graduate_applications = [
            {
                "key": application.pk,
                "faculty": application.program.department.faculty.faculty_name,
                "program": application.program.program_name,
                "major": application.major,
                "Advisor": application.advisor, 
                "status": application.application_status
            }
            for application in applications.filter(app_type="grad")
        ]

        # Mockup for scholarships
        scholarships = [
            {
                "key" : application.pk,
                "name": application.scholarship_name,
                "amount": application.payment_amount,
              
                "status": application.application_status
            }
            for application in applications.filter(app_type="scholarship")
        ]
        awards = [
            {
                "key" : application.pk,
                "name": application.scholarship_name,
                "amount": application.payment_amount,
                "status": application.application_status
            }
            for application in applications.filter(app_type="award")
        ]
        # Construct the final response
        response_data = {
            "Undergrad applications": undergrad_applications,
            "Graduate applications": graduate_applications,
            "Scholarships": scholarships,
            "Awards" : awards
        }

        return Response(response_data)

class StudentGradeView(APIView, GradeMixins):
    authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get(self, request):

        # student = Student.objects.first()  # Replace with authentication late
        student = get_object_or_404(Student, user=request.user)
        enrollments = Enrollment.objects.filter(student=student)
        applications = StudentApplications.objects.filter(student=student).first()


        # Calculate the student's year
        total_courses = len(enrollments)
        student_year = min(4, math.ceil(total_courses / 10)) # Assuming 10 courses per year, calculate the student's year
        
        activity = {}
        for enrollment in enrollments:
            term = enrollment.lecture.term.term_name
            grades = Grade.objects.filter(enrollment=enrollment)
            termYear = f"{term} {enrollment.lecture.term.term_year}"
            if termYear not in activity:
                activity[termYear] = {
                    "UnitsEnrolled": 0,
                    "Program": applications.program.program_name,
                    "Level": student_year,
                    "Plan": f"{applications.program.program_degree_level}, {applications.program.program_name}",
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
                activity[termYear]["courses"].append(course_info)
                activity[termYear]["UnitsEnrolled"] += 3 # Assuming each course is 3 units

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
    

class StudentFinancesView(APIView):
    authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get(self, request):
        student = get_object_or_404(Student, user=request.user)

        # student = Student.objects.first()  # Replace with authentication later
        # if not student:
        #     return Response({"error": "No student found"}, status=404)

        transactions = Transaction.objects.filter(student=student).order_by('term__term_year', 'term__term_name')
        
        activity = {}
        for transaction in transactions:
            term_name = f"{transaction.term.term_name} {transaction.term.term_year}"
            if term_name not in activity:
                activity[term_name] = []
            
            transaction_entry = {
                "name": transaction.transaction_name,
                "date": transaction.transaction_posted_date.strftime('%Y-%m-%d'),
                "amount": abs(transaction.transaction_amount),
                "type": "credit" if transaction.transaction_amount > 0 else "debit",
            }
            
            activity[term_name].append(transaction_entry)

        total_paid = sum(transaction.transaction_amount for transaction in transactions if transaction.transaction_amount > 0)
        total_awards = sum(transaction.transaction_amount for transaction in transactions if transaction.transaction_type == "award")
        total_due = sum(transaction.transaction_amount for transaction in transactions if transaction.transaction_amount < 0)

        response_data = {
            "paid": total_paid,
            "awards": total_awards,
            "due": total_due * -1,  # Convert negative due amount to positive
            "selectedTerm": f"{transaction.term.term_name} {transaction.term.term_year}",
            "activity": activity
        }

        return Response(response_data)

    

class DashboardView(APIView, GradeMixins):

    def get(self, request):
        student = Student.objects.first()
        if not student:
            return Response({"error": "No student found"}, status=404)
        
        # Dashboard data structure
        dashboard_data = {
            "grades": {},
            "finances": {}
        }

        # Grades
        enrollments = Enrollment.objects.filter(student=student)
        for enrollment in enrollments:
            term_name = f"{enrollment.lecture.term.term_name} {enrollment.lecture.term.term_year}"
            grades = Grade.objects.filter(enrollment=enrollment)

            if term_name not in dashboard_data["grades"]:
                dashboard_data["grades"][term_name] = {
                    "TermGPA": 0,
                    "TermLetterGrade": "",
                    "courses": []
                }

            for grade in grades:
                course_info = {
                    "name": enrollment.lecture.course.course_code,
                    "letter": self.grade_to_letter(grade.grade),
                    "grade": grade.grade,
                }
                dashboard_data["grades"][term_name]["courses"].append(course_info)

            # Calculate TermGPA and TermLetterGrade
            term_gpa, term_letter_grade = self.calculate_term_gpa_and_letter_grade(dashboard_data["grades"][term_name]["courses"])
            dashboard_data["grades"][term_name]["TermGPA"] = term_gpa
            dashboard_data["grades"][term_name]["TermLetterGrade"] = term_letter_grade

        # Finances
        transactions = Transaction.objects.filter(student=student).order_by('term__term_year', 'term__term_name')
        for transaction in transactions:
            term_name = f"{transaction.term.term_name} {transaction.term.term_year}"
            if term_name not in dashboard_data["finances"]:
                dashboard_data["finances"][term_name] = {
                    "balance": 0,
                    "due": "To Be Determined"  # To be adjust as needed
                }

            # Assuming negative amount is due and positive is paid/credit
            dashboard_data["finances"][term_name]["balance"] += transaction.transaction_amount

        return Response(dashboard_data)
    
class StudentRequirementsView(APIView):
    def get(self, request):
        student = Student.objects.first()
        if not student:
            return Response({"error": "No student found"}, status=404)
        
        requirement_data = {
            "programInfo": {
                "degree":{},
                "major":{},
                "minor":{},
                "concentration": "none",
                "year": "3",
                "academicLoad": "full-time"
            },
            "requirements": []
        }


        applications = StudentApplications.objects.filter(student_id=student)
        application = applications[0]
        maj_prog = application.major_program
        min_prog = application.minor_program

        requirement_data["programInfo"]["degree"] = maj_prog.program_degree_level
        requirement_data["programInfo"]["major"] = maj_prog.program_name
        requirement_data["programInfo"]["minor"] = min_prog.program_name            
            
        enrollments = Enrollment.objects.filter(student_id=student)
        lecture_list = []
        grade_list = []
        for enrollment in enrollments:
            lectures = Lecture.objects.filter(lecture_id=enrollment.lecture_id)
            for lecture in lectures:
                lecture_list.append(lecture)
            grades = Grade.objects.filter(enrollment_id=enrollment)
            for grade in grades:
                grade_list.append(grade)

        major_requirements = Requirement.objects.filter(program_id=maj_prog)
        for requirement in major_requirements:                
            courses = Course.objects.filter(course_code__in=requirement.courses.all())
            course_data = []
            units_completed = 0
            for course in courses:
                status = "incomplete"
                for grade in grade_list:
                    if grade.enrollment.lecture.course == course and grade.grade >= 50:
                        status = "complete"
                        units_completed += course.course_units
                course_data.append({
                    "name": course.course_code,
                    "units": course.course_units,
                    "status": status
                })
            req_status = ""
            if units_completed == requirement.required_units:
                req_status = "complete"
            elif 0 < units_completed and units_completed < requirement.required_units:
                req_status = "in-progress"
            else:
                req_status = "incomplete"
            requirement_data["requirements"].append({
                "description": requirement.description,
                "requiredUnits": requirement.required_units,
                "status": req_status,
                "courses": course_data
            })


        return Response(requirement_data)


