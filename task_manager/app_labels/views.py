from django.contrib.messages.views import SuccessMessageMixin as Success
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  UpdateView)

from task_manager.app_labels.forms import LabelForm
from task_manager.app_labels.models import Labels
from task_manager.mixins import CheckDeleteMixin as Delete
from task_manager.mixins import CheckSignInMixin as Sign

PATHS_TO_TEMPLATES = {
    'labels': 'labels/labels.html',
    'label_create': 'labels/labels_create.html',
    'label_update': 'labels/labels_update.html',
    'label_delete': 'labels/labels_delete.html',
}
MESSAGES = {
    'success_create': 'Метка успешно создана',
    'success_update': 'Метка успешно изменена',
    'success_delete': 'Метка успешно удалена',
    'no_del': 'Невозможно удалить метку, потому что она используется',
}


class ListOfLabels(Sign, ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class CreateLabel(Success, Sign, CreateView):
    model = Labels
    template_name = 'labels/labels_create.html'
    form_class = LabelForm
    success_message = gettext_lazy('Label created successfully')
    success_url = reverse_lazy('list_of_labels')


class UpdateLabel(Sign, Success, UpdateView, FormView):
    model = Labels
    template_name = 'labels/labels_update.html'
    form_class = LabelForm
    success_message = gettext_lazy('Label changed successfully')
    success_url = reverse_lazy('list_of_labels')


class DeleteLabel(Sign, Delete, Success, DeleteView, FormView):
    model = Labels
    template_name = 'labels/labels_delete.html'
    error_delete_message = "Can't delete label because it's in use"
    success_delete_message = 'Label deleted successfully'
    redirect_delete_url = 'list_of_labels'
