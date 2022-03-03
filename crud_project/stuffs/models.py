from pyexpat import model
from django.db import models
from django.db.models.aggregates import Count
from django.db.models.base import Model

# Create your models here.

class abst_base(models.Model):
    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*

    class Meta:
        abstract = True


class gpu(abst_base):
    graphics_card_ram_size = models.SmallIntegerField()
    series=models.CharField(max_length=10)
    computer_memory_type = models.CharField(max_length=10)
    log=models.CharField(max_length=300)

    def __str__(self):
        return "gpu-"+self.series+"-"+str(self.graphics_card_ram_size)

class cpu(abst_base):
    series= models.CharField(max_length=100) 
    log=models.CharField(max_length=300)

    def __str__(self):
        return "cpu:"+self.series

class power(abst_base):
    watt = models.CharField(max_length=100)
    is24pin = models.BooleanField(null=True, blank=True)
    log=models.CharField(max_length=300)

    def __str__(self):
        return "power added"

class hard(abst_base):
    capacity = models.SmallIntegerField()
    hardtpype = models.CharField(max_length=100,blank=True)    
    log=models.CharField(max_length=300)

    def __str__(self):
        return "hard added"

class MOTHERBOARD(abst_base):
    series = models.CharField(max_length=100)
    log=models.CharField(max_length=300)

    def __str__(self):
        return "MOTHERBOARD added"

class fan(abst_base):
    series = models.CharField(max_length=100)
    log=models.CharField(max_length=300)

    def __str__(self):
        return "fan added"

class ram(abst_base):
    ramtype = models.CharField(max_length=100)
    ramsize=models.SmallIntegerField()
    log=models.CharField(max_length=300)

    def __str__(self):
        return "ram added"

class keybordandmouse(abst_base):
    keybordormouse = models.CharField(max_length=100)
    vgaorusb=models.CharField(max_length=100,blank=True)
    log=models.CharField(max_length=300)

    def __str__(self):
        return "keybordandmouse added"

class etc(abst_base):
    name = models.CharField(max_length=100)
    log=models.CharField(max_length=300)

    def __str__(self):
        return "etc added"









