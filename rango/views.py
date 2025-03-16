from django.shortcuts import render, redirect
from django.http import HttpResponse

from rango.forms import UserForm, UserProfileForm

def index(request):
    context_dict = {'boldmessage': 'how to use ontext dictionary'}

    return render(request, 'rango/index.html', context= context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', context=
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


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
