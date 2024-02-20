from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Student


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
