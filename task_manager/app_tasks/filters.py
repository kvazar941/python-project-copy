from django import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy as _
from django_filters import BooleanFilter, ChoiceFilter, FilterSet

from task_manager.app_labels.models import Label
from task_manager.app_statuses.models import Status
from task_manager.app_tasks.models import Task
from task_manager.app_users.models import ApplicationUser


class TaskFilter(FilterSet):
    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(label=_('Status'), choices=all_statuses)
    all_executors = ApplicationUser.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True).all()
    executor = ChoiceFilter(label=_('Executor'), choices=all_executors)
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    labels = ChoiceFilter(label=_('Label'), choices=all_labels)
    my_tasks = BooleanFilter(
        label=_('Only your task'),
        widget=forms.CheckboxInput(),
        method='filter_self_tasks',
        field_name='my_tasks',
    )

    def filter_self_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
