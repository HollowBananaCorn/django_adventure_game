from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Enemy(models.Model):
    pass

class Attack(models.Model):
    pass

class Action(models.Model):
    pass

class Achievement(models.Model):
    pass

class UserProfile(models.Model): #copied from previous
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username