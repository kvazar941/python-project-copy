from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from task_manager.app_labels.models import Labels


class LabelForm(ModelForm):

    class Meta:
        model = Labels
        fields = ('name', )
        labels = {'name': gettext_lazy('Name')}
