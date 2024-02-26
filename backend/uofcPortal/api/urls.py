from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, FacultyViewSet, DepartmentViewSet, ProgramViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet, basename='student')
router.register('faculties', FacultyViewSet, basename='faculty')
router.register('departments', DepartmentViewSet, basename='department')
router.register('programs', ProgramViewSet, basename='program')

urlpatterns = [
    path('api/', include(router.urls)),
]