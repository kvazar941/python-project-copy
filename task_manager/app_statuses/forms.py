from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from task_manager.app_statuses.models import Status


class StatusesForm(ModelForm):

    class Meta:
        model = Status
        fields = ['name']
        labels = {'name': gettext_lazy('Name')}
