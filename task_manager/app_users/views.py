from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as Login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin as Success
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from task_manager.app_users.forms import SignInForm, SignUpForm
from task_manager.app_users.models import ApplicationUsers
from task_manager.mixins import CheckDeleteMixin as Delete
from task_manager.mixins import CheckSignInMixin as Sign
from task_manager.mixins import CheckUpdateMixin as Update

PATHS_TO_TEMPLATES = {
    'users': 'users/users.html',
    'user_create': 'users/users_create.html',
    'user_update': 'users/users_update.html',
    'user_delete': 'users/users_delete.html',
    'login': 'login.html',
}
MESSAGES = {
    'success_registration': 'Пользователь успешно зарегистрирован',
    'success_update': 'Пользователь успешно изменён',
    'success_delete': 'Пользователь успешно удалён',
    'success_login': 'Вы залогинены',
    'success_logout': 'Вы разлогинены',
    'no_rules': 'У вас нет прав для изменения другого пользователя.',
    'no_del': 'Невозможно удалить пользователя, потому что он используется',
}
ROUTE_USERS = 'users'


class ListOfUsers(ListView):

    model = ApplicationUsers
    template_name = PATHS_TO_TEMPLATES['users']
    context_object_name = 'application_users'


class SignUp(CreateView, Success, FormView):

    model = ApplicationUsers
    template_name = PATHS_TO_TEMPLATES['user_create']
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = gettext(MESSAGES['success_registration'])


class UpdateUser(Login, Update, Sign, Success, UpdateView, FormView):

    model = ApplicationUsers
    template_name = PATHS_TO_TEMPLATES['user_update']
    form_class = SignUpForm
    success_url = reverse_lazy(ROUTE_USERS)
    success_message = gettext_lazy(MESSAGES['success_update'])
    redirect_error_update = ROUTE_USERS
    error_update_message = MESSAGES['no_rules']


class DeleteUser(Login, Update, Sign, Delete, Success, DeleteView, FormView):

    model = ApplicationUsers
    template_name = PATHS_TO_TEMPLATES['user_delete']
    redirect_error_update = ROUTE_USERS
    error_update_message = MESSAGES['no_rules']
    error_delete_message = MESSAGES['no_del']
    success_delete_message = MESSAGES['success_delete']
    redirect_delete_url = ROUTE_USERS


class SignIn(Success, LoginView):

    model = ApplicationUsers
    template_name = PATHS_TO_TEMPLATES['login']
    form_class = SignInForm
    next_page = reverse_lazy('home')
    success_message = gettext_lazy(MESSAGES['success_login'])


class SignOut(LogoutView, Success):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(
            request,
            messages.SUCCESS,
            gettext(MESSAGES['success_logout']),
        )
        return super().dispatch(request, *args, **kwargs)
