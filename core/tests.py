from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Project, Task


class ModelTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password',
            role='student'
        )

        self.project = Project.objects.create(
            name='Test Project',
            description='Test Description',
            owner=self.user
        )

    def test_user_created(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_project_created(self):
        self.assertEqual(self.project.name, 'Test Project')

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Task Desc',
            status='todo',
            due_date='2026-01-01',
            project=self.project,
            assignee=self.user
        )
        self.assertEqual(task.title, 'Test Task')


class ViewTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password',
            role='student'
        )

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_access_dashboard(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)


class ProjectTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='teacher',
            password='password',
            role='teacher'
        )
        self.client.login(username='teacher', password='password')

    def test_create_project(self):
        response = self.client.post('/project/create/', {
            'name': 'New Project',
            'description': 'Test Description'
        })
        self.assertEqual(response.status_code, 302)