import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_adventure_game.settings')

import django
django.setup() 

from django.contrib.auth.models import User
from rango.models import Enemy, Action, UserProfile#, Achievement #for now only enemy to implement basics of battle

def populate():
    enemies = [
        {'name' : 'Skeleton',
         'max_health' : 50,
         'min_damage' : 10,
         'max_damage' : 20,
         'defense' : 0,
         'gold_drop' : 50,
         'image_filename' : 'skeleton.jpg'},
         {'name' : 'Soldier',
         'max_health' : 70,
         'min_damage' : 15,
         'max_damage' : 20,
         'defense' : 20,
         'gold_drop' : 15,
         'image_filename' : 'knight.jpg'},
    ]

    actions = [
        {'name': 'Slash', 
         'action_type': 'attack', 
         'dmg_multiplier': 1.0, 
         'miss_chance': 0.05, 
         'crit_chance': 0.15,
         'luck_increase': 0,
         'atk_increase': 0,
         'def_increase': 0,
         'adp_increase': 0},
        {'name': 'Sniper', 
         'action_type': 'attack', 
         'dmg_multiplier': 3, 
         'miss_chance': 0.7,
         'crit_chance': 0.5,
         'luck_increase': 0,
         'atk_increase': 0,
         'def_increase': 0,
         'adp_increase': 0},
        {'name': 'Barricade', 
         'action_type': 'buff', 
         'dmg_multiplier': 1, 
         'miss_chance': 0.0,
         'crit_chance': 0.0,
         'luck_increase': 0,
         'atk_increase': 0,
         'def_increase': 10,
         'adp_increase': 0},
    ]

    for enemy in enemies:
        add_enemy(enemy['name'], enemy['max_health'], enemy['min_damage'], enemy['max_damage'], enemy['defense'], enemy['gold_drop'], enemy['image_filename'])

    for action in actions:
        add_action(action['name'], action['action_type'], action['dmg_multiplier'], action['miss_chance'], action['crit_chance'], action['luck_increase'], action['atk_increase'], action['def_increase'], action['adp_increase'])

    #create dummy users:
    for i in range(20):
        username = f"dummy_user_{i+1}"
        email = f"{username}@example.com"
        password = "testpassword"

        dummy_user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            dummy_user.set_password(password)
            dummy_user.save()
            max_score = random.randint(30, 5000)
            UserProfile.objects.create(user=dummy_user, max_score=max_score)
            print(f"user {username} added")


def add_enemy(name, max_health, min_damage, max_damage, defense, gold_drop, image_filename):
    e = Enemy.objects.get_or_create(name = name)[0]
    e.max_health = max_health
    e.min_damage= min_damage
    e.max_damage = max_damage
    e.defense = defense
    e.gold_drop = gold_drop
    e.image_filename = image_filename
    e.save()
    return e

def add_action(name, action_type, dmg_multiplier, miss_chance, crit_chance, luck_increase, atk_increase, def_increase, adp_increase):
    a = Action.objects.get_or_create(name=name)[0]
    a.action_type = action_type
    a.dmg_multiplier = dmg_multiplier
    a.miss_chance = miss_chance
    a.crit_chance = crit_chance
    a.luck_increase = luck_increase
    a.atk_increase = atk_increase
    a.def_increase = def_increase
    a.adp_increase = adp_increase
    a.save()
    return a


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    print('done')