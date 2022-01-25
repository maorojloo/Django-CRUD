from pyexpat import model
from django.db import models
from django.db.models.aggregates import Count
from django.db.models.base import Model

# Create your models here.
class gpu(models.Model):
    graphics_card_ram_size = models.SmallIntegerField()
    series=models.CharField(max_length=10)
    computer_memory_type = models.CharField(max_length=10)
    log=models.CharField(max_length=300)

    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*

    def __str__(self):
        return "gpu-"+self.series+"-"+str(self.graphics_card_ram_size)

class cpu(models.Model):
    series= models.CharField(max_length=100)

    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    

    def __str__(self):
        return "cpu:"+self.series

class power(models.Model):
    watt = models.CharField(max_length=100)
    is24pin = models.BooleanField(null=True, blank=True)

    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)


    def __str__(self):
        return "power added"

class hard(models.Model):
    capacity = models.SmallIntegerField()
    hardtpype = models.CharField(max_length=100,blank=True)

    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    def __str__(self):
        return "hard added"

class MOTHERBOARD(models.Model):
    series = models.CharField(max_length=100)
    
    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    def __str__(self):
        return "MOTHERBOARD added"

class fan(models.Model):
    series = models.CharField(max_length=100)
    
    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    def __str__(self):
        return "fan added"

class ram(models.Model):
    ramtype = models.CharField(max_length=100)
    ramsize=models.SmallIntegerField()
    
    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    def __str__(self):
        return "ram added"

class keybordandmouse(models.Model):
    keybordormouse = models.CharField(max_length=100)
    vgaorusb=models.CharField(max_length=100,blank=True)
    
    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    def __str__(self):
        return "keybordandmouse added"

class etc(models.Model):
    name = models.CharField(max_length=100)
     
    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)

    def __str__(self):
        return "etc added"









