from django.db import models

from task_manager.app_labels.models import Labels
from task_manager.app_statuses.models import Statuses
from task_manager.app_users.models import ApplicationUsers

MAX_LENGHT_STRING = 150


class Tasks(models.Model):

    name = models.CharField(max_length=MAX_LENGHT_STRING)
    description = models.TextField(blank=True)

    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        null=True,
        related_name='task_status',
    )
    author = models.ForeignKey(
        ApplicationUsers,
        on_delete=models.PROTECT,
        null=False,
        related_name='task_author',
    )
    executor = models.ForeignKey(
        ApplicationUsers,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='task_executor',
    )
    labels = models.ManyToManyField(
        Labels,
        related_name='task_label',
        blank=True,
        through='TaskLabels',
        through_fields=('task', 'label'),
    )

    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)


class TaskLabels(models.Model):

    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)
