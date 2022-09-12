from django.contrib.messages.views import SuccessMessageMixin as Success
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.app_statuses.forms import StatusesForm
from task_manager.app_statuses.models import Statuses
from task_manager.mixins import CheckDeleteMixin as Delete
from task_manager.mixins import CheckSignInMixin as Sign


class ListOfStatuses(Sign, ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class CreateStatus(Sign, Success, CreateView):

    model = Statuses
    template_name = 'statuses/statuses_create.html'
    form_class = StatusesForm
    success_message = gettext_lazy('Status created successfully')
    success_url = reverse_lazy('list_of_statuses')


class UpdateStatus(Sign, Success, UpdateView):

    model = Statuses
    template_name = 'statuses/statuses_update.html'
    form_class = StatusesForm
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy('Status changed successfully')


class DeleteStatus(Sign, Delete, Success, DeleteView):

    model = Statuses
    template_name = 'statuses/statuses_delete.html'
    error_delete_message = "Can't delete status because it's in use"
    success_delete_message = 'Status deleted successfully'
    redirect_delete_url = 'list_of_statuses'
