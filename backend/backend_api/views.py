from django.shortcuts import render
from backend_api.serializers import CourseSerializer
from backend_api.models import Course
from rest_framework import viewsets

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer