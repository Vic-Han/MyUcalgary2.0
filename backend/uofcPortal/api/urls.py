from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

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
router.register('tutorials', TutorialViewSet, basename='tutorial')
router.register('terms', TermViewSet, basename='term')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/student-grades/', StudentGradeView.as_view(), name='student-grade'),
    path('api/student-finances/', StudentFinancesView.as_view(), name='student-finances'),
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/student-applications/', StudentApplicationsViewSet.as_view(), name='student-applications'),
    path('api/course-requirements/', StudentRequirementsView.as_view(), name='course-requirements'),
    path('api/schedule-builder/', ScheduleBuilderView.as_view(), name='schedule-builder')
]