from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from task_manager import views
from task_manager.views import users, users_update, users_delete, login, logout, NewView
from django.conf.urls.i18n import i18n_patterns
from .views import EmployeeCreate


appname = 'task_manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('task_manager.app_users.urls'), name='users'),
    #path('users/create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    #path('users/<int:pk>/update/', views.users_update),
    #path('users/<int:pk>/delete/', views.users_delete),
    #path('login/', views.login),
    #path('logout/', views.logout),
    path('i18n/', include('django.conf.urls.i18n')),
]

#urlpatterns += i18n_patterns(
#    path('2/', include('task_manager.urls', #namespace='task_manager')),
#)
