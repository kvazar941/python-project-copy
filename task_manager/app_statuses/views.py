from django.contrib.auth.mixins import LoginRequiredMixin as Login
from django.contrib.messages.views import SuccessMessageMixin as Success
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  UpdateView)

from task_manager.app_statuses.forms import StatusesForm
from task_manager.app_statuses.models import Statuses
from task_manager.mixins import CheckDeleteMixin as Delete
from task_manager.mixins import CheckSignInMixin as Sign

PATHS_TO_TEMPLATES = {
    'statuses': 'statuses/statuses.html',
    'status_create': 'statuses/statuses_create.html',
    'status_update': 'statuses/statuses_update.html',
    'status_delete': 'statuses/statuses_delete.html',
}
MESSAGES = {
    'no_delete': 'Невозможно удалить статус, потому что он используется',
    'success_create': 'Статус успешно создан',
    'success_update': 'Статус успешно изменён',
    'success_delete': 'Статус успешно удалён',
}


class ListOfStatuses(Login, Sign, ListView):
    model = Statuses
    template_name = PATHS_TO_TEMPLATES['statuses']
    context_object_name = 'statuses'


class CreateStatus(Login, Sign, Success, CreateView, FormView):

    model = Statuses
    template_name = PATHS_TO_TEMPLATES['status_create']
    form_class = StatusesForm
    success_message = gettext_lazy(MESSAGES['success_create'])
    success_url = reverse_lazy('list_of_statuses')


class UpdateStatus(Login, Sign, Success, UpdateView):

    model = Statuses
    template_name = PATHS_TO_TEMPLATES['status_update']
    form_class = StatusesForm
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy(MESSAGES['success_update'])


class DeleteStatus(Login, Sign, Delete, Success, DeleteView):

    model = Statuses
    template_name = PATHS_TO_TEMPLATES['status_delete']
    error_delete_message = MESSAGES['no_delete']
    success_delete_message = MESSAGES['success_delete']
    redirect_delete_url = 'list_of_statuses'
