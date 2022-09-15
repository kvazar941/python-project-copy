from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from task_manager.app_tasks.models import Task
from task_manager.app_users.forms import SignUpForm
from task_manager.app_users.mixins_user import CheckUpdateMixin
from task_manager.app_users.models import ApplicationUser
from task_manager.mixins import CheckSignInMixin

ROUTE_USERS = 'users'


class ListOfUsers(ListView):

    model = ApplicationUser
    template_name = 'users/users.html'
    context_object_name = 'application_users'


class SignUp(CreateView, SuccessMessageMixin, FormView):

    model = ApplicationUser
    template_name = 'users/users_create.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = gettext('User successfully registered')


class UpdateUser(CheckUpdateMixin,
                 CheckSignInMixin,
                 SuccessMessageMixin,
                 UpdateView):

    model = ApplicationUser
    template_name = 'users/users_update.html'
    form_class = SignUpForm
    success_url = reverse_lazy(ROUTE_USERS)
    success_message = gettext_lazy('User changed successfully')
    redirect_error_update = ROUTE_USERS
    error_update_message = gettext_lazy(
        'You do not have permission to change another user',
    )


class DeleteUser(CheckUpdateMixin,
                 CheckSignInMixin,
                 SuccessMessageMixin,
                 DeleteView):

    model = ApplicationUser
    template_name = 'users/users_delete.html'
    redirect_error_update = ROUTE_USERS
    success_url = reverse_lazy(ROUTE_USERS)
    error_update_message = gettext_lazy(
        'You do not have permission to delete another user',
    )
    error_delete_message = gettext_lazy(
        'Cannot delete user because it is in use',
    )
    success_delete_message = gettext_lazy(
        'User deleted successfully',
    )
    redirect_delete_url = reverse_lazy(ROUTE_USERS)

    def form_valid(self, request, *args, **kwargs):
        author = Task.objects.filter(author=self.request.user.pk)
        executor = Task.objects.filter(executor=self.request.user.pk)
        if author or executor:
            messages.warning(
                self.request,
                gettext_lazy(self.error_delete_message),
            )
            return HttpResponseRedirect(self.redirect_delete_url)
        messages.success(
            self.request,
            gettext_lazy(self.success_delete_message),
        )
        return super().delete(request, *args, **kwargs)


class SignIn(SuccessMessageMixin, LoginView):

    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    success_message = gettext_lazy('You are logged in')

    def get_success_url(self):
        return self.success_url


class SignOut(SuccessMessageMixin, LogoutView):

    next_page = reverse_lazy('home')
    success_message = gettext_lazy('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, self.success_message)
        return super().dispatch(request, *args, **kwargs)
