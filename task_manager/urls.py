from django.contrib import admin
from django.urls import include, path
from task_manager import views
from task_manager.views import task_manager_detail2
from django.conf.urls.i18n import i18n_patterns


appname = 'task_manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #path('', include('templates.index', namespace='task_manager')),
    #path('', include('task_manager.urls', namespace='task_manager')),
    #path('<slug:slug>', task_manager_detail, name='task_manager_detail'),
    path('2/', views.task_manager_detail2),
    path('i18n/', include('django.conf.urls.i18n')),
]

#urlpatterns += i18n_patterns(
#    path('2/', include('task_manager.urls', #namespace='task_manager')),
#)
