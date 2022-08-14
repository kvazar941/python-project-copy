from django.shortcuts import get_object_or_404, render
from .models import my_class


def home(request):
    return render(request, 'home.html', context={
        'who': 'World',
    })


def users(request):
    #instance = get_object_or_404(my_class, slug='2')
    context = {
        'who': 'users',
    }
    return render(request, 'users.html', context)


def users_create(request):
    if request.method == 'GET':
        context = {
            'who': request.method,
        }
        return render(request, 'users_create.html', context)
    elif request.method == 'POST':
        context = {
            'who': request.method,
        }
        return render(request, 'users_create.html', context)


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
