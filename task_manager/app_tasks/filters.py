import django_filters
from django import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy

from task_manager.app_labels.models import Label
from task_manager.app_statuses.models import Status
from task_manager.app_tasks.models import Task
from task_manager.app_users.models import ApplicationUser


class TaskFilter(django_filters.FilterSet):
    statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = django_filters.ChoiceFilter(
        label=gettext_lazy('Status'),
        choices=statuses,
    )
    executors = ApplicationUser.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True).all()

    executor = django_filters.ChoiceFilter(
        label=gettext_lazy('Executor'),
        choices=executors,
    )

    all_labels = Label.objects.values_list('id', 'name', named=True).all()

    labels = django_filters.ChoiceFilter(
        label=gettext_lazy('Label'),
        choices=all_labels,
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
        model = Task
        fields = ['status', 'executor', 'labels']
