from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, DepartmentViewSet, ProgramViewSet, StudentViewSet, CourseViewSet, InstructorViewSet, LectureViewSet, GradeViewSet

router = DefaultRouter()
router.register('faculty', FacultyViewSet)
router.register('deparment', DepartmentViewSet)
router.register('program', ProgramViewSet)
router.register('student', StudentViewSet)
router.register('course', CourseViewSet)
router.register('instructor', InstructorViewSet)
router.register('lecture', LectureViewSet)
router.register('grade', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]