from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Student, Requirement, Faculty, Tutorial, Lab, Department, Program, Course, Instructor, Lecture, Grade, Enrollment, Address, Transaction, StudentApplications


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # to hide the password from the response
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # for creating a new user and hashing the password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user) # to create a token for new users
        return user

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    emergency_contact1 = serializers.SerializerMethodField()
    emergency_contact2 = serializers.SerializerMethodField()
    emergency_contact3 = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = '__all__'
    def get_address(self,obj):
        address = obj.address
        if address:
            return f"{address.address_country},{address.address_province},{address.address_city},{address.address_street_address}, {address.address_postal_code}"
        return ""
    def get_emergency_contact1(self,obj):
        if obj.emergency_contact1:
            return f"{obj.emergency_contact1.emergency_contact_name},{obj.emergency_contact1.emergency_contact_phone},{obj.emergency_contact1.emergency_contact_relationship}"
        return None
    def get_emergency_contact2(self,obj):
        if obj.emergency_contact2:
            return f"{obj.emergency_contact2.emergency_contact_name},{obj.emergency_contact2.emergency_contact_phone},{obj.emergency_contact2.emergency_contact_relationship}"
        return None
    def get_emergency_contact3(self,obj):
        if obj.emergency_contact3:
            return f"{obj.emergency_contact3.emergency_contact_name},{obj.emergency_contact3.emergency_contact_phone},{obj.emergency_contact3.emergency_contact_relationship}"
        return None
    


class PersonalInfoSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()
    citizenship = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    phone_numbers = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    emergency_contact = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ('personal_info', 'citizenship', 'address', 'phone_numbers', 'email', 'emergency_contact')

    def get_personal_info(self, obj):
        return {
            "firstname": obj.student_first_name,
            "lastname": obj.student_last_name,
            "UCID": obj.student_id,
            "date of birth": obj.date_of_birth
        }

    def get_citizenship(self, obj):
        return {
            "country": obj.address.address_country,
            "status": obj.citizenship_status
        }

    def get_address(self, obj):
        return {
            "street address": obj.address.address_street_address,
            "postal code": obj.address.address_postal_code,
            "city": obj.address.address_city,
            "province/state": obj.address.address_province
        }

    def get_phone_numbers(self, obj):
        return {
            "home": obj.home_phone_number if obj.home_phone_number else None,
            "mobile": obj.mobile_phone_number if obj.mobile_phone_number else None,
            "other": obj.other_phone_number if obj.other_phone_number else None,
            "preferred": obj.preferred_phone
        }

    def get_email(self, obj):
        return {
            "personal": obj.personal_email,
            "school": obj.school_email, 
            "preferred": obj.preferred_email
        }

    def get_emergency_contact(self, obj):
        return {
            "name1": obj.emergency_contact1.emergency_contact_name,
            "phone1": obj.emergency_contact1.emergency_contact_phone,
            "relation1": obj.emergency_contact1.emergency_contact_relationship,
            "name2": obj.emergency_contact2.emergency_contact_name if obj.emergency_contact2.emergency_contact_name else None,
            "phone2": obj.emergency_contact2.emergency_contact_phone if obj.emergency_contact2.emergency_contact_phone else None,
            "relation2": obj.emergency_contact2.emergency_contact_relationship if obj.emergency_contact2.emergency_contact_relationship else None,
            "name3": obj.emergency_contact3.emergency_contact_name if obj.emergency_contact3.emergency_contact_name else None,
            "phone3": obj.emergency_contact3.emergency_contact_phone if obj.emergency_contact3.emergency_contact_phone else None,
            "relation3": obj.emergency_contact3.emergency_contact_relationship if obj.emergency_contact3.emergency_contact_relationship else None,
            "preferred": obj.preferred_emergency_contact
        }

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class StudentApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplications
        fields = '__all__'

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'