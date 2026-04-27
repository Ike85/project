from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, TrainingModule, EnrolmentModule, Session


@login_required
def home(request):
    return render(request, "home.html", {
        "student_count": Student.objects.count(),
        "module_count": TrainingModule.objects.count(),
        "enrolment_count": EnrolmentModule.objects.count(),
        "session_count": Session.objects.count(),

    })
    return render(request, "home.html", context)



@login_required
def workouts(request):
    modules = TrainingModule.objects.all()
    return render(request, "workouts.html", {"modules": modules})


@login_required
def enrol_module(request, module_id):
    student = Student.objects.filter(user=request.user).first()
    module = get_object_or_404(TrainingModule, id=module_id)

    if student:
        EnrolmentModule.objects.get_or_create(
            athlete=student,
            module=module,
            defaults={"status": "Enrolled", "progress": "0%"}
        )

    return redirect("workouts")


@login_required
def progress(request):
    student = Student.objects.filter(user=request.user).first()
    enrolments = EnrolmentModule.objects.filter(athlete=student) if student else []

    return render(request, "progress.html", {"enrolments": enrolments})


@login_required
def profile(request):
    student = Student.objects.filter(user=request.user).first()
    enrolments = EnrolmentModule.objects.filter(athlete=student) if student else []

    return render(request, "profile.html", {
        "student": student,
        "enrolments": enrolments
    })