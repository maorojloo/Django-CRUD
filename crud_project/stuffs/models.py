from pyexpat import model
from django.db import models
from django.db.models.aggregates import Count
from django.db.models.base import Model

class BaseModel(models.Model):

    new = models.BooleanField(null=True, blank=True)#*
    issue = models.CharField(max_length=100, blank=True)#*
    countt=models.SmallIntegerField()#*
    etc = models.CharField(max_length=100,blank=True)#*
    log=models.CharField(max_length=300)
    
    class Meta:
        abstract = True 

# Create your models here.
class gpu(BaseModel):
    graphics_card_ram_size = models.SmallIntegerField()
    series=models.CharField(max_length=10)
    computer_memory_type = models.CharField(max_length=10)
    
    def __str__(self):
        return "gpu-"+self.series+"-"+str(self.graphics_card_ram_size)

class cpu(BaseModel):
    series= models.CharField(max_length=100)

    def __str__(self):
        return "cpu:"+self.series

class power(BaseModel):
    watt = models.CharField(max_length=100)
    is24pin = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "power added"

class hard(BaseModel):
    capacity = models.SmallIntegerField()
    hardtpype = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return "hard added"

class MOTHERBOARD(BaseModel):
    series = models.CharField(max_length=100)
    
    def __str__(self):
        return "MOTHERBOARD added"

class fan(BaseModel):
    series = models.CharField(max_length=100)

    def __str__(self):
        return "fan added"

class ram(BaseModel):
    ramtype = models.CharField(max_length=100)
    ramsize=models.SmallIntegerField()

    def __str__(self):
        return "ram added"

class keybordandmouse(BaseModel):
    keybordormouse = models.CharField(max_length=100)
    vgaorusb=models.CharField(max_length=100,blank=True)
    
 
    def __str__(self):
        return "keybordandmouse added"

class etc(BaseModel):
    name = models.CharField(max_length=100)
     
    def __str__(self):
        return "etc added"









