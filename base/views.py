from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Home page')


def room(request):
    return HttpResponse('Room')
