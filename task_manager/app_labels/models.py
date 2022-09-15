from django.db import models

from task_manager.app_users.models import ApplicationUser


class Label(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        ApplicationUser,
        on_delete=models.PROTECT,
        null=False,
        related_name='Label_author',
    )

    def __str__(self):
        return self.name
