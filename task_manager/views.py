from django.shortcuts import get_object_or_404, render
from .models import my_class


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def task_manager_detail(request, slug):
    instance = get_object_or_404(my_class, slug=slug)
    context = {
        'instanse': instance,
    }
    return render(request, 'task_manager/templates/task_manager_detail.html', context)


def task_manager_detail2(request):
    #instance = get_object_or_404(my_class, slug='2')
    context = {
        'who': 'task manager',
    }
    return render(request, 'task_manager_detail.html', context)
