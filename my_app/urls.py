from django.urls import path
from .views import home
from .views import student_api


urlpatterns = [
    path('', home),
    path('students/', student_api)
]