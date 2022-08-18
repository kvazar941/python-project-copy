from django.shortcuts import get_object_or_404, render
from .models import Employee
from django.http import HttpResponse
from django.views import View
from .form import EmployeeForm
from django .views.generic.edit import CreateView


def home(request):
    return render(request, 'home.html', context={
        'who': 'World',
    })


def users(request):
    context = {
        'who': 'users',
    }
    return render(request, 'users.html', context)


class NewView(View):
    def get(self, request):
        context = {
            'who': request.method,
        }
        response = render(request, 'users_create.html', context)
        return HttpResponse(response)

class EmployeeCreate(CreateView):
    model = Employee
    
    fields = '__all__'


def users_update(request):
    if request.method == 'GET':
        context = {
            'who': request.method,
        }
        return render(request, 'users_update.html', context)
    elif request.method == 'POST':
        context = {
            'who': request.method,
        }
        return render(request, 'users_update.html', context)


def users_delete(request):
    if request.method == 'GET':
        context = {
            'who': request.method,
        }
        return render(request, 'users_delete.html', context)
    elif request.method == 'POST':
        context = {
            'who': request.method,
        }
        return render(request, 'users_delete.html', context)


def login(request):
    if request.method == 'GET':
        context = {
            'who': request.method,
        }
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        context = {
            'who': request.method,
        }
        return render(request, 'login.html', context)


def logout(request):
    if request.method == 'POST':
        context = {
            'who': request.method,
        }
        return render(request, 'logout.html', context)
