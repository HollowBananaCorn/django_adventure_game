import json

from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import timedelta

from rango.forms import UserForm, UserProfileForm
from .signals import achievement_check
from .models import Enemy, Character, UserProfile, Action

def index(request):
    #user_profile = UserProfile.objects.get_or_create(user = request.user)[0]
    #condext_dictionary = {'user_profile' : user_profile}
    return render(request, 'rango/index.html')

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

    # if character payed stranger.
    if character.payed_stranger:
        return redirect("rango:updated_play")

    return render(request, 'rango/play.html', {'player': character}) 

@login_required
def dungeon(request):  # First Dungeon?

    enemy = Enemy.objects.first()
    
    user_profile = get_object_or_404(UserProfile, user=request.user)
    character = get_object_or_404(Character, user=user_profile)
    actions = Action.objects.all()

    return render(request, 'rango/dungeon.html', {'enemy' : enemy, 'player' : character, 'actions' : actions})


def shop(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)
    character, char_created = Character.objects.get_or_create(user=user_profile)

    return render(request, 'rango/shop.html', {'player': character})

def stranger(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    character, char_created = Character.objects.get_or_create(user=user_profile)

    if request.method == "POST":  
        if character.gold >= 500 and not character.payed_stranger:
            character.gold -= 500
            character.payed_stranger = True
            character.save()
            return redirect("rango:boss_area")  # Send player to boss area after paying
        else:
            #reloadit if nothing done instead
            return render(request, "rango/stranger.html", {"player": character, "error": "not enough money"})

    # loadit if normally
    return render(request, "rango/stranger.html", {"player": character})

def stats(request):
 
     return render(request, 'rango/stats.html')

def bossArea(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)
    character, char_created = Character.objects.get_or_create(user=user_profile)

    return render(request, 'rango/boss_area.html', {'player': character})

def bossTalk(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)
    character, char_created = Character.objects.get_or_create(user=user_profile)

    return render(request, 'rango/boss_talk.html', {'player': character})

def boss(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)
    character, char_created = Character.objects.get_or_create(user=user_profile)
    actions = Action.objects.all()

    return render(request, 'rango/boss.html',  {'player': character, 'actions' : actions})

def updatedPlay(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)
    character, char_created = Character.objects.get_or_create(user=user_profile)

    if not character.payed_stranger:
        return redirect("rango:play")

    return render(request, 'rango/updated_play.html', {'player': character})




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
@csrf_exempt
def update_defense(request):
    #should only be when the USER want to update health - 
    #submits data from the client’s web browser to be processed
    if request.method == 'POST': 
        try:
            data = json.loads(request.body)
            new_defense= data.get("new_defense")

            user_profile = UserProfile.objects.get(user=request.user)
            character = Character.objects.get(user=user_profile)

            character.defense = new_defense
            character.save()

            return JsonResponse({"status": "success", "new_defense": character.defense})
        except Exception as e:
            # not in book, but good for debug stuff
            return JsonResponse({"status": "error", "message": str(e)}) 
        
    #displays it like the one from the webb task in the hackathon
    return JsonResponse({"status": "error", "message": "Invalid request"}, )

@login_required
@csrf_exempt
def update_agility(request):
    #should only be when the USER want to update health - 
    #submits data from the client’s web browser to be processed
    if request.method == 'POST': 
        try:
            data = json.loads(request.body)
            new_agility= data.get("new_agility")

            user_profile = UserProfile.objects.get(user=request.user)
            character = Character.objects.get(user=user_profile)

            character.agility = new_agility
            character.save()

            return JsonResponse({"status": "success", "new_agility": character.agility})
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

def update_score(request):
    if request.method == "POST":
        data = json.loads(request.body)

        print(data)

        time = data.get("passed_time", 0)
        
        user_profile = UserProfile.objects.get(user=request.user)
        
        if user_profile.max_score == 0 or time < user_profile.max_score:
            user_profile.max_score = time
            print(time)
            user_profile.save()
        print("saved successfuly")
        #minutes-seconds format
        formatted_time = f"{time // 60:02}:{time % 60:02}"

        return JsonResponse({"success": "success", "formatted_time": formatted_time})
    
    #bad request, client should not access this url.
    return JsonResponse({"success": "error"}, status=400)