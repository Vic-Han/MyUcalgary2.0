
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
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer

    def get_queryset(self):
        # Filter the addresses to only those belonging to the currently authenticated user
        return Address.objects.filter(student__user=self.request.user)

class EmergencyContactViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)


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


class PersonalInfoView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        # student = get_object_or_404(Student, user=request.user)
        student = Student.objects.first()
        personal_info = {
            "firstname": student.student_first_name,
            "lastname": student.student_last_name,
            "UCID": student.student_id,
            "date of birth": student.date_of_birth.strftime('%Y-%m-%d') if student.date_of_birth else None
        }

        citizenship = {
            "country": student.address.address_country if student.address else None,
            "status": student.citizenship_status
        }

        address = {
            "id": student.address.pk if student.address else None,
            "street address": student.address.address_street_address if student.address else None,
            "postal code": student.address.address_postal_code if student.address else None,
            "city": student.address.address_city if student.address else None,
            "province/state": student.address.address_province if student.address else None
        }

        phone_numbers = {
            "home": student.home_phone_number,
            "mobile": student.mobile_phone_number,
            "other": student.other_phone_number,
            "preferred": student.preferred_phone
        }

        email = {
            "personal": student.personal_email,
            "school": student.school_email,
            "preferred": student.preferred_email
        }

        emergency_contact = {
            "id1": student.emergency_contact1.pk if student.emergency_contact1 else None,
            "name1": student.emergency_contact1.emergency_contact_name if student.emergency_contact1 else None,
            "phone1": student.emergency_contact1.emergency_contact_phone if student.emergency_contact1 else None,
            "relation1": student.emergency_contact1.emergency_contact_relationship if student.emergency_contact1 else None,
            "id2": student.emergency_contact2.pk if student.emergency_contact2 else None,
            "name2": student.emergency_contact2.emergency_contact_name if student.emergency_contact2 else None,
            "phone2": student.emergency_contact2.emergency_contact_phone if student.emergency_contact2 else None,
            "relation2": student.emergency_contact2.emergency_contact_relationship if student.emergency_contact2 else None,
            "id3": student.emergency_contact3.pk if student.emergency_contact3 else None,
            "name3": student.emergency_contact3.emergency_contact_name if student.emergency_contact3 else None,
            "phone3": student.emergency_contact3.emergency_contact_phone if student.emergency_contact3 else None,
            "relation3": student.emergency_contact3.emergency_contact_relationship if student.emergency_contact3 else None,
            "preferred": student.preferred_emergency_contact
        }

        response_data = {
            "personal_info": personal_info,
            "citizenship": citizenship,
            "address": address,
            "phone_numbers": phone_numbers,
            "email": email,
            "emergency_contact": emergency_contact
        }

        return Response(response_data)
    

class StudentApplicationsViewSet(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        student = Student.objects.first()  # Replace with authentication later
        if not student:
            return Response({"error": "No student found"}, status=404)
        applications = StudentApplications.objects.filter(student=student)

        undergrad_applications = [
            {
                "primary key": application.pk,
                "faculty": application.major_program.department.faculty.faculty_name,
                "program": application.major_program.program_name,
                "major": application.major_program.program_name,
                "minor": application.minor_program.program_name if application.minor_program else "None",
                "concentration": application.concentration, 
                "status": application.application_status
            }
            for application in applications.filter(major_program__program_degree_level="Bachelor")
        ]       

        graduate_applications = [
            {
                "primary key": application.pk,
                "faculty": application.major_program.department.faculty.faculty_name,
                "program": application.major_program.program_name,
                "major": application.major_program.program_name,
                "type": "Research (What is Type??)",
                "Advisor": "Ronnie the software architecture goat", 
                "status": application.application_status
            }
            for application in applications.filter(major_program__program_degree_level__in=["Master", "PhD"])
        ]

        # Mockup for scholarships
        scholarships = [
            {
                "not implemented": "yet",
            }
        ]

        # Construct the final response
        response_data = {
            "Undergrad applications": undergrad_applications,
            "Graduate applications": graduate_applications,
            "Scholarships": scholarships,
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
                    "Program": applications.major_program.program_name,
                    "Level": student_year,
                    "Plan": f"{applications.major_program.program_degree_level}, {applications.major_program.program_name}",
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

        #student = Student.objects.first()  # Replace with authentication later
        #if not student:
        #    return Response({"error": "No student found"}, status=404)

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
                    "credits": 0,
                    "debits": 0,
                    "net_balance": 0,
                    "due": transaction.term.due_date  # To be adjust as needed
                }

            # Assuming negative amount is due and positive is paid/credit
            current_amount = transaction.transaction_amount
            if current_amount < 0:
                dashboard_data["finances"][term_name]["debits"] += current_amount
            else:
                dashboard_data["finances"][term_name]["credits"] += current_amount
            dashboard_data["finances"][term_name]["net_balance"] += current_amount

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


