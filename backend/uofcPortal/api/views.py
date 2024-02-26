from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Student, Faculty, Department, Program
from .serializers import StudentSerializer, UserSerializer, FacultySerializer, DepartmentSerializer, ProgramSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Assuming the user is linked to the student via a ForeignKey
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