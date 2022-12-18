from django.db import models

# Create your models here.

class Course(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    courseid = models.IntegerField()
    coursename = models.CharField(max_length=255)
    prerequisite = models.CharField(max_length=255, default='None')
    program = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)
    description = models.TextField()
