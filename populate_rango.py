import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_adventure_game.settings')

import django
django.setup() 
from rango.models import Enemy#, Action, Achievement #for now only enemy to implement basics of battle

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

    for enemy in enemies:
        add_enemy(enemy['name'], enemy['max_health'], enemy['min_damage'], enemy['max_damage'], enemy['defense'], enemy['gold_drop'], enemy['image_filename'])


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


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    print('done')