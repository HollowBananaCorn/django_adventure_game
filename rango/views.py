from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'how to use ontext dictionary'}

    return render(request, 'rango/index.html', context= context_dict)

def achievements(request):

    return render(request, 'rango/achievements.html')

def play(request):

    return render(request, 'rango/play.html')

def dungeon(request):

    return render(request, 'rango/dungeon.html')

def shop(request):

    return render(request, 'rango/shop.html')

def stranger(request):

    return render(request, 'rango/stranger.html')

def stats(request):
 
     return render(request, 'rango/stats.html')
