from django.contrib import admin

from task_manager.app_tasks.models import Task

admin.site.register(Task)
