from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, ListView, UpdateView

from task_manager.app_statuses.forms import StatusesForm
from task_manager.app_statuses.models import Status
from task_manager.mixins import CheckDeleteMixin, CheckSignInMixin


class ListOfStatuses(CheckSignInMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class CreateStatus(CheckSignInMixin, SuccessMessageMixin, CreateView):

    model = Status
    template_name = 'statuses/statuses_create.html'
    form_class = StatusesForm
    success_message = gettext_lazy('Status created successfully')
    success_url = reverse_lazy('list_of_statuses')


class UpdateStatus(CheckSignInMixin, SuccessMessageMixin, UpdateView):

    model = Status
    template_name = 'statuses/statuses_update.html'
    form_class = StatusesForm
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy('Status changed successfully')


class DeleteStatus(CheckSignInMixin, CheckDeleteMixin, SuccessMessageMixin):

    model = Status
    template_name = 'statuses/statuses_delete.html'
    error_delete_message = gettext_lazy(
        "Can't delete status because it's in use",
    )
    success_delete_message = gettext_lazy(
        'Status deleted successfully',
    )
    redirect_delete_url = reverse_lazy('list_of_statuses')
    success_url = redirect_delete_url
