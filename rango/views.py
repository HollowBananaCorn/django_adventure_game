import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
def dungeon(request):  # First Dungeon?

    enemy = Enemy.objects.first()
    
    user_profile = get_object_or_404(UserProfile, user=request.user)
    character = get_object_or_404(Character, user=user_profile)

    return render(request, 'rango/dungeon.html', {'enemy' : enemy, 'player' : character})

def updated_dungeon(request):

    return render(request, 'rango/updated_dungeon.html')


def shop(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)

    character, char_created = Character.objects.get_or_create(user=user_profile)

    return render(request, 'rango/shop.html', {'player': character})

def stranger(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)

    character, char_created = Character.objects.get_or_create(user=user_profile)

    return render(request, 'rango/stranger.html', {'player': character})

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





#not Pages, view required to communicate with Server
@login_required
@csrf_exempt
def update_health(request):
    #should only be when the USER want to update health - 
    #submits data from the client’s web browser to be processed
    if request.method == 'POST': 
        try:
            data = json.loads(request.body)
            new_health = data.get("new_health")

            user_profile = UserProfile.objects.get(user=request.user)
            character = Character.objects.get(user=user_profile)

            character.current_health = new_health
            character.save()

            return JsonResponse({"status": "success", "new_health": character.current_health})
        except Exception as e:
            # not in book, but good for debug stuff
            return JsonResponse({"status": "error", "message": str(e)}) 
        
    #displays it like the one from the webb task in the hackathon
    return JsonResponse({"status": "error", "message": "Invalid request"}, )

@login_required
@csrf_exempt
def update_gold(request):
    #should only be when the USER want to update health - 
    #submits data from the client’s web browser to be processed
    if request.method == 'POST': 
        try:
            data = json.loads(request.body)
            new_gold = data.get("new_gold")

            user_profile = UserProfile.objects.get(user=request.user)
            character = Character.objects.get(user=user_profile)

            character.gold = new_gold
            character.save()

            return JsonResponse({"status": "success", "new_gold": character.gold})
        except Exception as e:
            # not in book, but good for debug stuff
            return JsonResponse({"status": "error", "message": str(e)}) 
        
    #displays it like the one from the webb task in the hackathon
    return JsonResponse({"status": "error", "message": "Invalid request"}, )

@login_required
@csrf_exempt
def update_attack(request):
    #should only be when the USER want to update health - 
    #submits data from the client’s web browser to be processed
    if request.method == 'POST': 
        try:
            data = json.loads(request.body)
            new_attack= data.get("new_attack")

            user_profile = UserProfile.objects.get(user=request.user)
            character = Character.objects.get(user=user_profile)

            character.attack = new_attack
            character.save()

            return JsonResponse({"status": "success", "new_attack": character.attack})
        except Exception as e:
            # not in book, but good for debug stuff
            return JsonResponse({"status": "error", "message": str(e)}) 
        
    #displays it like the one from the webb task in the hackathon
    return JsonResponse({"status": "error", "message": "Invalid request"}, )


@login_required
def delete_character(request):
    
    try:
        character = Character.objects.get(user=request.user.userprofile)
        character.delete()
    except Character.DoesNotExist:
        pass

    return redirect('index')