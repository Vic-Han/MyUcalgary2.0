from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import *

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

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
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