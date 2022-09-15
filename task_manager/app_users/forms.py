from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from task_manager.app_users.models import ApplicationUser

MAX_LENGTH_STRING = 100


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=MAX_LENGTH_STRING,
        label=(_('Name')),
        required=True,
    )
    last_name = forms.CharField(
        max_length=MAX_LENGTH_STRING,
        label=(_('Last Name')),
        required=True,
    )

    class Meta:
        model = ApplicationUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]
