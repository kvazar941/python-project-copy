from django.shortcuts import get_object_or_404, render
from .models import my_class


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def task_manager_detail(request, slug):
    instance = get_object_or_404(My_Class, slug=slug)
    context = {
        'instanse': instance,
    }
    return render(request, 'task_manager/templates/index.html', context)
