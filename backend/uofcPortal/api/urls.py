from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]