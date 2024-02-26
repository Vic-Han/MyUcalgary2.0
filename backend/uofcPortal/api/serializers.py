from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Student, Faculty, Department, Program


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