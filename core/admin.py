from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(TaskComment)
