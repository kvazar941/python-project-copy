from task_manager.app_users.models import ApplicationUsers
from task_manager.mixins import (CheckSignInMixin,
                                 CheckDeleteMixin,
                                 CheckUpdateMixin)

from django.contrib.messages.views import SuccessMessageMixin

from task_manager.app_users.forms import SignInForm, SignUpForm

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy, gettext

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView,
                                       FormView)

NO_RULES = 'У вас нет прав для изменения другого пользователя.'

class ListOfUsers(ListView):

    model = ApplicationUsers
    template_name = 'users.html'
    context_object_name = 'application_users'


class SignUp(CreateView, SuccessMessageMixin, FormView):

    model = ApplicationUsers
    template_name = 'users_create.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = gettext('Пользователь успешно зарегистрирован')


class UpdateUser(LoginRequiredMixin, CheckUpdateMixin,
                 CheckSignInMixin, SuccessMessageMixin,
                 UpdateView, FormView):

    model = ApplicationUsers
    template_name = 'users_update.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users')
    success_message = gettext_lazy('Пользователь успешно изменён')
    redirect_error_update = 'users'
    error_update_message = NO_RULES


class DeleteUser(LoginRequiredMixin, CheckUpdateMixin, CheckSignInMixin,
                 CheckDeleteMixin, SuccessMessageMixin,
                 DeleteView, FormView):

    model = ApplicationUsers
    template_name = 'users_delete.html'
    redirect_error_update = 'users'
    error_update_message = NO_RULES
    error_delete_message = 'Невозможно удалить пользователя,\
                            потому что он используется'
    success_delete_message = 'Пользователь успешно удалён'
    redirect_delete_url = 'users'


class SignIn(SuccessMessageMixin, LoginView):

    model = ApplicationUsers
    template_name = 'login.html'
    form_class = SignInForm
    next_page = reverse_lazy('home')
    success_message = gettext_lazy('Вы залогинены')


class SignOut(LogoutView, SuccessMessageMixin):

    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS,
                             gettext('Вы разлогинены'))
        return super().dispatch(request, *args, **kwargs)
