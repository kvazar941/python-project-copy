from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from task_manager.app_users.forms import SignInForm, SignUpForm
from task_manager.app_users.mixins_user import CheckUpdateMixin
from task_manager.app_users.models import ApplicationUsers
from task_manager.mixins import CheckDeleteMixin, CheckSignInMixin

ROUTE_USERS = 'users'


class ListOfUsers(ListView):

    model = ApplicationUsers
    template_name = 'users/users.html'
    context_object_name = 'application_users'


class SignUp(CreateView, SuccessMessageMixin):

    model = ApplicationUsers
    template_name = 'users/users_create.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = gettext('User successfully registered')


class UpdateUser(CheckUpdateMixin,
                 CheckSignInMixin,
                 SuccessMessageMixin,
                 UpdateView):

    model = ApplicationUsers
    template_name = 'users/users_update.html'
    form_class = SignUpForm
    success_url = reverse_lazy(ROUTE_USERS)
    success_message = gettext_lazy('User changed successfully')
    redirect_error_update = ROUTE_USERS
    error_update_message = 'You do not have permission to change another user'


class DeleteUser(CheckUpdateMixin,
                 CheckSignInMixin,
                 CheckDeleteMixin,
                 SuccessMessageMixin,
                 DeleteView):

    model = ApplicationUsers
    template_name = 'users/users_delete.html'
    redirect_error_update = ROUTE_USERS
    error_update_message = 'You do not have permission to change another user'
    error_delete_message = 'Cannot delete user because it is in use'
    success_delete_message = 'User deleted successfully'
    redirect_delete_url = ROUTE_USERS


class SignIn(SuccessMessageMixin, LoginView):

    model = ApplicationUsers
    template_name = 'login.html'
    form_class = SignInForm
    next_page = reverse_lazy('home')
    success_message = gettext_lazy('You are logged in')


class SignOut(LogoutView, SuccessMessageMixin):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(
            request,
            messages.SUCCESS,
            gettext('You are logged out'),
        )
        return super().dispatch(request, *args, **kwargs)
