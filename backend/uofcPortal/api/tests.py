import json
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import (Student,Faculty,Department,Program,Term,EmergencyContact,Address,Course,Instructor,Lecture,Enrollment,Grade,Transaction,StudentApplications,Requirement)
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
        self.minor_program = Program.objects.create(program_name="None",department=self.department_design,program_degree_level="Bachelor",program_honor=False)
        self.term_2024_spring = Term.objects.create(term_key="Spr2024", term_name="Spring", term_year=2024, start_date='2024-03-01', end_date='2024-06-30', due_date='2024-07-01')
        
        self.course_design_basics = Course.objects.create(course_code="DES101", course_title="Design Basics", department=self.department_design, course_units=3)
        self.instructor_jane = Instructor.objects.create(instructor_id="002", instructor_first_name="Jane", instructor_last_name="Doe", department=self.department_design)
        
        self.lecture_design = Lecture.objects.create(lecture_id="D01", term=self.term_2024_spring, course=self.course_design_basics, instructor=self.instructor_jane, lecture_days="TuTh", lecture_starttime=10.00, lecture_endtime=11.30, lecture_roomnumber="AD100")
        
        self.student_tom = Student.objects.create(user=self.user_tom, student_id="T100", student_first_name="Tom", student_last_name="Baker", date_of_birth="1995-01-15")
        
        self.enrollment_tom_design = Enrollment.objects.create(student=self.student_tom, lecture=self.lecture_design)
        self.grade_tom_design = Grade.objects.create(grade=88.0, enrollment=self.enrollment_tom_design)
        
        self.student_application_tom = StudentApplications.objects.create(application_status="Accepted",student=self.student_tom,major=self.program_graphic_design.program_name,minor=self.minor_program.program_name,concentration=False,program=self.program_graphic_design)  # Directly linking to a Program instance
        
        self.transaction_spring = Transaction.objects.create(transaction_name="Spring Transaction",transaction_posted_date="2024-03-01",transaction_type="debit",  transaction_amount=-5000.00,student=self.student_tom, term=self.term_2024_spring)

        self.requirement_core = Requirement.objects.create(description="Complementary Studies",required_units=3,program=self.program_graphic_design)
        
 
        
        

        
        
    def test_root_endpoint(self):
        url = "/api/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_student_grades(self):
    
        url = reverse('student-grade')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()
        
        #this part of printing could be commented out
        formatted_new_json = json.dumps(response_json, indent=4)
        print(formatted_new_json)
        print("-------------end of student grades endpoint check------------------")
        
        self.assertEqual(response_json['overallGPA'], 3.3)
        self.assertEqual(response_json['letterGrade'], 'A-')

        # Validate the structure and content for "Spring 2024"
        spring_2024_activity = response_json['activity'].get('Spring 2024', {})
        self.assertNotEqual(spring_2024_activity, {}, "Spring 2024 data is missing in the response.")

        self.assertEqual(spring_2024_activity.get('UnitsEnrolled'), 3)
        self.assertEqual(spring_2024_activity.get('Program'), "GD")  
        self.assertEqual(spring_2024_activity.get('Level'), 1)  
        self.assertEqual(spring_2024_activity.get('Plan'), "Bachelor, GD")  
        self.assertEqual(spring_2024_activity.get('TermGPA'), 3.3)
        self.assertEqual(spring_2024_activity.get('TermLetterGrade'), "A-")

        # Check the course under "Spring 2024"
        self.assertEqual(len(spring_2024_activity['courses']), 1)  
        spring_2024_course = spring_2024_activity['courses'][0]
        self.assertEqual(spring_2024_course['name'], "DES101")
        self.assertEqual(spring_2024_course['grade'], 88.0)
        self.assertEqual(spring_2024_course['letter'], "B+")  
        self.assertEqual(spring_2024_course['units'], 3)
        
        
    def test_student_finances(self):
        # Fetching the student-finances endpoint
        url = reverse('student-finances')  # Ensure you have named your URL route as 'student-finances'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()
        
        #this part of printing could be commented out
        formatted_new_json = json.dumps(response_json, indent=4)
        print(formatted_new_json)
        print("-------------end of student finances endpoint check------------------")
        
        self.assertAlmostEqual(response_json["paid"],0.0, places=2, msg="Paid amount does not match expected value.")
        self.assertAlmostEqual(response_json["awards"], 0.0, places=2, msg="Awards amount does not match expected value.")
        self.assertAlmostEqual(response_json["due"], 5000.0, places=2, msg="Due amount does not match expected value.")
        self.assertEqual(response_json["selectedTerm"], "Spring 2024", msg="Selected term does not match expected value.")

        # Check for the expected transaction within "Spring 2024"   
        expected_spring_2024_activities = [{
            "name": "Spring Transaction",  # Name as per setup
            "date": "2024-03-01",  # Date as per setup
            "amount": 5000.0,  # Amount as per setup
            "type": "debit"  # Type as per setup
        }]
        self.assertIn("Spring 2024", response_json["activity"], "Spring 2024 data is missing in the response.")
        self.assertEqual(len(response_json["activity"]["Spring 2024"]), 1, "Expected number of transactions in Spring 2024 does not match.")
        self.assertDictEqual(response_json["activity"]["Spring 2024"][0], expected_spring_2024_activities[0], "Spring 2024 activity does not match expected data.")
        
    
    def test_personal_info_endpoint(self):
        url = reverse('personal-info')  # Ensure you have named your URL route as 'personal-info'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()

        # Check if the response contains all expected keys
        expected_keys = ['personal_info', 'citizenship', 'address', 'phone_numbers', 'email', 'emergency_contact']
        for key in expected_keys:
            self.assertIn(key, response_json, msg=f"{key} is missing in the response")

        # Verify some specific personal information details
        self.assertEqual(response_json['personal_info']['firstname'], 'Tom')
        self.assertEqual(response_json['personal_info']['lastname'], 'Baker')
        self.assertEqual(response_json['personal_info']['UCID'], 'T100')
        



    def test_student_requirements_view(self):
        url = reverse('course-requirements')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()

        # Check the presence of programInfo and requirements sections
        self.assertIn('programInfo', response_json)
        self.assertIn('requirements', response_json)

        # Validate program information is as expected
        expected_program_info = {
            'degree': self.program_graphic_design.program_degree_level,
            'major': self.program_graphic_design.program_name,
            'minor': self.minor_program.program_name,
            'concentration': 'none',
            'year': '3',  # Assuming logic for calculating year
            'academicLoad': 'full-time'
        }
        self.assertDictEqual(response_json['programInfo'], expected_program_info)

        # Validate at least one requirement is listed with expected structure
        self.assertGreater(len(response_json['requirements']), 0)
        for requirement in response_json['requirements']:
            self.assertIn('description', requirement)
            self.assertIn('requiredUnits', requirement)
            self.assertIn('remainingUnits', requirement)
            self.assertIn('status', requirement)
            self.assertIn('optional', requirement)
            self.assertIn('courses', requirement)
            

    def test_retrieve_student_applications(self):
        url = reverse('student-applications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertTrue("Undergrad applications" in response_data)  # Check for keys or specific data as needed

    def test_delete_student_application(self):
        application_to_delete = StudentApplications.objects.create(
            application_status="Pending",
            student=self.student_tom,
            major="Test Major",
            minor="Test Minor",
            concentration=False,
            program=self.program_graphic_design
        )
        url = reverse('student-applications')
        response = self.client.delete(url, {"application_id": application_to_delete.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(StudentApplications.objects.count(), 1)  # Assuming one was created in setUp

    

 