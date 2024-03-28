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
        self.term_2024_Winter = Term.objects.create(term_key="Win2024", term_name="Winter", term_year=2024, start_date='2024-01-03', end_date='2024-04-30', due_date='2024-04-30')
        self.term_2023_fall = Term.objects.create(term_key="Fal2023", term_name="Fall", term_year=2023, start_date='2023-09-01', end_date='2023-12-30', due_date='2023-12-30')
        self.course_design_basics = Course.objects.create(course_code="DES101", course_title="Design Basics", department=self.department_design, course_units=3)
        self.instructor_jane = Instructor.objects.create(instructor_id="002", instructor_first_name="Jane", instructor_last_name="Doe", department=self.department_design)
        
        self.lecture_design = Lecture.objects.create(lecture_id="D01", term=self.term_2023_fall, course=self.course_design_basics, instructor=self.instructor_jane, lecture_days="TuTh", lecture_starttime=10.00, lecture_endtime=11.30, lecture_roomnumber="AD100")
        
        self.student_tom = Student.objects.create(user=self.user_tom, student_id="T100", student_first_name="Tom", student_last_name="Baker", date_of_birth="1995-01-15")
        
        self.enrollment_tom_design = Enrollment.objects.create(student=self.student_tom, lecture=self.lecture_design)
        self.grade_tom_design = Grade.objects.create(grade=88.0, enrollment=self.enrollment_tom_design)
        
        self.student_application_tom = StudentApplications.objects.create(application_status="Accepted",student=self.student_tom,major=self.program_graphic_design.program_name,minor=self.minor_program.program_name,concentration=False,program=self.program_graphic_design,app_type="Undergrad")  # Directly linking to a Program instance
        
        self.transaction_fall = Transaction.objects.create(transaction_name="Fall Transaction",transaction_posted_date="2023-10-01",transaction_type="debit",  transaction_amount=-5000.00,student=self.student_tom, term=self.term_2023_fall)

        self.requirement_core = Requirement.objects.create(description="Complementary Studies",required_units=3,program=self.program_graphic_design)
        
        self.program = Program.objects.create(program_name="Test Program", department=self.department_design, program_degree_level="Masters", program_honor=False)
        
        
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
        print("-------------start of student grades endpoint check------------------")
        print(formatted_new_json)
        print("-------------end of student grades endpoint check------------------")
        
        self.assertEqual(response_json['overallGPA'], 3.3)
        self.assertEqual(response_json['letterGrade'], 'B+')

        # Validate the structure and content for "Spring 2024"
        fall_2023_activity = response_json['activity'].get('Fall 2023', {})
        self.assertNotEqual(fall_2023_activity, {}, "Fall 2023 data is missing in the response.")

        self.assertEqual(fall_2023_activity.get('UnitsEnrolled'), 3)
        self.assertEqual(fall_2023_activity.get('Program'), "GD")  
        self.assertEqual(fall_2023_activity.get('Level'), 1)  
        self.assertEqual(fall_2023_activity.get('Plan'), "Bachelor, GD")  
        self.assertEqual(fall_2023_activity.get('TermGPA'), 3.3)
        self.assertEqual(fall_2023_activity.get('TermLetterGrade'), "B+")

        # Check the course under "Spring 2024"
        self.assertEqual(len(fall_2023_activity['courses']), 1)  
        fall_2023_course = fall_2023_activity['courses'][0]
        self.assertEqual(fall_2023_course['name'], "DES101")
        self.assertEqual(fall_2023_course['grade'], 88.0)
        self.assertEqual(fall_2023_course['letter'], "B+")  
        self.assertEqual(fall_2023_course['units'], 3)
        
        
    def test_student_finances(self):
        # Fetching the student-finances endpoint
        url = reverse('student-finances')  # Ensure you have named your URL route as 'student-finances'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()
        
        #this part of printing could be commented out
        formatted_new_json = json.dumps(response_json, indent=4)
        print("------start of student finances endpoint----------")
        print(formatted_new_json)
        print("-------------end of student finances endpoint check------------------")
        
        self.assertAlmostEqual(response_json["paid"],0.0, places=2, msg="Paid amount does not match expected value.")
        self.assertAlmostEqual(response_json["awards"], 0.0, places=2, msg="Awards amount does not match expected value.")
        self.assertAlmostEqual(response_json["due"], 0.0, places=2, msg="Due amount does not match expected value.")
        self.assertEqual(response_json["selectedTerm"], "Fall 2023", msg="Selected term does not match expected value.")

        # Check for the expected transaction within "Fall 2023"   
        expected_Fall_2023_activities = [{
            "name": "Fall Transaction",  # Name as per setup
            "date": "2023-10-01",  # Date as per setup
            "amount": 5000.0,  # Amount as per setup
            "type": "debit"  # Type as per setup
        }]
        self.assertIn("Fall 2023", response_json["activity"], "Spring 2024 data is missing in the response.")
        self.assertEqual(len(response_json["activity"]["Fall 2023"]), 1, "Expected number of transactions in Fall 2023 does not match.")
        self.assertDictEqual(response_json["activity"]["Fall 2023"][0], expected_Fall_2023_activities[0], "Fall 2023 activity does not match expected data.")
        
    
    def test_personal_info_endpoint(self):
        url = reverse('personal-info')  # Ensure you have named your URL route as 'personal-info'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_json = response.json()

        formatted_new_json = json.dumps(response_json, indent=4)
        print("------start of personal info endpoint----------")
        print(formatted_new_json)
        print("-------------end of personal info endpoint check------------------")
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

        formatted_new_json = json.dumps(response_json, indent=4)
        print("------start of requirement endpoint----------")
        print(formatted_new_json)
        print("-------------end of requirement endpoint check------------------")
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


    
    def test_schedule_builder(self):
        # Assuming the URL name for ScheduleBuilderView is 'schedule-builder'
        term_key = self.term_2023_fall.term_key
        url = reverse('schedule-builder-get',args=[term_key])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Schedule Builder endpoint response status code mismatch.")
        response_data = response.json()
        
        # Check for allCourses, currentSchedule, and academicRequirements in the response
        self.assertIn('allCourses', response_data, "allCourses is missing in the response.")
        self.assertIn('currentSchedule', response_data, "currentSchedule is missing in the response.")
        self.assertIn('academicRequirements', response_data, "academicRequirements is missing in the response.")

        # Validate structure of a course in allCourses
        if response_data['allCourses']:
            course = response_data['allCourses'][0]
            self.assertIn('name', course, "Course name is missing.")
            self.assertIn('title', course, "Course title is missing.")
            self.assertIn('desc', course, "Course description is missing.")
            self.assertIn('prereq', course, "Course prerequisites are missing.")
            self.assertIn('prereqfilled', course, "prereqfilled flag is missing.")
            self.assertIn('lectures', course, "Course lectures are missing.")
            self.assertIn('tutorials', course, "Course tutorials are missing.")

        # Validate structure of currentSchedule
        for course_code, schedule in response_data['currentSchedule'].items():
            self.assertIn('Lecture', schedule, f"Lecture information is missing for {course_code}.")
            self.assertIn('Tutorial', schedule, f"Tutorial information is missing for {course_code}.")

        # Validate structure of academicRequirements
        for requirement in response_data['academicRequirements']['requirements']:
            self.assertIn('description', requirement, "Requirement description is missing.")
            self.assertIn('requiredUnits', requirement, "Required units for requirement are missing.")
            self.assertIn('status', requirement, "Requirement status is missing.")
            self.assertIn('courses', requirement, "Required courses for requirement are missing.")


    def test_dashBoard(self):
        print("------------start of dashboard endpoint test-----------------")
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Dashboard endpoint response status code mismatch.")

        response_data = response.json()
        formatted_new_json = json.dumps(response_data, indent=4)
        print(formatted_new_json)
        # Assert main sections exist
        self.assertIn('grades', response_data, "Grades section is missing in the response.")
        self.assertIn('finances', response_data, "Finances section is missing in the response.")
        self.assertIn('schedule', response_data, "Schedule section is missing in the response.")

        # Check the grades data
        expected_grades_data = {
            'Fall 2023': {
                'TermGPA': 3.3,
                'TermLetterGrade': 'B+',
                'courses': [{
                    'name': "DES101",
                    'grade': 88.0,
                    'letter': 'B+',
                }]
            }
        }
        self.assertEqual(response_data['grades'], expected_grades_data, "Grades data does not match expected.")

        # Check the finances data
        expected_finances_data = {
            'Fall 2023': {
                'credits': 0,
                'debits': -5000.0,
                'net_balance': -5000.0,
                'due': '2023-12-30',
            }
        }
        self.assertEqual(response_data['finances'], expected_finances_data, "Finances data does not match expected.")

        # Check the schedule data
        expected_schedule_data = []  # Assuming no current enrollments are added to the schedule in the setup
        self.assertEqual(response_data['schedule'], expected_schedule_data, "Schedule data does not match expected.")

        print("-------------end of dashboard endpoint test------------------")




    def test_create_student_application(self):
        # Assuming 'student-applications' is the correct URL name for posting a new application
        url = reverse('student-applications')

        # Construct the data to POST based on your application model
        application_data = {
            "type": "undergrad", # Or "grad" based on your setup
            "program": "Test Program",
            "minor": "None", # Assuming a minor can be "None"
            "concentration": "None"
        }

        # Make a POST request with the application data
        response = self.client.post(url, application_data, format='json')

        # Check the response status code (201 created)
        self.assertEqual(response.status_code, 201)

        applications = StudentApplications.objects.filter(student=self.student_tom)
        
        # Then either check that the count of applications is what you expect,
        self.assertTrue(applications.count() > 0, "No applications found for student.")
        
        # And/or perform checks on the applications themselves. For example:
        latest_application = applications.latest('id')  # Assuming you have a DateTime or similar field to determine the latest.
        self.assertEqual(latest_application.program.program_name, "Test Program")
        self.assertEqual(latest_application.application_status, "Under Review")
    
    
    def test_retrieve_student_applications(self):
        # Create an application to retrieve
        StudentApplications.objects.create(application_status="Under Review", student=self.student_tom, program=self.program, app_type="undergrad")

        # Assuming 'student-applications' is the correct URL name for retrieving applications
        url = reverse('student-applications')

        # Make a GET request
        response = self.client.get(url, format='json')

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Verify the response data contains the application
        self.assertIn("Undergrad applications", response.data)
        self.assertEqual(len(response.data["Undergrad applications"]), 1)  # Assuming there is one application
        self.assertEqual(response.data["Undergrad applications"][0]["program"], "GD")