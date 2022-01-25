import imp
from typing import List
from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.
from .models import post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from.forms import post_add_form


def home (request):
    context={'postss':post.objects.order_by('-date_posted')}
   
    return render(request, 'post/home.html',context)

class Postlistview(ListView):
    model= post
    template_name = 'post/home.html' #app/template.html
    context_object_name = 'postss'
    #ordered_tasks = TaskItem.objects.order_by('-created_date')
    ordering= ['-date_posted']

@login_required(login_url='/login/') #redirect when user is not logged in
def post_delete(request,id):
    apost = post.objects.get(id=id)
    if request.method == 'POST':
        apost.delete()
        messages.success(request,"the post has been deleted successfully")
        return redirect('postـhome')
    else:
        return render(request, 'gpu_delete.html', {'apost':apost} )




@login_required(login_url='/login/') #redirect when user is not logged in
def post_add(request):
    add_template_name='addform.html'
    redirect_url='postـhome'
    addpage_url='addingstuff.html'
    
    form = post_add_form(request.POST or None)
    if form.is_valid():
        task_list=form.save(commit=False)
        messages.success(request,"item has been added successfully")
        #add user name to log
        log_msg="[added by "+request.user.username+"]"
        task_list.log = log_msg
        task_list.content = task_list.content+"\n"+log_msg
        task_list.author=request.user.username
        task_list.save()

        
        return  redirect(redirect_url)
    else:
        if request.method =='POST':
            messages.warning(request, 'some things went wrong try again')
        return render (request, add_template_name ,{'form':form} )

@login_required(login_url='/login/') #redirect when user is not logged in
def post_update(request,id): #ok  
    gpuone = post.objects.get(id=id)
    form = post_add_form(request.POST or None, instance=gpuone)
    if form.is_valid():
        #add user name to log 
        task_list=form.save(commit=False)
        log_msg="[updated by "+request.user.username+"]"
        task_list.log =task_list.log+ log_msg
        task_list.content = task_list.content+"\n"+log_msg
        task_list.author=request.user.username
        task_list.save()
        #end of adding msg to log
            
        messages.success(request,"item has been updated successfully")
        return redirect('postـhome')
    else:
        return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

        