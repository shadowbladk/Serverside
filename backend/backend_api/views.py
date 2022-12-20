from django.shortcuts import render
from django.http.response import Http404
from backend_api.serializers import CourseSerializer, ProfessorSerializer, AlumniSerializer, NewsSerializer, NewsPostSerializer
from backend_api.models import Course, Professor, Alumni, News
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

# class ProfessorAPIView(viewsets.ModelViewSet):
#     pagination_class = LimitOffsetPagination
    
#     def get_object(self, pk):
#         try:
#             return Professor.objects.get(pk=pk)
#         except Professor.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk=None, format=None):
#         if pk:
#             data = self.get_object(pk)
#             serializer = ProfessorSerializer(data)
#         else:
#             data = Professor.objects.all()
#             serializer = ProfessorSerializer(data, many=True)
#         return Response(serializer.data)
        
#     def post(self, request, format=None):
#         data = request.data
#         serializer = ProfessorPostSerializer(data=data)

#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         response = Response()
#         response.data = {
#             'message': 'Professor profile Created Successfully',
#             'data': serializer.data
#         }

#         return response

#     def put(self, request, pk):
#         old_data = self.get_object(pk)
#         if not old_data:
#             return Response({'message': 'The data is not found'}, Http404)

#         data = request.data
#         serializer = ProfessorPostSerializer(old_data, data=data)

#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         response = Response()
#         response.data = {
#             'message': 'Professor profile Updated Successfully',
#             'data': serializer.data
#         }

#         return response
        

#     def delete(self, request, pk, format=None):
#         professor_to_delete = Professor.objects.get(pk=pk)
#         professor_to_delete.delete()
#         return Response({
#             'message': 'Professor profile Deleted Successfully'
#         })

class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

class NewsAPIView(APIView):
    pagination_class = LimitOffsetPagination
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = NewsSerializer(data)
        else:
            data = News.objects.all()
            serializer = NewsSerializer(data, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        data = request.data
        serializer = NewsPostSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'News Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk):
        old_data = self.get_object(pk)
        if not old_data:
            return Response({'message': 'The data is not found'}, Http404)

        data = request.data
        serializer = NewsPostSerializer(old_data, data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'News Updated Successfully',
            'data': serializer.data
        }

        return response
        

    def delete(self, request, pk, format=None):
        professor_to_delete = Professor.objects.get(pk=pk)
        professor_to_delete.delete()
        return Response({
            'message': 'News Deleted Successfully'
        })