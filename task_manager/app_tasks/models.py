from django.db import models

from task_manager.app_labels.models import Label
from task_manager.app_statuses.models import Status
from task_manager.app_users.models import ApplicationUser

MAX_LENGHT_STRING = 150


class Task(models.Model):

    name = models.CharField(max_length=MAX_LENGHT_STRING)
    description = models.TextField(blank=True)

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        related_name='task_status',
    )
    author = models.ForeignKey(
        ApplicationUser,
        on_delete=models.PROTECT,
        null=False,
        related_name='task_author',
    )
    executor = models.ForeignKey(
        ApplicationUser,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='task_executor',
    )
    labels = models.ManyToManyField(
        Label,
        related_name='task_label',
        blank=True,
        through='TaskLabel',
        through_fields=('task', 'label'),
    )

    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)


class TaskLabel(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
