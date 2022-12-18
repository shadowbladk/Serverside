from django.shortcuts import render
from backend_api.serializers import CourseSerializer, CrewSerializer
from backend_api.models import Course, Crew
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]