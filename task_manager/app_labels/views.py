from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, ListView, UpdateView

from task_manager.app_labels.forms import LabelForm
from task_manager.app_labels.models import Labels
from task_manager.mixins import CheckDeleteMixin, CheckSignInMixin


class ListOfLabels(CheckSignInMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class CreateLabel(SuccessMessageMixin, CheckSignInMixin, CreateView):
    model = Labels
    template_name = 'labels/labels_create.html'
    form_class = LabelForm
    success_message = gettext_lazy('Label created successfully')
    success_url = reverse_lazy('list_of_labels')


class UpdateLabel(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    template_name = 'labels/labels_update.html'
    form_class = LabelForm
    success_message = gettext_lazy('Label changed successfully')
    success_url = reverse_lazy('list_of_labels')


class DeleteLabel(CheckSignInMixin, CheckDeleteMixin, SuccessMessageMixin):
    model = Labels
    template_name = 'labels/labels_delete.html'
    error_delete_message = gettext_lazy(
        "Can't delete label because it's in use",
    )
    success_delete_message = gettext_lazy('Label deleted successfully')
    redirect_delete_url = reverse_lazy('list_of_labels')
    success_url = redirect_delete_url
