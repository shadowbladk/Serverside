from rest_framework import serializers
from backend_api.models import Course, Professor, Alumni, News

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'
        
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = '__all__'