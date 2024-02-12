from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, DepartmentViewSet, ProgramViewSet

router = DefaultRouter()
router.register('faculty', FacultyViewSet)
router.register('deparment', DepartmentViewSet)
router.register('program', ProgramViewSet)

# router.register('user', UserViewSet)
# router.register('course', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]