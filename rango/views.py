from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserProfile, Enemy, Attack, Action, Achievement

import random

@login_required
def index(request):
    #this should be the main page/home page before the start of the game showing player specific content
    
    if request.user.is_authenticated:
        player = get_object_or_404(UserProfile, user=request.user)
        achievements = Achievement.objects.filter(player = player)#not sure of this is needed but adding it for now
        leaderboard_entries = Leaderboard.objects.order_by("time taken")[:10]
        context = {
            "player": player,
            "achievements": achievements,
            "leaderboard_entries": leaderboard_entries
        }
    else:
        context = {} #for now keeping it like this will force the user to log in, as they cant see anything before logging in

    return render(request, 'rango/index.html', context)

@login_required
def battle(request, enemy_id):
    #this is for the turn based battles with enemies
    player = get_object_or_404(UserProfile, user = request.user)
    enemy = get_object_or_404(Enemy, id=enemy_id)

    player_damage = max(1, player.attack - enemy.defense)
    enemy_damage = max(1, enemy_damage - player.defence)
    dodge_chance = random.random() < (player.agility/100)

    if not dodge_chance:
        player.health -= enemy_damage

    enemy_health -= player_damage

    if enemy.health <= 0:
        player.gold += enemy.gold_drop
        enemy.delete()#ive looked around somw other django games and also asked chatgpt, its better if we populate the data base with the enemy we fight apparantly(up for disscussions later on if needed)
        battle_outcome = "win"
    elif player.health <= 0:
        battle_outcome = "lose"
    else:
        battle_outcome = "ongoing"

    player.save()

    return JsonResponse({
        "battle_outcome": battle_outcome,
        "player_health": player.health,
        "enemy_health": enemy.health,
        "gold": player.gold
    })

@login_required
def achievements(request):
    #displays player achievements
    player = get_object_or_404(UserProfile, user=request.user)
    achievements = Achievement.objects.filter(player=player)
    
    return render(request, "rango/achievements.html", {"achievements": achievements})

def play(request):

    return render(request, 'rango/play.html')

def dungeon(request):

    return render(request, 'rango/dungeon.html')

@login_required
def shop(request):
    #allows players to buy upgrades using gold, thats the only logic ive made here will add the iteams/key to dungeon later. i dont think we need it but i forgot what we decided on
    player = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == "POST":
        upgrade_type = request.POST.get("upgrade_type")
        cost = 20  # fixed cost for now
        
        if player.gold >= cost:
            player.gold -= cost
            if upgrade_type == "attack":
                player.attack += 5
            elif upgrade_type == "defense":
                player.defense += 5
            elif upgrade_type == "agility":
                player.agility += 3
            player.save()
            return JsonResponse({"success": True, "message": f"{upgrade_type} has been improved!"})
        else:
            return JsonResponse({"success": False, "message": "Not enough gold for that!"})

    return render(request, "rango/shop.html", {"player": player})

@login_required
def stranger(request):
    #handles the logic for progressing to the next stage
    player = get_object_or_404(UserProfile, user=request.user)
    gold_required = 50  #fixed amount needed to pass

    if player.gold >= gold_required:
        player.gold -= gold_required
        player.location = "dungeon" if player.location == "jungle" else "boss_fight"
        player.save()
        return JsonResponse({"success": True, "message": "You have been granted passage!"})
    
    return JsonResponse({"success": False, "message": "That is not enough gold!"})

