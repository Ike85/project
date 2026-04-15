from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    studentName = models.CharField(max_length=100)
    age = models.IntegerField()

class Module(models.Model):
    module_id = models.IntegerField(primary_key=True)
    moduleTitle = models.CharField(max_length=100)
    moduleDescription = models.CharField(max_length=100)
    moduleStatus = models.CharField(max_length=100)