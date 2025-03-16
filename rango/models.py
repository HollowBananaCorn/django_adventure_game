from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model): #will store player related data such as stats,inventory and progress
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    defence = models.IntegerField(default=5)
    agility = models.IntegerField(default=5)
    gold = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default="Jungle")#assuming the wireframes showed the start of the game, can be changed let kshamith know
    defeated_boss = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Enemy(models.Model):
    name = models.CharField(max_length=50)
    health = models.IntegerField(default=50)
    attack = models.IntegerField(default=10)
    defense = models.IntegerField(default=5)
    agility = models.IntegerField(default=3)
    gold_drop = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class Attack(models.Model):  
    name = models.CharField(max_length=50)
    damage = models.IntegerField()

    def __str__(self):
        return f"{self.name} - Damage: {self.damage}"

class Action(models.Model):
    player = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    enemy = models.ForeignKey(Enemy, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=10, choices=[
        ('attack', 'Attack'),
        ('block', 'Block'),
        ('dodge', 'Dodge'),
        ('run', 'Run')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.user.username} - {self.action_type} - {self.enemy.name}"
    
class Achievement(models.Model):  
    #tracks achievements unlocked by players, i dont know if this needs to be here but im adding it from the specs
    player = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    unlocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.user.username} - {self.name}"





   