from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import (
    Student,
    Faculty,
    Department,
    Program,
    Term,
    EmergencyContact,
    Address,
    Course,
    Instructor,
    Lecture,
    Enrollment,
    Grade,
    Transaction,
    StudentApplications,
    Requirement
)
from rest_framework.authtoken.models import Token
# Create your tests here.

class BackendTesting(APITestCase):
    
    def setUp(self):        
        # Creating user Tom and his authentication token
        self.user_tom = User.objects.create_user(username='tom.baker', email='tom.baker@ucalgary.ca', password='securepassword')
        self.token_tom = Token.objects.get(user=self.user_tom)
        
        # Setting the test client to use Tom's authentication token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_tom.key)
        
        # Additional setup for Tom's academic and personal information
        self.faculty_art_design = Faculty.objects.create(faculty_name="Art and Design")
        self.department_design = Department.objects.create(department_name="Design", faculty=self.faculty_art_design)
        self.program_graphic_design = Program.objects.create(program_name="GD", department=self.department_design, program_degree_level="Bachelor", program_honor=False)
        self.term_2024_spring = Term.objects.create(term_key="Spr2024", term_name="Spring", term_year=2024, start_date='2024-03-01', end_date='2024-06-30', due_date='2024-07-01')
        
        self.course_design_basics = Course.objects.create(course_code="DES101", course_title="Design Basics", department=self.department_design, course_units=3)
        self.instructor_jane = Instructor.objects.create(instructor_id="002", instructor_first_name="Jane", instructor_last_name="Doe", department=self.department_design)
        
        self.lecture_design = Lecture.objects.create(lecture_id="D01", term=self.term_2024_spring, course=self.course_design_basics, instructor=self.instructor_jane, lecture_days="TuTh", lecture_starttime=10.00, lecture_endtime=11.30, lecture_roomnumber="AD100")
        
        self.student_tom = Student.objects.create(user=self.user_tom, student_id="T100", student_first_name="Tom", student_last_name="Baker", date_of_birth="1995-01-15")
        
        self.enrollment_tom_design = Enrollment.objects.create(student=self.student_tom, lecture=self.lecture_design)
        self.grade_tom_design = Grade.objects.create(grade=88.0, enrollment=self.enrollment_tom_design)
        
        self.student_application_tom = StudentApplications.objects.create(application_status="Accepted",student=self.student_tom,major_program=self.program_graphic_design,concentration=False,honors_program=False)
    def test_root_endpoint(self):
        url = "/api/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_student_grades(self):
    
        url = reverse('student-grade')  # Use Django's reverse to get URL from the name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()
        
        # print("Response Json", response_json)
        
        self.assertEqual(response_json['overallGPA'], 3.3)
        self.assertEqual(response_json['letterGrade'], 'A-')

        # Validate the structure and content for "Spring 2024"
        spring_2024_activity = response_json['activity'].get('Spring 2024', {})
        self.assertNotEqual(spring_2024_activity, {}, "Spring 2024 data is missing in the response.")

        self.assertEqual(spring_2024_activity.get('UnitsEnrolled'), 3)
        self.assertEqual(spring_2024_activity.get('Program'), "GD")  # Adjusted to reflect your setup
        self.assertEqual(spring_2024_activity.get('Level'), 1)  # Assuming Level 1 for simplicity
        self.assertEqual(spring_2024_activity.get('Plan'), "Bachelor, GD")  # Adjusted to reflect your setup
        self.assertEqual(spring_2024_activity.get('TermGPA'), 3.3)
        self.assertEqual(spring_2024_activity.get('TermLetterGrade'), "A-")

        # Check the course under "Spring 2024"
        self.assertEqual(len(spring_2024_activity['courses']), 1)  # Assuming one course for simplicity
        spring_2024_course = spring_2024_activity['courses'][0]
        self.assertEqual(spring_2024_course['name'], "DES101")
        self.assertEqual(spring_2024_course['grade'], 88.0)
        self.assertEqual(spring_2024_course['letter'], "B+")  # Assuming this is the correct mapping for a grade of 88
        self.assertEqual(spring_2024_course['units'], 3)
        
        
    # def test_student_finances(self):
    #     url = reverse('student-finances')  # Use Django's reverse to get URL from the name
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response['Content-Type'], 'application/json')
    #     response_json = response.json()   
                
     

