from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


class CheckSignInMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class CheckDeleteMixin(AccessMixin):
    error_delete_message = ''
    success_delete_message = ''
    redirect_delete_url = ''

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                gettext_lazy(self.error_delete_message),
            )
        else:
            messages.success(
                self.request,
                gettext_lazy(self.success_delete_message),
            )
        return HttpResponseRedirect(reverse_lazy(self.redirect_delete_url))
