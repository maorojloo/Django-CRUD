from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
import users



class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='defaultjpg',upload_to='profile_pics')

def __str__(self):
    return f'{self.user.username} profile'