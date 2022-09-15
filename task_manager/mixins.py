from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import DeleteView

from task_manager.app_tasks.models import Task


class CheckSignInMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class CheckDeleteMixin(AccessMixin, DeleteView):
    error_delete_message = ''
    success_delete_message = ''
    redirect_delete_url = ''
    success_url = ''

    def form_valid(self, request, *args, **kwargs):
        if Task.objects.filter(status=self.get_object().pk):
            messages.error(
                self.request,
                gettext_lazy(self.error_delete_message),
            )
            return HttpResponseRedirect(self.redirect_delete_url)
        messages.success(
            self.request,
            gettext_lazy(self.success_delete_message),
        )
        return super().delete(request, *args, **kwargs)
