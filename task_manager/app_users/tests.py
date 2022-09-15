from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.app_users.models import ApplicationUser

CODE_REDIRECT = 302
CODE_CORRECT_REQUEST = 200


class TestApplicationUser(TestCase):

    fixtures = ['application_users.yaml',
                'tasks.yaml',
                'labels.yaml',
                'statuses.yaml']

    def setUp(self):
        self.first_user = ApplicationUser.objects.get(pk=1)
        self.second_user = ApplicationUser.objects.get(pk=2)
        self.client: Client = Client()

    def test_sign_up(self):
        url = reverse_lazy('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, CODE_CORRECT_REQUEST)

        new_user = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'password1': 'Test123!#',
            'password2': 'Test123!#',
        }

        response = self.client.post(url, new_user, follow=True)
        self.assertRedirects(response, '/login/')

    def test_update(self):
        user = self.first_user
        self.client.force_login(user)
        url = reverse_lazy('update_user', args=(user.id, ))

        change_user = {
            'first_name': 'Vladimir',
            'last_name': user.last_name,
            'username': user.username,
            'password1': 'Test321!#',
            'password2': 'Test321!#',
        }

        response = self.client.post(url, change_user, follow=True)
        changed_user = ApplicationUser.objects.get(username=user.username)

        self.assertRedirects(response, '/users/')
        self.assertTrue(changed_user.check_password('Test321!#'))

    def test_delete_user(self):
        user = self.second_user
        self.client.force_login(user)
        url = reverse_lazy('delete_user', args=(user.id,))
        response = self.client.post(url, follow=True)

        with self.assertRaises(ApplicationUser.DoesNotExist):
            ApplicationUser.objects.get(pk=user.id)

        self.assertRedirects(response, '/users/')

    def test_sign_in(self):
        url = reverse_lazy('login')
        correct_data = {'username': 'yeltsin',
                        'password1': 'FakePass654!#'}
        response = self.client.post(url, correct_data, follow=True)

        self.assertEqual(response.status_code, CODE_CORRECT_REQUEST)

    def test_sign_out(self):
        url = reverse_lazy('logout')
        response = self.client.post(url)

        self.assertEqual(response.status_code, CODE_REDIRECT)
        self.assertRedirects(response, '/')

    def test_delete_user_with_tasks(self):
        user = self.first_user
        self.client.force_login(user)
        url = reverse_lazy('delete_user', args=(user.pk,))
        response = self.client.post(url, follow=True)

        self.assertTrue(
            ApplicationUser.objects.filter(pk=self.first_user.id).exists(),
        )
        self.assertRedirects(response, '/users/')
