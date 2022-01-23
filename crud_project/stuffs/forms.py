from django import forms
from django.db import models
from django.forms import fields
from .models import cpu, gpu, power,hard,MOTHERBOARD,fan,ram,keybordandmouse,etc,MOTHERBOARD

class adding_gpu_form(forms.ModelForm):
    #graphics_card_ram_size= forms.CharField(required=False)
    #series= forms.CharField(required=False)
    #CHOICES=[('1','1'),('2','2')]
    #computer_memory_type= forms.CharField(choices=[('select1','select 1'),('select2','select 2')], widget=forms.RadioSelect,required=False)

    CHOICES = [('ddr1','ddr1'),('ddr2','ddr3'),('ddr3','ddr3'),('ddr4','ddr4'),('etc','etc')]
    computer_memory_type=forms.CharField(label='computer memory type', widget=forms.RadioSelect(choices=CHOICES))

    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))

    issue= forms.CharField(required=False)
    #countt= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    


    class Meta:
        model=gpu
        fields=['graphics_card_ram_size','series','computer_memory_type','new','issue','countt','etc']

      
class adding_cpu_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=cpu
        fields=['series','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']

class adding_hard_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    CHOICES = [('hdd','hdd'),('ssd','ssd'),('hdd 2.5 inch','hdd 2.5 inch'),('ssd 2.5 inch','ssd 2.5 inch'),('etc','etc')]
    hardtpype=forms.CharField(label='hard type', widget=forms.RadioSelect(choices=CHOICES))


    
    class Meta:
        model=hard
        fields=['capacity','hardtpype','new','issue','countt','etc']


class adding_MOTHERBOARD_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    

    
    class Meta:
        model=MOTHERBOARD
        fields=['series','new','issue','countt','etc']


class adding_fan_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)

    
    class Meta:
        model=fan
        fields=['series','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']


class adding_power_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    is24pin = forms.BooleanField( required=False)

    
    class Meta:
        model=power
        fields=['watt','is24pin','new','issue','countt','etc']

class adding_ram_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    CHOICES = [('ddr1','ddr1'),('ddr2','ddr3'),('ddr3','ddr3'),('ddr4','ddr4'),('etc','etc')]
    ramtype=forms.CharField(label='computer memory type', widget=forms.RadioSelect(choices=CHOICES))
    
    class Meta:
        model=ram
        fields=['ramtype','ramsize','new','issue','countt','etc']

     
class adding_etc_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    
    class Meta:
        model=etc
        fields=['name','new','issue','countt','etc']




class adding_keybordandmouse_form(forms.ModelForm):
    
    CHOICES = [('True','True'),('False','False')]
    new=forms.CharField(label='new or stock?', widget=forms.RadioSelect(choices=CHOICES))
    issue= forms.CharField(required=False)
    etc= forms.CharField(required=False)
    CHOICES = [('vga','vga'),('usb','usb')]
    vgaorusb=forms.CharField(label='vga or usb?', widget=forms.RadioSelect(choices=CHOICES))
    CHOICES = [('keybord','keybord'),('mouse','mouse')]
    keybordormouse=forms.CharField(label='keybord or mouse?', widget=forms.RadioSelect(choices=CHOICES))
    
    class Meta:
        model=keybordandmouse
        fields=['keybordormouse','vgaorusb','issue','countt','etc']







