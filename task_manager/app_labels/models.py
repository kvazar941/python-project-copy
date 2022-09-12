from django.db import models


class Labels(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        """doc."""

        verbose_name = 'Label'
        verbose_name_plural = 'Labels'
