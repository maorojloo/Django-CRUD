from django import forms
from django.db import models
from django.forms import fields
from .models import post
from django.utils import timezone

class post_add_form(forms.ModelForm):
    
    
    title= forms.CharField()
    content= forms.CharField(widget=forms.Textarea)
    

    
    class Meta:
        model=post
        fields=['title','content']