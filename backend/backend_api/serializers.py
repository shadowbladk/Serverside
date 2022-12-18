from rest_framework import serializers
from backend_api.models import Course, Crew

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CrewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'