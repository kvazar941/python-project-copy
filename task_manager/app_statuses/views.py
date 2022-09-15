from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.app_statuses.forms import StatusesForm
from task_manager.app_statuses.models import Status
from task_manager.app_tasks.models import Task
from task_manager.app_users.models import ApplicationUser
from task_manager.mixins import CheckSignInMixin

STATUS_PAGE = 'list_of_statuses'


class ListOfStatuses(CheckSignInMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class CreateStatus(CheckSignInMixin, SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'statuses/statuses_create.html'
    form_class = StatusesForm
    success_message = _('Status created successfully')
    success_url = reverse_lazy(STATUS_PAGE)

    def form_valid(self, form):
        author = ApplicationUser.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateStatus(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'statuses/statuses_update.html'
    form_class = StatusesForm
    success_url = reverse_lazy(STATUS_PAGE)
    success_message = _('Status changed successfully')
    no_author_message = _("Only it's author can update a status")
    redirect_update_url = reverse_lazy(STATUS_PAGE)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().author:
            messages.warning(self.request, self.no_author_message)
            return HttpResponseRedirect(self.redirect_update_url)
        messages.success(self.request, self.success_message)
        return super().dispatch(request, *args, **kwargs)


class DeleteStatus(CheckSignInMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/statuses_delete.html'
    error_delete_message = _("Can't delete status because it's in use")
    success_delete_message = _('Status deleted successfully')
    redirect_delete_url = reverse_lazy(STATUS_PAGE)
    success_url = reverse_lazy(STATUS_PAGE)
    no_author_message = _("Only it's author can delete a status")

    def form_valid(self, request, *args, **kwargs):
        if Task.objects.filter(status=self.get_object().pk):
            messages.warning(self.request, _(self.error_delete_message))
            return HttpResponseRedirect(self.redirect_delete_url)
        if self.request.user != self.get_object().author:
            messages.warning(self.request, self.no_author_message)
            return HttpResponseRedirect(self.redirect_delete_url)
        messages.success(self.request, _(self.success_delete_message))
        return super().delete(request, *args, **kwargs)
