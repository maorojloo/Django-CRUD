from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
 
from django.contrib.auth.models import User # Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateField(default=timezone.now)
    author = models.TextField()
    log= models.CharField(max_length=100)
    attachedfile=models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title 

 