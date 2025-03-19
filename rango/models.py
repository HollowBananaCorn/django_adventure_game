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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    health = models.IntegerField(default=100) # always max 100 hp, only keep track of current
    attack = models.IntegerField(default=10) # base damage before calculations
    defence = models.IntegerField(default=10) # %damage ignored
    agility = models.IntegerField(default=5) # dodgeChance
    gold = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Character"
    
class Enemy(models.Model):
    name = models.CharField(max_length=50)
    health = models.IntegerField(default=50)
    max_health = models.IntegerField(default=50)
    min_damage = models.IntegerField(default=5)
    max_damage = models.IntegerField(default=15)
    defense = models.IntegerField(default=5)
    gold_drop = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    
class Action(models.Model): #same as Attack. Might add block/buff later.
    ACTION_TYPES = [
        ('attack', 'Attack'),
        ('dodge', 'Dodge'),
    ]

    name = models.CharField(max_length=50)
    action_type = models.CharField(max_length=10, choices=ACTION_TYPES)

    def __str__(self):
        return f"{self.name} ({self.action_type})"

class Achievement(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    unlocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.user.username} - {self.name}"
