from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard.html', {'projects': projects})


@login_required
def create_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.owner = request.user
        project.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form})


@login_required
def create_task(request, project_id):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.project_id = project_id
        task.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form})
# Create your views here.
