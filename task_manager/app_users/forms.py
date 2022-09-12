from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from task_manager.app_users.models import ApplicationUsers

MAX_LENGTH = 100


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=MAX_LENGTH,
        label=('Name'),
        required=True,
    )
    last_name = forms.CharField(
        max_length=MAX_LENGTH,
        label=('LastName'),
        required=True,
    )

    class Meta:
        model = ApplicationUsers
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]


class SignInForm(AuthenticationForm):
    username = ApplicationUsers.username
    password = ApplicationUsers.password
    fields = ['username', 'password1']
