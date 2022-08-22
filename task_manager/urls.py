from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from task_manager import views
from task_manager.views import users, users_update, users_delete, login, logout, NewView
from django.conf.urls.i18n import i18n_patterns
from .views import EmployeeCreate
from task_manager.app_users.views import SignIn, SignOut


appname = 'task_manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', SignIn.as_view(), name='login'),
    path('logout/', SignOut.as_view(), name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('users/', include('task_manager.app_users.urls'), name='users'),
    path('statuses/', include('task_manager.app_statuses.urls'), name='statuses'),
    path('tasks/', include('task_manager.app_tasks.urls'), name='tasks'),
    path('labels/', include('task_manager.app_labels.urls'), name='labels'),
]

#urlpatterns += i18n_patterns(
#    path('2/', include('task_manager.urls', #namespace='task_manager')),
#)
