from django.db import models

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
    courseid = models.IntegerField()
    coursename = models.CharField(max_length=255)
    prerequisite = models.CharField(max_length=255, default='None')
    program = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)
    description = models.TextField()

class Crew(models.Model):
    ROLE_CHOICES = [
        ("Professor", "Professor"),
        ("Alumni", "Alumni")
    ]

    name = models.CharField(max_length=255)
    picture = models.ImageField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    tel = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    about = models.TextField()
    
    
    
