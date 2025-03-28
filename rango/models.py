from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class UserProfile(models.Model): #copied from previous
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_score = models.IntegerField(default = 0)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
    
class Character(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    max_health = models.IntegerField(default=100) # always max 100 hp, but better still have it.
    current_health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10) # base damage before calculations
    defense = models.IntegerField(default=10) # %damage ignored
    agility = models.IntegerField(default=5) # dodgeChance
    gold = models.IntegerField(default=0)

    start_time = models.DateTimeField(default=now)
    payed_stranger = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user.username}'s Character"
    
    
class Enemy(models.Model):
    name = models.CharField(max_length=50, default="rabbit")
    max_health = models.IntegerField(default=50)
    min_damage = models.IntegerField(default=5)
    max_damage = models.IntegerField(default=15)
    defense = models.IntegerField(default=5)
    gold_drop = models.IntegerField(default=10)
    image_filename = models.CharField(max_length=100, default="skeleton.jpg") # whole page background image, implement later

    #gives the full path
    def getImageUrl(self):
        return f"/static/enemy_images/{self.image_filename}"

    def __str__(self):
        return self.name
    
class Action(models.Model): # Attack buttons mid-fight
    ATTACK = 'attack'
    BUFF = 'buff'
    
    ACTION_TYPES = [
        (ATTACK, 'Attack'),
        (BUFF, 'Buff'),
    ]

    name = models.CharField(max_length=50, default='bash')
    action_type = models.CharField(max_length=10, choices=ACTION_TYPES, default=ATTACK)

    # For attack actions
    dmg_multiplier = models.FloatField(default=1.0)  # 100% damage
    miss_chance = models.FloatField(default=0.0)  # 0.0 = no miss, 1.0 = always miss
    crit_chance = models.FloatField(default=0.0)  # 0.0 = no crit, 1.0 = always crit

    # for buff actions (if action_type == 'buff')
    luck_increase = models.IntegerField(default=0, blank=True, null=True)
    atk_increase = models.IntegerField(default=0, blank=True, null=True)
    def_increase = models.IntegerField(default=0, blank=True, null=True)
    adp_increase = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    # players = models.ManyToManyField(User, blank=True)  # Tracks which users unlocked it
    # name = models.CharField(max_length=100, default='none')
    # description = models.TextField(default="")
    # unlocked = models.BooleanField(default=False)
    # #image = models.ImageField(upload_to='achievement_images/', blank=True) # icon


    # def __str__(self):
    #     return f"{self.player.user.username} - {self.name}"

    pass
