from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Course(models.Model):
    YEAR_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    SEMESTER_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3)
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    courseid = models.CharField(max_length=255)
    coursename = models.CharField(max_length=255)
    prerequisite = models.CharField(max_length=255, default='None')
    program = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)
    description = models.TextField()

class Professor(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    picture = CloudinaryField('image')
    tel = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    about = models.TextField()

class Alumni(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    picture = CloudinaryField('image')
    tel = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    about = models.TextField()

class News(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    picture = CloudinaryField('image', null=True)
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)