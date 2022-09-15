from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.app_tasks.filters import TaskFilter
from task_manager.app_tasks.forms import TaskForm
from task_manager.app_tasks.models import Task
from task_manager.app_users.models import ApplicationUser
from task_manager.mixins import CheckSignInMixin

CONTEXT_NAME = 'list_of_tasks'


class ListOfTasks(CheckSignInMixin, SuccessMessageMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = CONTEXT_NAME
    filterset_class = TaskFilter


class CreateTask(CheckSignInMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'tasks/tasks_create.html'
    form_class = TaskForm
    success_message = gettext_lazy('Task successfully created')
    success_url = reverse_lazy(CONTEXT_NAME)

    def form_valid(self, form):
        author = ApplicationUser.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateTask(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = 'tasks/tasks_update.html'
    form_class = TaskForm
    success_message = gettext_lazy('Task changed successfully')
    success_url = reverse_lazy(CONTEXT_NAME)


class DeleteTask(CheckSignInMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/tasks_delete.html'
    success_url = reverse_lazy(CONTEXT_NAME)
    success_message = gettext_lazy('Task deleted successfully')

    def form_valid(self, form):
        if self.request.user != self.get_object().author:
            messages.warning(
                self.request,
                gettext_lazy("Only it's author can delete a task"),
            )
        else:
            super().form_valid(form)
        return redirect(self.success_url)


class ViewTask(CheckSignInMixin, SuccessMessageMixin, DetailView):
    model = Task
    template_name = 'tasks/tasks_view.html'
    context_object_name = 'task'
