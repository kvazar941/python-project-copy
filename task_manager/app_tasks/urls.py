from django.urls import path

from task_manager.app_tasks.views import (CreateTask, DeleteTask, ListOfTasks,
                                          UpdateTask, ViewTask)

urlpatterns = [
    path('', ListOfTasks.as_view(), name='list_of_tasks'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('<int:pk>/', ViewTask.as_view(), name='view_task'),
]
