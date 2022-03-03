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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
from pycoingecko import CoinGeckoAPI




coinapi = CoinGeckoAPI() 
@login_required(login_url='/login/') #redirect when user is not logged in
def home (request):
    

    try:   
        rates = coinapi.get_price(ids=['bitcoin', 'ethereum','Ethereum','Litecoin','Cardano','Polkadot','Stellar','Dogecoin','Binance Coin','Tether','Solana'], vs_currencies='usd', include_24hr_change=True)
        markt_info=[{"BTC: "+str(rates["bitcoin"]["usd"]):float("{:.2f}".format(rates["bitcoin"]["usd_24h_change"]))},
                {"ETH: "+str(rates["ethereum"]["usd"]):float("{:.2f}".format(rates["ethereum"]["usd_24h_change"]))},
                {"LTC: "+str(rates["litecoin"]["usd"]):float("{:.2f}".format(rates["litecoin"]["usd_24h_change"]))},
                {"ADA: "+str(rates["cardano"]["usd"]):float("{:.2f}".format(rates["cardano"]["usd_24h_change"]))},
                {"DOT: "+str(rates["polkadot"]["usd"]):float("{:.2f}".format(rates["polkadot"]["usd_24h_change"]))},
                {"str: "+str(rates["stellar"]["usd"]):float("{:.2f}".format(rates["stellar"]["usd_24h_change"]))},
                {"DOGE: "+str(rates["dogecoin"]["usd"]):float("{:.2f}".format(rates["dogecoin"]["usd_24h_change"]))},
                {"BNB: "+str(rates["binancecoin"]["usd"]):float("{:.2f}".format(rates["binancecoin"]["usd_24h_change"]))},
                {"USDT: "+str(rates["tether"]["usd"]):float("{:.2f}".format(rates["tether"]["usd_24h_change"]))},
                {"SOL: "+str(rates["solana"]["usd"]):float("{:.2f}".format(rates["solana"]["usd_24h_change"]))}]
    
    except:
        print("an error occurred in getting data from api")
        markt_info="an error occurred in getting data from api"

    
    context={'postss':post.objects.order_by('-date_posted'),"markt_info":markt_info}
   
    return render(request, 'post/home.html',context)


"""

@method_decorator(login_required, name='dispatch')
class Postlistview(ListView):
    model= post
    template_name = 'post/home.html' #app/template.html
    context_object_name = 'postss'
    #ordered_tasks = TaskItem.objects.order_by('-created_date')
    ordering= ['-date_posted']
    """

@login_required(login_url='/login/') #redirect when user is not logged in
def post_delete(request,id):
    apost = post.objects.get(id=id)
    if request.method == 'POST':
        if request.user.username == post.author:
            apost.delete()
            messages.success(request,"the post has been deleted successfully")
            return redirect('postـhome')
        else:
            messages.warning(request,"only "+request.user.username+" has promition to edit this post.")
            return redirect('postـhome')
        
    else:
        return render(request, 'gpu_delete.html', {'apost':apost} )




@login_required(login_url='/login/') #redirect when user is not logged in
def post_add(request):
    add_template_name='upload.html'
    redirect_url='postـhome'
    addpage_url='addingstuff.html'
    
    form = post_add_form(request.POST ,request.FILES)
    
    if form.is_valid():
        task_list=form.save(commit=False)
        messages.success(request,"item has been added successfully")
        #add user name to log
        log_msg="[added by "+request.user.username+"]"
        task_list.log = log_msg
        
        task_list.author=request.user.username
        task_list.save()

        #file
        print("***************************")
        print(task_list.attachedfile)
        print("***************************")
        
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
        if request.user.username == post.author:
        #add user name to log 
            task_list=form.save(commit=False)
            log_msg="[updated by "+request.user.username+"]"
            task_list.log =task_list.log+ log_msg
            task_list.author=request.user.username
            task_list.save()
        else:
            messages.warning(request,"only "+request.user.username+" has promition to edit this post.")
            return redirect('postـhome')
        #end of adding msg to log
            
        messages.success(request,"item has been updated successfully")
        return redirect('postـhome')
    else:
        return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

        