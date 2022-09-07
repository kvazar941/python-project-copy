from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as Login
from django.contrib.messages.views import SuccessMessageMixin as Success
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.app_tasks.filters import TaskFilter
from task_manager.app_tasks.forms import TaskForm
from task_manager.app_tasks.models import Tasks
from task_manager.app_users.models import ApplicationUsers
from task_manager.mixins import CheckSignInMixin

PATHS_TO_TEMPLATES = {
    'tasks': 'tasks/tasks.html',
    'task_create': 'tasks/tasks_create.html',
    'task_update': 'tasks/tasks_update.html',
    'task_delete': 'tasks/tasks_delete.html',
    'task_view': 'tasks/tasks_view.html',
}
MESSAGES = {
    'success_create': 'Задача успешно создана',
    'success_update': 'Задача успешно изменена',
    'success_delete': 'Задача успешно удалена',
    'no_del': 'Задачу может удалить только её автор',
}


class ListOfTasks(Login, CheckSignInMixin, Success, FilterView):
    model = Tasks
    template_name = PATHS_TO_TEMPLATES['tasks']
    context_object_name = 'list_Of_tasks'
    filterset_class = TaskFilter


class CreateTask(Login, CheckSignInMixin, Success, CreateView):
    model = Tasks
    template_name = PATHS_TO_TEMPLATES['task_create']
    form_class = TaskForm
    success_message = gettext_lazy(MESSAGES['success_create'])
    success_url = reverse_lazy('list_of_tasks')

    def form_valid(self, form):
        author = ApplicationUsers.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateTask(Login, CheckSignInMixin, Success, UpdateView):
    model = Tasks
    template_name = PATHS_TO_TEMPLATES['task_update']
    form_class = TaskForm
    success_message = gettext_lazy(MESSAGES['success_update'])
    success_url = reverse_lazy('list_of_tasks')


class DeleteTask(Login, CheckSignInMixin, Success, DeleteView):
    model = Tasks
    template_name = PATHS_TO_TEMPLATES['task_delete']
    success_url = reverse_lazy('list_of_tasks')
    success_message = gettext_lazy(MESSAGES['success_delete'])

    def form_valid(self, form):
        if self.request.user != self.get_object().author:
            messages.error(self.request, gettext_lazy(MESSAGES['no_del']))
        else:
            super().form_valid(form)
        return redirect(self.success_url)


class ViewTask(Login, CheckSignInMixin, Success, DetailView):
    model = Tasks
    template_name = PATHS_TO_TEMPLATES['task_view']
    context_object_name = 'task'
