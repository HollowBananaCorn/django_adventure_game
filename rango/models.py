from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model): #copied from previous
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_score = models.IntegerField(default = 0)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
    
class Character(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # health = models.IntegerField(default=100) # always max 100 hp, only keep track of current
    # attack = models.IntegerField(default=10) # base damage before calculations
    # defence = models.IntegerField(default=10) # %damage ignored
    # agility = models.IntegerField(default=5) # dodgeChance
    # gold = models.IntegerField(default=0)

    # def __str__(self):
    #     return f"{self.user.username}'s Character"
    pass
    
class Enemy(models.Model):
    name = models.CharField(max_length=50, default="rabbit")
    #health = models.IntegerField(default=50) #probably dont need it since it sytarts with max_health, later substracts during battle.
    max_health = models.IntegerField(default=50)
    min_damage = models.IntegerField(default=5)
    max_damage = models.IntegerField(default=15)
    defense = models.IntegerField(default=5)
    gold_drop = models.IntegerField(default=10)
    #image = models.ImageField(upload_to='enemy_images/', blank=True) # whole page background image, implement later

    def __str__(self):
        return self.name
    
class Action(models.Model): #same as Attack. Might add block/buff later.
    # ACTION_TYPES = [
    #     ('attack', 'Attack'),
    #     ('dodge', 'Dodge'),
    # ]

    # name = models.CharField(max_length=50)
    # action_type = models.CharField(max_length=10, choices=ACTION_TYPES)

    # def __str__(self):
    #     return f"{self.name} ({self.action_type})"
    pass

class Achievement(models.Model):
    # players = models.ManyToManyField(User, blank=True)  # Tracks which users unlocked it
    # name = models.CharField(max_length=100, default='none')
    # description = models.TextField(default="")
    # unlocked = models.BooleanField(default=False)
    # #image = models.ImageField(upload_to='achievement_images/', blank=True) # icon


    # def __str__(self):
    #     return f"{self.player.user.username} - {self.name}"

    pass
