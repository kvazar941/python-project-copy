# Generated by Django 4.1 on 2022-09-16 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_statuses', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_labels', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_author', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_executor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_labels.label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='task_label', through='app_tasks.TaskLabel', to='app_labels.label'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_status', to='app_statuses.status'),
        ),
    ]
