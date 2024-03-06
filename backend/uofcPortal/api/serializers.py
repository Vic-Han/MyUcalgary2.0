from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Student, Faculty, Department, Program, Course, Instructor, Lecture, Grade


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


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



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
            "country": obj.country,
            "status": obj.citizenship_status
        }

    def get_address(self, obj):
        return {
            "street address": obj.street_address,
            "postal code": obj.postal_code,
            "city": obj.city,
            "province/state": obj.province
        }

    def get_phone_numbers(self, obj):
        return {
            "home": obj.primary_phone_number,
            "cell": obj.secondary_phone_number if obj.secondary_phone_number else None
        }

    def get_email(self, obj):
        return {
            "personal": obj.personal_email,
            "school": obj.school_email
        }

    def get_emergency_contact(self, obj):
        return {
            "name": obj.emergency_contact_name,
            "phone": obj.emergency_contact_phone,
            "relation": obj.emergency_contact_relationship
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

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

