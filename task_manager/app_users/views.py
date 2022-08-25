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

MESSAGE_NO_RULES = 'У вас нет прав для изменения другого пользователя.'
MESSAGE_NO_DEL = 'Невозможно удалить пользователя, потому что он используется'
ROUTE_USERS = 'users'


class ListOfUsers(ListView):

    model = ApplicationUsers
    template_name = 'users.html'
    context_object_name = 'application_users'


class SignUp(CreateView, Success, FormView):

    model = ApplicationUsers
    template_name = 'users_create.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = gettext('Пользователь успешно зарегистрирован')


class UpdateUser(Login, Update, Sign, Success, UpdateView, FormView):

    model = ApplicationUsers
    template_name = 'users_update.html'
    form_class = SignUpForm
    success_url = reverse_lazy(ROUTE_USERS)
    success_message = gettext_lazy('Пользователь успешно изменён')
    redirect_error_update = ROUTE_USERS
    error_update_message = MESSAGE_NO_RULES


class DeleteUser(Login, Update, Sign, Delete, Success, DeleteView, FormView):

    model = ApplicationUsers
    template_name = 'users_delete.html'
    redirect_error_update = ROUTE_USERS
    error_update_message = MESSAGE_NO_RULES
    error_delete_message = MESSAGE_NO_DEL
    success_delete_message = 'Пользователь успешно удалён'
    redirect_delete_url = ROUTE_USERS


class SignIn(Success, LoginView):

    model = ApplicationUsers
    template_name = 'login.html'
    form_class = SignInForm
    next_page = reverse_lazy('home')
    success_message = gettext_lazy('Вы залогинены')


class SignOut(LogoutView, Success):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(
            request,
            messages.SUCCESS,
            gettext('Вы разлогинены'),
        )
        return super().dispatch(request, *args, **kwargs)
