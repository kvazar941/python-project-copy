from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.app_labels.forms import LabelForm
from task_manager.app_labels.models import Label
from task_manager.app_tasks.models import Task
from task_manager.app_users.models import ApplicationUser
from task_manager.mixins import CheckSignInMixin

LABELS_PAGE = 'list_of_labels'


class ListOfLabels(CheckSignInMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class CreateLabel(SuccessMessageMixin, CheckSignInMixin, CreateView):
    model = Label
    template_name = 'labels/labels_create.html'
    form_class = LabelForm
    success_message = _('Label created successfully')
    success_url = reverse_lazy(LABELS_PAGE)

    def form_valid(self, form):
        author = ApplicationUser.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateLabel(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'labels/labels_update.html'
    form_class = LabelForm
    success_message = _('Label changed successfully')
    success_url = reverse_lazy(LABELS_PAGE)
    no_author_message = _("Only it's author can update a label")
    redirect_update_url = reverse_lazy(LABELS_PAGE)

    def form_valid(self, request, *args, **kwargs):
        if self.request.user != self.get_object().author:
            messages.warning(self.request, self.no_author_message)
            return HttpResponseRedirect(self.redirect_update_url)
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.redirect_update_url)


class DeleteLabel(CheckSignInMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/labels_delete.html'
    error_delete_message = _("Can't delete label because it's in use")
    success_delete_message = _('Label deleted successfully')
    redirect_delete_url = reverse_lazy(LABELS_PAGE)
    success_url = reverse_lazy(LABELS_PAGE)
    no_author_message = _("Only it's author can delete a label")

    def form_valid(self, request, *args, **kwargs):
        if Task.objects.filter(status=self.get_object().pk):
            messages.warning(self.request, _(self.error_delete_message))
            return HttpResponseRedirect(self.redirect_delete_url)
        if self.request.user != self.get_object().author:
            messages.warning(self.request, self.no_author_message)
            return HttpResponseRedirect(self.redirect_delete_url)
        messages.success(self.request, _(self.success_delete_message))
        return super().delete(request, *args, **kwargs)
