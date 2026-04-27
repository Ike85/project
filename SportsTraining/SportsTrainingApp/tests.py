from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Student, TrainingModule, EnrolmentModule, Session, Attendance


class StudentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="john", password="pass1234")

    def test_create_student(self):
        student = Student.objects.create(
            user=self.user,
            studentName="John",
            age=20
        )

        self.assertEqual(student.studentName, "John")
        self.assertEqual(student.age, 20)


class TrainingModuleTestCase(TestCase):

    def test_create_training_module(self):
        module = TrainingModule.objects.create(
            moduleTitle="Football",
            moduleDescription="Football training",
            moduleCoach="Coach A",
            moduleDate="2026-04-20"
        )

        self.assertEqual(module.moduleTitle, "Football")
        self.assertEqual(module.moduleCoach, "Coach A")


class EnrolmentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="mike", password="pass1234")

        self.student = Student.objects.create(
            user=self.user,
            studentName="Mike",
            age=22
        )

        self.module = TrainingModule.objects.create(
            moduleTitle="Gym",
            moduleDescription="Gym training",
            moduleCoach="Coach B",
            moduleDate="2026-04-20"
        )

    def test_enrol_student_in_module(self):

        enrolment = EnrolmentModule.objects.create(
            athlete=self.student,
            module=self.module,
            status="In Progress",
            progress="50%"
        )

        self.assertEqual(enrolment.athlete.studentName, "Mike")
        self.assertEqual(enrolment.module.moduleTitle, "Gym")


class AttendanceTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="liam", password="pass1234")

        self.student = Student.objects.create(
            user=self.user,
            studentName="Liam",
            age=25
        )

        self.module = TrainingModule.objects.create(
            moduleTitle="Cardio",
            moduleDescription="Cardio training",
            moduleCoach="Coach C",
            moduleDate="2026-04-20"
        )

        self.session = Session.objects.create(
            module=self.module,
            date="2026-04-20",
            duration=2
        )

    def test_attendance_record(self):

        attendance = Attendance.objects.create(
            athlete=self.student,
            session=self.session,
            status="present"
        )

        self.assertEqual(attendance.status, "present")
        self.assertEqual(attendance.athlete.studentName, "Liam")


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="pass1234")

    def test_login_required_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_login_access_home(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_workouts_page(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/workouts/")
        self.assertEqual(response.status_code, 200)

    def test_progress_page(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/progress/")
        self.assertEqual(response.status_code, 200)