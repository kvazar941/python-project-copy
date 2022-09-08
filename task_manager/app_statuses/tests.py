from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.app_statuses.models import Statuses
from task_manager.app_users.models import ApplicationUsers

CODE_CORRECT_REQUEST = 200
ROUTE_STATUSES = '/statuses/'


class TestStatuses(TestCase):

    fixtures = ['application_users.yaml',
                'tasks.yaml',
                'labels.yaml',
                'statuses.yaml']

    def setUp(self):

        self.user = ApplicationUsers.objects.get(pk=1)
        self.first_status = Statuses.objects.get(pk=1)
        self.second_status = Statuses.objects.get(pk=2)

    def test_list_of_statuses(self):

        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('list_of_statuses'))
        list_of_statuses = list(response.context['statuses'])

        self.assertEqual(response.status_code, CODE_CORRECT_REQUEST)
        self.assertQuerysetEqual(list_of_statuses, [self.first_status,
                                                    self.second_status])

    def test_create_status(self):

        self.client.force_login(self.user)
        status = {'name': 'Отложить'}

        post_data = self.client.post(
            reverse_lazy('create_status'),
            status,
            follow=True,
        )
        сurrent_status = Statuses.objects.get(name=status['name'])

        self.assertRedirects(post_data, ROUTE_STATUSES)
        self.assertEqual(сurrent_status.name, 'Отложить')

    def test_update_status(self):

        self.client.force_login(self.user)
        url = reverse_lazy('update_status', args=(self.first_status.pk,))
        status = {'name': 'В работе'}
        response = self.client.post(url, status, follow=True)

        self.assertEqual(
            Statuses.objects.get(pk=self.first_status.id),
            self.first_status,
        )
        self.assertRedirects(response, ROUTE_STATUSES)

    def test_delete_status(self):

        self.client.force_login(self.user)
        url = reverse_lazy('delete_status', args=(self.second_status.pk,))
        response = self.client.post(url, follow=True)

        with self.assertRaises(Statuses.DoesNotExist):
            Statuses.objects.get(pk=self.second_status.id)

        self.assertRedirects(response, ROUTE_STATUSES)

    def test_delete_status_with_tasks(self):
        self.client.force_login(self.user)
        url = reverse_lazy('delete_status', args=(self.first_status.pk,))
        response = self.client.post(url, follow=True)

        self.assertTrue(
            Statuses.objects.filter(pk=self.first_status.id).exists(),
        )
        self.assertRedirects(response, ROUTE_STATUSES)

    def test_unauthorized(self):

        response = self.client.get(reverse_lazy('list_of_statuses'))

        self.assertRedirects(response, '/login/')
