from django.contrib.auth.mixins import LoginRequiredMixin as Login
from django.contrib.messages.views import SuccessMessageMixin as Success
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  UpdateView)

from task_manager.app_labels.forms import LabelForm
from task_manager.app_labels.models import Labels
from task_manager.mixins import CheckDeleteMixin as Delete
from task_manager.mixins import CheckSignInMixin as SignIn

ERROR_MESSAGE_DEL = 'Невозможно удалить метку, потому что она используется'


class ListOfLabels(Login, SignIn, ListView):
    model = Labels
    template_name = 'labels.html'
    context_object_name = 'labels'


class CreateLabel(Success, SignIn, CreateView):
    model = Labels
    template_name = 'labels_create.html'
    form_class = LabelForm
    success_message = gettext_lazy('Метка успешно создана')
    success_url = reverse_lazy('list_of_labels')


class UpdateLabel(Login, SignIn, Success, UpdateView, FormView):
    model = Labels
    template_name = 'labels_update.html'
    form_class = LabelForm
    success_message = gettext_lazy('Метка успешно изменена')
    success_url = reverse_lazy('list_of_labels')


class DeleteLabel(Login, SignIn, Delete, Success, DeleteView, FormView):
    model = Labels
    template_name = 'labels_delete.html'
    error_delete_message = ERROR_MESSAGE_DEL
    success_delete_message = 'Метка успешно удалена'
    redirect_delete_url = 'list_of_labels'
