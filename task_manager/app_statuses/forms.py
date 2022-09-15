from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.app_statuses.models import Status


class StatusesForm(ModelForm):

    class Meta:
        model = Status
        fields = ['name']
        labels = {'name': _('Name')}
