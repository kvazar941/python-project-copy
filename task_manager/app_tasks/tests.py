from django.test import TestCase
from django.urls import reverse_lazy
from django_filters import FilterSet

from task_manager.app_statuses.models import Status
from task_manager.app_tasks.models import Task
from task_manager.app_users.models import ApplicationUser

CODE_CORRECT_REQUEST = 200
ROUTE_TASKS = '/tasks/'
STATUS = 'status'
EXECUTOR = 'executor'
LABELS = 'labels'
NAME = 'name'


class TestTask(TestCase):

    fixtures = ['application_users.yaml',
                'tasks.yaml',
                'labels.yaml',
                'statuses.yaml']

    def setUp(self) -> None:
        self.first_user = ApplicationUser.objects.get(pk=1)
        self.second_user = ApplicationUser.objects.get(pk=2)
        self.first_status = Status.objects.get(pk=1)
        self.second_status = Status.objects.get(pk=2)
        self.first_task = Task.objects.get(pk=1)
        self.second_task = Task.objects.get(pk=2)

    def test_list_of_tasks(self):
        self.client.force_login(self.first_user)
        response = self.client.get(reverse_lazy('list_of_tasks'))
        tasks_list = list(response.context['list_of_tasks'])

        self.assertEqual(response.status_code, CODE_CORRECT_REQUEST)
        self.assertQuerysetEqual(tasks_list, [self.first_task,
                                              self.second_task])

    def test_create_tasks(self):
        self.client.force_login(self.first_user)
        task = {'name': 'Написать тесты',
                'description': 'Тесты к tasks',
                'author': 1,
                'executor': 2,
                'status': 1}

        response = self.client.post(
            reverse_lazy('create_task'),
            task,
            follow=True,
        )
        created_task = Task.objects.get(name=task[NAME])

        self.assertRedirects(response, ROUTE_TASKS)
        self.assertEqual(created_task.name, 'Написать тесты')

    def test_update_task(self):
        self.client.force_login(self.first_user)
        url = reverse_lazy('update_task', args=(self.first_task.pk,))
        task = {
            'name': 'Обновлённая задача',
            'description': 'Обновлённое описание',
            'author': 2,
            'executor': 1,
            'status': 2,
        }

        response = self.client.post(url, task, follow=True)
        created_task = Task.objects.get(name=task[NAME])

        self.assertRedirects(response, ROUTE_TASKS)
        self.assertEqual(created_task.name, 'Обновлённая задача')

    def test_delete_task(self):
        self.client.force_login(self.first_user)
        url = reverse_lazy('delete_task', args=(self.first_task.id,))
        response = self.client.post(url, follow=True)

        self.assertRedirects(response, ROUTE_TASKS)

    def test_delete_task_by_non_author(self):
        self.client.force_login(self.second_user)
        url = reverse_lazy('delete_task', args=(self.first_task.pk,))
        response = self.client.post(url, follow=True)

        self.assertTrue(Task.objects.filter(pk=self.first_task.pk).exists())
        self.assertRedirects(response, ROUTE_TASKS)

    def test_filter_status(self):

        status = Task._meta.get_field(STATUS)
        result = FilterSet.filter_for_field(status, STATUS)

        self.assertEqual(result.field_name, STATUS)

    def test_filter_executor(self):

        status = Task._meta.get_field(EXECUTOR)
        result = FilterSet.filter_for_field(status, EXECUTOR)

        self.assertEqual(result.field_name, EXECUTOR)

    def test_filter_label(self):

        status = Task._meta.get_field(LABELS)
        result = FilterSet.filter_for_field(status, LABELS)

        self.assertEqual(result.field_name, LABELS)
