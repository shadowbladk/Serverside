from django.shortcuts import render
from course_api.serializers import CourseSerializer
from course_api.models import Course
from rest_framework import viewsets

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer