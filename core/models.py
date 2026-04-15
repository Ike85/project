from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.project}"


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

