from django.contrib import admin
from django.urls import include, path
from task_manager import views
from task_manager.views import task_manager_detail


appname = 'task_manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #path('', include('templates.index', namespace='task_manager')),
    path('<slug:slug>', task_manager_detail, name='task_manager_detail'),
    path('i18n/', include('django.conf.urls.i18n')),
]

#urlpatterns += i18n_patterns(
#    path('task_manager/', include('task_manager.urls')),
#)
