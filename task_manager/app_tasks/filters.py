import django_filters
from django import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy

from task_manager.app_labels.models import Labels
from task_manager.app_statuses.models import Statuses
from task_manager.app_tasks.models import Tasks
from task_manager.app_users.models import ApplicationUsers


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Statuses.objects.values_list(
            'id', 'name', named=True
        ).all(),
        label=gettext_lazy('Status'),
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=ApplicationUsers.objects.values_list(
            'id',
            Concat('first_name', Value(' '), 'last_name'),
            named=True
        ).all(),
        label=gettext_lazy('Executor'),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Labels.objects.values_list('id', 'name', named=True).all(),
        label=gettext_lazy('Label'),
    )
    my_tasks = django_filters.BooleanFilter(
        label=gettext_lazy('Only your task'),
        widget=forms.CheckboxInput(),
        method='filter_self_tasks',
        field_name='my_tasks',
    )

    def filter_self_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels']
