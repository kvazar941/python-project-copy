from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from task_manager.app_tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')
        labels = {
            'name': gettext_lazy('Name'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status'),
            'executor': gettext_lazy('Executor'),
            'labels': gettext_lazy('Labels'),
        }
