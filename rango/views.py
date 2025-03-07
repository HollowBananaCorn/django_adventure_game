from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'how to use ontext dictionary'}

    return render(request, 'rango/index.html', context= context_dict)

def achievements(request):

    return render(request, 'rango/achievements.html')

def play(request):

    return render(request, 'rango/play.html')
