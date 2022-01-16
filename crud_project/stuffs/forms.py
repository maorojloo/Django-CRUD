from django import forms
from django.db import models
from django.forms import fields
from .models import cpu, gpu, power,hard,MOTHERBOARD,fan,ram,keybordandmouse,etc,MOTHERBOARD

class adding_gpu_form(forms.ModelForm):
    #graphics_card_ram_size= forms.CharField(required=False)
    #series= forms.CharField(required=False)
    computer_memory_type= forms.CharField(required=False)
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    #countt= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=gpu
        fields=['graphics_card_ram_size','series','computer_memory_type','new','issue','countt','etc']

      
class adding_cpu_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=cpu
        fields=['series','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']

class adding_hard_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    hardtpype = forms.CharField( required=False)

    
    class Meta:
        model=hard
        fields=['capacity','hardtpype','new','issue','countt','etc']


class adding_MOTHERBOARD_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    

    
    class Meta:
        model=MOTHERBOARD
        fields=['series','new','issue','countt','etc']


class adding_fan_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)

    
    class Meta:
        model=fan
        fields=['series','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']

class adding_ram_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=ram
        fields=['ramtype','ramsize','new','issue','countt','etc']

     
class adding_etc_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=etc
        fields=['name','new','issue','countt','etc']




class adding_etc_form(forms.ModelForm):
    
    new= forms.CharField(required=False)
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=keybordandmouse
        fields=['keybordormouse','vgaorusb','issue','countt','etc']







