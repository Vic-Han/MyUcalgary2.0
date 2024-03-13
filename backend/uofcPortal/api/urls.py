from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, FacultyViewSet, DepartmentViewSet, ProgramViewSet, PersonalInfoViewSet, CourseViewSet, InstructorViewSet, LectureViewSet, GradeViewSet, EnrollmentViewSet, StudentGradeView, StudentFinancesView, TransactionViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet, basename='student')
router.register('personal-info', PersonalInfoViewSet, basename='personal-info')
router.register('faculties', FacultyViewSet, basename='faculty')
router.register('departments', DepartmentViewSet, basename='department')
router.register('programs', ProgramViewSet, basename='program')
router.register('courses', CourseViewSet, basename='course')
router.register('instructors', InstructorViewSet, basename='instructor')
router.register('lectures', LectureViewSet, basename='lecture')
router.register('grades', GradeViewSet, basename='grade')
router.register('enrollments', EnrollmentViewSet, basename='enrollment')
router.register('transactions', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/student-grades/', StudentGradeView.as_view(), name='student-grade'),
    path('api/student-finances/', StudentFinancesView.as_view(), name='student-finances'),


]