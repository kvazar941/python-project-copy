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


class ListOfTasks(Login, CheckSignInMixin, Success, FilterView):
    model = Tasks
    template_name = 'tasks/tasks.html'
    context_object_name = 'list_Of_tasks'
    filterset_class = TaskFilter


class CreateTask(Login, CheckSignInMixin, Success, CreateView):
    model = Tasks
    template_name = 'tasks/tasks_create.html'
    form_class = TaskForm
    success_message = gettext_lazy('Task successfully created')
    success_url = reverse_lazy('list_of_tasks')

    def form_valid(self, form):
        author = ApplicationUsers.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateTask(Login, CheckSignInMixin, Success, UpdateView):
    model = Tasks
    template_name = 'tasks/tasks_update.html'
    form_class = TaskForm
    success_message = gettext_lazy('Task changed successfully')
    success_url = reverse_lazy('list_of_tasks')


class DeleteTask(Login, CheckSignInMixin, Success, DeleteView):
    model = Tasks
    template_name = 'tasks/tasks_delete.html'
    success_url = reverse_lazy('list_of_tasks')
    success_message = gettext_lazy('Task deleted successfully')

    def form_valid(self, form):
        if self.request.user != self.get_object().author:
            messages.error(
                self.request,
                gettext_lazy('Only its author can delete a task')
            )
        else:
            super().form_valid(form)
        return redirect(self.success_url)


class ViewTask(Login, CheckSignInMixin, Success, DetailView):
    model = Tasks
    template_name = 'tasks/tasks_view.html'
    context_object_name = 'task'
