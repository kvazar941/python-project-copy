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

MESSAGE_NO_DEL = 'Невозможно удалить статус, потому что он используется'


class ListOfStatuses(Login, Sign, ListView):
    model = Statuses
    template_name = 'statuses.html'
    context_object_name = 'statuses'


class CreateStatus(Login, Sign, Success, CreateView, FormView):

    model = Statuses
    template_name = 'statuses_create.html'
    form_class = StatusesForm
    success_message = gettext_lazy('Статус успешно создан')
    success_url = reverse_lazy('list_of_statuses')


class UpdateStatus(Login, Sign, Success, UpdateView):

    model = Statuses
    template_name = 'statuses_update.html'
    form_class = StatusesForm
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy('Статус успешно изменён')


class DeleteStatus(Login, Sign, Delete, Success, DeleteView):

    model = Statuses
    template_name = 'statuses_delete.html'
    error_delete_message = MESSAGE_NO_DEL
    success_delete_message = 'Статус успешно удалён'
    redirect_delete_url = 'list_of_statuses'
