from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.studentName


class TrainingModule(models.Model):
    moduleTitle = models.CharField(max_length=100)
    moduleDescription = models.TextField()
    moduleCoach = models.CharField(max_length=100)
    moduleDate = models.DateField()

    def __str__(self):
        return self.moduleTitle


class EnrolmentModule(models.Model):
    athlete = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(TrainingModule, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Enrolled")
    progress = models.CharField(max_length=20, default="0%")

    def __str__(self):
        return f"{self.athlete} - {self.module}"


class Session(models.Model):
    module = models.ForeignKey(TrainingModule, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.module} - {self.date}"


class Attendance(models.Model):
    athlete = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.athlete} - {self.status}"