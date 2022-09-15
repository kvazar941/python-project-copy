from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


class CheckUpdateMixin(AccessMixin):
    redirect_error_update = ''
    error_update_message = ''

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object():
            messages.warning(
                self.request,
                gettext_lazy(self.error_update_message),
            )
            return redirect(reverse_lazy(self.redirect_error_update))
        return super().dispatch(request, *args, **kwargs)
