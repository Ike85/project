from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('project/create/', views.create_project, name='create_project'),
    path('task/create/<int:project_id>/', views.create_task, name='create_task'),
]