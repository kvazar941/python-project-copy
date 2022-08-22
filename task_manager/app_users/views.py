from task_manager.app_users.models import ApplicationUsers
from django.views.generic.list import ListView

class ListOfUsers(ListView):

    model = ApplicationUsers
    template_name = 'users.html'
    context_object_name = 'application_users'
