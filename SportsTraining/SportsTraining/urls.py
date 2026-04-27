from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from SportsTrainingApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('workouts/', views.workouts, name='workouts'),
    path('progress/', views.progress, name='progress'),
    path('profile/', views.profile, name='profile'),
    path('enrol/<int:module_id>/', views.enrol_module, name='enrol_module'),

    # 🔥 ADD THIS (LOGIN SYSTEM)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]