from django.contrib import admin
from django.urls import include, path
from task_manager import views
from task_manager.views import users, users_create, users_update, users_delete, login, logout
from django.conf.urls.i18n import i18n_patterns


appname = 'task_manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('users/', views.users),
    path('users/create/', views.users_create),
    path('users/<int:pk>/update/', views.users_update),
    path('users/<int:pk>/delete/', views.users_delete),
    path('login/', views.login),
    path('logout/', views.logout),
    path('i18n/', include('django.conf.urls.i18n')),
]

#urlpatterns += i18n_patterns(
#    path('2/', include('task_manager.urls', #namespace='task_manager')),
#)
