from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rango.forms import UserForm, UserProfileForm

from .models import Enemy, Character, UserProfile

def index(request):
    context_dict = {'boldmessage': 'how to use context dictionary'}

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
        
    else:
        return render(request, 'rango/login.html')

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))



@login_required
def achievements(request):

    return render(request, 'rango/achievements.html')

@login_required
def play(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)

    character, char_created = Character.objects.get_or_create(user=user_profile)

    return render(request, 'rango/play.html', {'player': character}) 

@login_required
def dungeon1(request):  # First Dungeon?

    enemy = Enemy.objects.first()
    
    user_profile = get_object_or_404(UserProfile, user=request.user)
    character = get_object_or_404(Character, user=user_profile)

    return render(request, 'rango/dungeon1.html', {'enemy' : enemy, 'player' : character})

def updated_dungeon1(request):

    return render(request, 'rango/updated_dungeon1.html')

def dungeon2(request):

    return render(request, 'rango/dungeon2.html')

def updated_dungeon2(request):

    return render(request, 'rango/updated_dungeon2.html')

def dungeon3(request):

    return render(request, 'rango/dungeon3.html')

def updated_dungeon3(request):

    return render(request, 'rango/updated_dungeon3.html')

def shop(request):

    return render(request, 'rango/shop.html')

def stranger(request):

    return render(request, 'rango/stranger.html')

def stats(request):
 
     return render(request, 'rango/stats.html')

def bossArea(request):

    return render(request, 'rango/boss_area.html')

def bossTalk(request):

    return render(request, 'rango/boss_talk.html')

def boss(request):

    return render(request, 'rango/boss.html')

def updatedPlay(request):

    return render(request, 'rango/updated_play.html')

def updatedShop(request):

    return render(request, 'rango/updated_shop.html')

def updatedStats(request):

    return render(request, 'rango/updated_stats.html')