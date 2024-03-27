
import math
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import viewsets, status
from .mixins import GradeMixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

import json

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

class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # queryset = Enrollment.objects.all()
    def get_queryset(self):
        token = self.request.auth  
        student = get_object_or_404(Student, user=token.user)
        return Enrollment.objects.filter(student=student)
    
    def delete(self, request, *args, **kwargs):
        try:
            student = get_object_or_404(Student, user=request.user)
        except Http404:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        term_data = request.data.get('term')
        course_data = request.data.get('course')

        if not term_data or not course_data:
            return Response({"error": "Term and course data are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            term = get_object_or_404(Term, term_key=term_data)
        except Http404:
            return Response({"error": "Term not found with the provided term data!!!"}, status=status.HTTP_404_NOT_FOUND)

        try:
            course = get_object_or_404(Course, course_code=course_data)
        except Http404:
            return Response({"error": "Course not found with the provided course data."}, status=status.HTTP_404_NOT_FOUND)

        try:
            enrollment = get_object_or_404(Enrollment, student=student, lecture__term=term, lecture__course=course)
        except Http404:
            return Response({"error": "Enrollment record not found."}, status=status.HTTP_404_NOT_FOUND)

        enrollment.delete()
        return Response({"message": "Unenrolled successfully."}, status=status.HTTP_204_NO_CONTENT)



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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        student = Student.objects.first()
        student = get_object_or_404(Student, user=request.user)
        if not student:
            return Response({"error": "No student found"}, status=404)

        data = request.data
        
        new_data = {}
        new_data['student'] = student.pk
        new_data['application_status'] = 'Under Review'
        new_data['app_type'] = data['type']
        if data['type'] == 'undergrad':
            new_data['program'] = Program.objects.get(program_name=data['program']).pk
            new_data['minor'] = data['minor']
            new_data['concentration'] = data['concentration']

        if data['type'] == 'grad':
            new_data['program'] = Program.objects.get(program_name=data['program']).pk

        if data['type'] == 'scholarship':
            new_data['scholarship_name'] = data['scholarship']
            new_data['scholarship_amount'] = 1000
        if data['type'] == 'award':
            new_data['scholarship_name'] = data['award']
            new_data['scholarship_amount'] = 1000


        serializer = StudentApplicationsSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
            
        return Response(serializer.errors, status=400)

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
                "major": application.program.program_name,
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
                "amount": application.scholarship_amount,
              
                "status": application.application_status
            }
            for application in applications.filter(app_type="scholarship")
        ]
        awards = [
            {
                "key" : application.pk,
                "name": application.scholarship_name,
                "amount": application.scholarship_amount,
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

    def delete(self, request, pk, format=None):
        # First, try to get the student object from the request.user
        try:
            student = request.user.student
        except Student.DoesNotExist:
            # If the student is not found, return a 404 error with a message
            return Response({'error': 'Student not found.'}, status=404)

        # Try to get the student application using the provided PK and ensure it belongs to the logged-in student
        try:
            application = StudentApplications.objects.get(pk=pk, student=student)
        except StudentApplications.DoesNotExist:
            # If the application is not found, return a 404 error with a message
            return Response({'error': f'Application with ID {pk} not found for this student.'}, status=404)

        # If the application is found, delete it
        application.delete()
        return Response({'message': 'Application deleted successfully.'}, status=204)
    
    # def delete(self, request):
    #     student = get_object_or_404(Student, user=request.user)

    #     # Extract the application ID from the request body
    #     application_id = request.data.get('application_id')
    #     if not application_id:
    #         return Response({"error": "Application ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         application = StudentApplications.objects.get(pk=application_id, student=student)
    #     except StudentApplications.DoesNotExist:
    #         return Response({"error": f"Application with ID {application_id} not found for this student"}, status=status.HTTP_404_NOT_FOUND)

    #     application.delete()
    #     return Response({"message": "Application deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class StudentGradeView(APIView, GradeMixins):
    authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get(self, request):

        #student = Student.objects.first()  # Replace with authentication late
        student = get_object_or_404(Student, user=request.user)
        enrollments = Enrollment.objects.filter(student=student)
        applications = StudentApplications.objects.filter(student=student).first()


        # Calculate the student's year
        total_courses = 0

        for enrollment in enrollments:
            total_courses += enrollment.lecture.course.course_units

        student_year = min(4, math.ceil(total_courses / 10)) # Assuming 10 courses per year, calculate the student's year

        currentStudentInfo = {
            "program": applications.program.program_name,
            "level": student_year,
            "plan": f"{applications.program.program_degree_level}, {applications.program.program_name}"
        }

        activity = {}
        for enrollment in enrollments:
            term = enrollment.lecture.term
            term_name = enrollment.lecture.term.term_name
            grades = Grade.objects.filter(enrollment=enrollment)
            if not grades:
                continue
            
            total_units_term = 0
            for enrollment in enrollments:
                if enrollment.lecture.term.start_date <= term.start_date:
                    total_courses += enrollment.lecture.course.course_units
            
            student_year_term = min(4, math.ceil(total_courses / 10))

            termYear = f"{term_name} {enrollment.lecture.term.term_year}"

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
                activity[termYear]["UnitsEnrolled"] += enrollment.lecture.course.course_units # Assuming each course is 3 units

        for term, info in activity.items():
            term_gpa, term_letter_grade = self.calculate_term_gpa_and_letter_grade(info['courses'])
            info['TermGPA'] = term_gpa
            info['TermLetterGrade'] = term_letter_grade

        overallGPA = self.calculate_overall_gpa(activity)
        response = {
            "overallGPA": overallGPA,
            "letterGrade": self.gpa_to_letter_grade(overallGPA),
            "activity": activity,
            "currentStudentInfo": currentStudentInfo,
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
    authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get_queryset(self):
        term = self.request.query_params.get('term')

    def get(self, request):
        student = get_object_or_404(Student, user=request.user)
        if not student:
            return Response({"error": "No student found"}, status=404)
        
        # Dashboard data structure
        dashboard_data = {
            "grades": {},
            "finances": {},
            "schedule": []
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


        # hardcoded term
        term = None
        try:
            term = Term.objects.get(term_key="Win2024")
        except Term.DoesNotExist:
            return Response({"error": "Term not found"}, status=404)
        # current schedule retrieval
        enrollments = Enrollment.objects.filter(student=student)
        for enrollment in enrollments:
            if enrollment.lecture.term == term:
                term_name = f"{enrollment.lecture.term.term_name} {enrollment.lecture.term.term_year}"
                enrollment_data = {
                    
                }
                lecture = Lecture.objects.get(lecture_id=enrollment.lecture.lecture_id , term=term)
                tutorial = Tutorial.objects.get(tutorial_id=enrollment.tutorial.tutorial_id,  term=term)
                lectureInfo = {
                    "LectureNO": lecture.lecture_id,
                    "days": lecture.lecture_days,
                    "start": lecture.lecture_starttime,
                    "end": lecture.lecture_endtime,
                    "roomno": lecture.lecture_roomnumber,

                }
                enrollment_data["Lecture"] = lectureInfo
                enrollment_data["courseCode"] = enrollment.lecture.course.course_code
                enrollment_data["courseTitle"] = enrollment.lecture.course.course_title

                if enrollment.tutorial:
                    tutorialInfo = {
                        "TutorialNO": tutorial.tutorial_id,
                        "days": tutorial.tutorial_days,
                        "start": tutorial.tutorial_starttime,
                        "end": tutorial.tutorial_endtime,
                        "roomno": tutorial.tutorial_roomnumber,
                    }
                    enrollment_data["Tutorial"] = tutorialInfo


                dashboard_data["schedule"].append(enrollment_data)
        return Response(dashboard_data)
    
class StudentRequirementsView(APIView):
    authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication

    def get(self, request):
        student = get_object_or_404(Student, user=request.user)
        student=Student.objects.first()
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
        maj_prog = application.program

        requirement_data["programInfo"]["degree"] = maj_prog.program_degree_level
        requirement_data["programInfo"]["major"] = maj_prog.program_name
        requirement_data["programInfo"]["minor"] = application.minor            
        
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
                best_grade = None
                status = "incomplete"
                for grade in grade_list:
                    if grade.enrollment.lecture.course == course and grade.grade >= 50:
                        status = "complete"
                        units_completed += course.course_units
                        if best_grade == None:
                            best_grade = grade.grade
                        elif grade.grade > best_grade:
                            best_grade = grade.grade
                course_data.append({
                    "name": course.course_code,
                    "units": course.course_units,
                    "grade": best_grade,
                    "status": status,
                    "semester": "F1"
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
                "remainingUnits": requirement.required_units - units_completed,
                "status": req_status,
                "optional": requirement.optional,
                "courses": course_data
            })


        return Response(requirement_data)


class ScheduleBuilderView(APIView):    
    authentication_classes = (TokenAuthentication,)  # uncomment this when doing authentication
    permission_classes = (IsAuthenticated,)  # uncomment this when doing authentication  

    def get_queryset(self):
        term = self.request.query_params.get('term')

    def post(self, request):
        student = get_object_or_404(Student, user=request.user)
        if not student:
            return Response({"error": "No student found"}, status=404)

        data = request.data
        term_name = data['term']
        term = Term.objects.get(term_key=term_name)
        courses = json.loads(data['courses'])
        results = []
        for course in courses:
            courseCode = course['course']
            lecturekey = course['lecture']
            tutorialkey = course['tutorial']

            new_data = {}
            new_data['student'] = student.pk
            course = Course.objects.get(course_code=courseCode).pk
            new_data['course'] = course
            new_data['enrollment_waitlist'] = False

            lecture = Lecture.objects.get(course=course, lecture_id=lecturekey, term=term).pk
            tutorial = None

            if tutorialkey != False:
                #print(tutorialkey)
                tutorial = Tutorial.objects.get(course=course, tutorial_id=tutorialkey, term=term_name).pk
                #print(tutorial)
                # print(Tutorial.objects.get(course=course, tutorial_id='T02', term=term_name).pk)
            new_data['lecture'] = lecture
            new_data['tutorial'] = tutorial


            enrollment = Enrollment.objects.filter(student=student.pk, lecture=lecture).first()
            if enrollment:
                #print(enrollment.lecture.pk, lecture, courseCode, enrollment.tutorial.pk)
                if enrollment.lecture.pk == lecture and  enrollment.lecture.term.pk == term_name and (not enrollment.tutorial or enrollment.tutorial.pk == tutorial):
                    results.append({courseCode: "Already enrolled in this section"})
                    continue
                
                #check enrollment in same course exists
                if enrollment.lecture.course.pk == courseCode and enrollment.lecture.term.pk ==term_name:
                    serializer = EnrollmentSerializer(enrollment, data=new_data)
                    if serializer.is_valid():
                        serializer.save()
                        results.append({courseCode: "Enrollment section changed successfully."})
                    else:
                        results.append({courseCode: "Error changing enrollment section."})

            else:
                serializer = EnrollmentSerializer(data=new_data)
                if serializer.is_valid():
                    serializer.save()
                    results.append({courseCode: "Enrolled in new course successfully"})
                else:
                    results.append({courseCode: "Error enrolling in new course"})
            print(results)
        return Response(results)

    def get(self, request, term_key, format=None):
        #student = Student.objects.first()
        student = get_object_or_404(Student, user=request.user)
        if not student:
            return Response({"error": "No student found"}, status=404)
        schedule_builder_data = {
            "allCourses": [],
            "currentSchedule": {},
            "academicRequirements": {}
        }
        try:
            term = Term.objects.get(term_key=term_key).pk
        except Term.DoesNotExist:
            return Response({"error": "Term not found"}, status=404)

        # hardcoded term
        # term = None
        # try:
        #     term = Term.objects.get(term_key="Fal2023")
        
        
        # offered course retrieval
        courses = Course.objects.all()
        for course in courses:

            if not Lecture.objects.filter(course=course, term=term).exists():
                continue
            if course.course_prerequisites == None:
                can_take = True
                prereq_codes = "none"
            else:
                can_take = True
                prereq_codes = course.course_prerequisites.split(', ')

            course_data = {
                "name": course.course_code,
                "title": course.course_title,
                "desc" : course.course_description,
                "prereq": prereq_codes,
                "prereqfilled": can_take,
                "combinations": [],
                "lectures": [],
                "tutorials": []
            }

            lectures = Lecture.objects.filter(course=course, term=term)
            for lecture in lectures:
                course_data["lectures"].append({
                    "name": lecture.lecture_id,
                    "days": lecture.lecture_days,
                    "start": lecture.lecture_starttime,
                    "end": lecture.lecture_endtime,
                    "Prof": lecture.instructor.instructor_last_name + ", " + lecture.instructor.instructor_first_name,
                    "totalSeats": lecture.lecture_totalseats, # hardcoded
                    "seatsFilled": lecture.lecture_filledseats, # hardcoded
                    "totalWaitlist": lecture.lecture_totalwaitlist, # hardcoded
                    "waitlistFilled": lecture.lecture_filledwaitlist, # hardcoded
                    "roomno": lecture.lecture_roomnumber
                })
            
            tutorials = Tutorial.objects.filter(course=course)
            for tutorial in tutorials:
                course_data["tutorials"].append({
                    "name": tutorial.tutorial_id,
                    "days": tutorial.tutorial_days,
                    "start": tutorial.tutorial_starttime,
                    "end": tutorial.tutorial_endtime,
                    "totalSeats": tutorial.tutorial_totalseats,
                    "seatsFilled": tutorial.tutorial_filledseats,
                    "totalWaitlist": tutorial.tutorial_totalwaitlist,
                    "waitlistFilled": tutorial.tutorial_filledwaitlist,
                    "roomno": tutorial.tutorial_roomnumber
                })

            for lecture in lectures:
                if(len(tutorials)) > 0:
                    for tutorial in tutorials:
                        for c in tutorial.tutorial_days:
                            if lecture.lecture_days.find(c) == -1:
                                course_data["combinations"].append([lecture.lecture_id, tutorial.tutorial_id])
                            elif lecture.lecture_starttime > tutorial.tutorial_endtime or lecture.lecture_endtime < tutorial.tutorial_starttime:
                                course_data["combinations"].append([lecture.lecture_id, tutorial.tutorial_id])
                else:
                    course_data["combinations"].append([lecture.lecture_id])
                            
            schedule_builder_data["allCourses"].append(course_data)
        
        # current schedule retrieval
        enrollments = Enrollment.objects.filter(student=student)
        termobj = Term.objects.get(pk=term)
        for enrollment in enrollments:
            if enrollment.lecture.term.pk == term:
                term_name = f"{enrollment.lecture.term.term_name} {enrollment.lecture.term.term_year}"
                schedule_builder_data["currentSchedule"][enrollment.lecture.course.course_code] = {
                    "Lecture": enrollment.lecture.lecture_id,
                    "Tutorial": enrollment.tutorial.tutorial_id if enrollment.tutorial else None
                }

        # academic requirements retrieval
        requirement_data = {
            "requirements": []
        }


        applications = StudentApplications.objects.filter(student_id=student)
        application = applications[0]
        maj_prog = application.program
        #min_prog = application.minor

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
                if status == "incomplete":
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
            if req_status == "incomplete" or req_status == "in-progress":
                requirement_data["requirements"].append({
                    "description": requirement.description,
                    "requiredUnits": requirement.required_units,
                    "status": req_status,
                    "courses": course_data
                })
        schedule_builder_data["academicRequirements"] = requirement_data

        return Response(schedule_builder_data)

    def delete(self, request, term_key, course_key, format=None):
        student = get_object_or_404(Student, user=request.user)
        data = request.data
      
        enrollments = Enrollment.objects.filter(student=student)
        if not enrollments:
            return Response({"error": "No enrollment found"}, status=404)
        for enrollment in enrollments:
            if enrollment.lecture.term.term_key == term_key and enrollment.lecture.course.course_code == course_key:
                enrollment.delete()
                return Response({"message": "Enrollment deleted successfully"}, status=204)
        return Response({"error": "Enrollment not found"}, status=404)