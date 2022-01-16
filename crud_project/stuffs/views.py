from django.forms.forms import Form
from django.shortcuts import render,redirect
from .models import gpu,cpu,power,hard,ram,fan,MOTHERBOARD,keybordandmouse,etc
from .forms import adding_gpu_form ,adding_cpu_form,adding_power_form,adding_etc_form,adding_hard_form,adding_MOTHERBOARD_form,adding_fan_form,adding_MOTHERBOARD_form,adding_ram_form
from django.contrib import messages
from django.shortcuts import render

from django.contrib.auth.decorators import login_required





#404
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

#home page
@login_required(login_url='/login/') #redirect when user is not logged in
def home_page(request):
    return render(request, 'home.html')



# Create your views here.
@login_required(login_url='/login/') #redirect when user is not logged in
def list_stuffs(request):
    gpus = gpu.objects.all()
    return render(request,'gpu.html',{'gpus':gpus})
#lisitg cpus
@login_required(login_url='/login/') #redirect when user is not logged in
def cpu_list(request):
    cpus = cpu.objects.all()
    return render(request,'cpu.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def power_list(request):
    cpus = power.objects.all()
    return render(request,'power.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def hard_list(request):
    cpus = hard.objects.all()
    return render(request,'hard.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def MOTHERBOARD_list(request):
    cpus = MOTHERBOARD.objects.all()
    return render(request,'MOTHERBOARD.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def fan_list(request):
    cpus = fan.objects.all()
    return render(request,'fan.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def ram_list(request):
    cpus = ram.objects.all()
    return render(request,'ram.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def keybordandmouse_list(request):
    cpus = keybordandmouse.objects.all()
    return render(request,'keybordandmouse.html',{'cpus':cpus})

@login_required(login_url='/login/') #redirect when user is not logged in
def etc_list(request):
    cpus = etc.objects.all()
    return render(request,'etc.html',{'cpus':cpus})





@login_required(login_url='/login/') #redirect when user is not logged in
def add_gpu(request,table):
    add_template_name='addform.html'


    if table=='gpu':
        redirect_url='list_stuffs'
        addpage_url='addingstuff.html'
        form = adding_gpu_form(request.POST or None)

    if table=='cpu':
        form = adding_cpu_form(request.POST or None)
        redirect_url='cpu_list'
        addpage_url='add_cpu.html'

    if table=='power':
        form = adding_power_form(request.POST or None)
        redirect_url='power_list'
        addpage_url='add_power.html'

    if table=='hard':
        form = adding_hard_form(request.POST or None)
        redirect_url='hard_list'
        addpage_url='add_hard.html'

    if table=='MOTHERBOARD':
        form = adding_MOTHERBOARD_form(request.POST or None)
        redirect_url='MOTHERBOARD_list'
        addpage_url='add_MOTHERBOARD.html'

    if table=='fan':
        form = adding_fan_form(request.POST or None)
        redirect_url='fan_list'
        addpage_url='add_fan.html'

    if table=='ram':
        form = adding_ram_form(request.POST or None)
        redirect_url='ram_list'
        addpage_url='add_ram.html'

    if table=='keybordandmouse':
        form = adding_gpu_form(request.POST or None)
        redirect_url='keybordandmouse_list'
        addpage_url='add_keybordandmouse.html'

    if table=='etc':
        form = adding_etc_form(request.POST or None)
        redirect_url='etc_list'
        addpage_url='add_etc.html'


    if form.is_valid():
        form.save()
        messages.success(request,"item has been added successfully")
        #return  redirect('list_stuffs')
        return  redirect(redirect_url)
    else:
        if request.method =='POST':
            messages.warning(request, 'some things went wrong try again')
        return render (request, add_template_name ,{'form':form} )



















@login_required(login_url='/login/') #redirect when user is not logged in
def update_gpu(request,table,id): #ok
    if table=='gpu':
        gpuone = gpu.objects.get(id=id)
        form = adding_gpu_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('list_stuffs')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

    if table=='cpu':
        gpuone = cpu.objects.get(id=id)
        form = adding_cpu_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('cpu_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

    if table=='power':
        gpuone = power.objects.get(id=id)
        form = adding_power_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('power_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

    if table=='hard':
        gpuone = hard.objects.get(id=id)
        form = adding_hard_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('hard_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

    if table=='MOTHERBOARD':
        gpuone = MOTHERBOARD.objects.get(id=id)
        form = adding_MOTHERBOARD_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('motherboard_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

    if table=='fan':
        gpuone = fan.objects.get(id=id)
        form = adding_fan_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('fan_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )

    if table=='ram':
        gpuone = ram.objects.get(id=id)
        form = adding_ram_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('ram_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} )    

    if table=='keybordandmouse':
        gpuone = keybordandmouse.objects.get(id=id)
        form = adding_keybordandmouse_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('keybordandmouse_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} ) 

    if table=='etc':
        gpuone = etc.objects.get(id=id)
        form = adding_etc_form(request.POST or None, instance=gpuone)
        if form.is_valid():
            form.save()
            messages.success(request,"item has been updated successfully")
            return redirect('etc_list')
        else:
            return render (request, 'gpu_edite.html' ,{'form':form , 'gpuone':gpuone} ) 



@login_required(login_url='/login/') #redirect when user is not logged in
def delete_gpu(request,table,id):
    redirect_page=''
    gpuone=''

    if table=='gpu':
        gpuone = gpu.objects.get(id=id)
        redirect_page='list_stuffs'

    if table=='cpu':
        gpuone = cpu.objects.get(id=id)
        redirect_page='cpu_list'

    if table=='power':
        gpuone = power.objects.get(id=id)
        redirect_page='power_list'

    if table=='hard':
        gpuone = hard.objects.get(id=id)
        redirect_page='hard_list'

    if table=='MOTHERBOARD':
        gpuone = MOTHERBOARD.objects.get(id=id)
        redirect_page='MOTHERBOARD_list'

    if table=='fan':
        gpuone = fan.objects.get(id=id)
        redirect_page='fan_list'

    if table=='ram':
        gpuone = ram.objects.get(id=id)
        redirect_page='ram_list'

    if table=='keybordandmouse':
        gpuone = keybordandmouse.objects.get(id=id)
        redirect_page='keybordandmouse_list'

    if table=='etc':
        gpuone = etc.objects.get(id=id)
        redirect_page='etc_list'


    if request.method == 'POST':
        gpuone.delete()
        messages.success(request,"record has been deleted successfully")
        return redirect(redirect_page)
    else:
        return render(request, 'gpu_delete.html', {'gpuone':gpuone} )
'''
#DELETE RECORD WITH OUT CONFOMATIN
def delete_gpu(request,id):
    gpuone = gpu.objects.get(id=id)
    gpuone.delete()
    messages.success(request,"record has been deleted successfully")
    return redirect('list_stuffs')#show deleted msg
'''












@login_required(login_url='/login/') #redirect when user is not logged in
def gpu_plusone(request,table,id):
    redirect_page=''
    gpuone=''

    if table=='gpu':
        gpuone = gpu.objects.get(id=id)
        redirect_page='list_stuffs'

    if table=='cpu':
        gpuone = cpu.objects.get(id=id)
        redirect_page='cpu_list'

    if table=='power':
        gpuone = power.objects.get(id=id)
        redirect_page='power_list'

    if table=='hard':
        gpuone = hard.objects.get(id=id)
        redirect_page='hard_list'

    if table=='MOTHERBOARD':
        gpuone = MOTHERBOARD.objects.get(id=id)
        redirect_page='MOTHERBOARD_list'

    if table=='fan':
        gpuone = fan.objects.get(id=id)
        redirect_page='fan_list'

    if table=='ram':
        gpuone = ram.objects.get(id=id)
        redirect_page='ram_list'

    if table=='keybordandmouse':
        gpuone = keybordandmouse.objects.get(id=id)
        redirect_page='keybordandmouse_list'

    if table=='etc':
        gpuone = etc.objects.get(id=id)
        redirect_page='etc_list'


    x=gpuone.countt
    gpuone.countt=x+1
    gpuone.save()
    messages.success(request,"item Number has been +1 successfully")
    return redirect(redirect_page)

@login_required(login_url='/login/') #redirect when user is not logged in
def gpu_minusone(request,table,id):
    redirect_page=''
    gpuone=''

    if table=='gpu':
        gpuone = gpu.objects.get(id=id)
        redirect_page='list_stuffs'

    if table=='cpu':
        gpuone = cpu.objects.get(id=id)
        redirect_page='cpu_list'

    if table=='power':
        gpuone = power.objects.get(id=id)
        redirect_page='power_list'

    if table=='hard':
        gpuone = hard.objects.get(id=id)
        redirect_page='hard_list'

    if table=='MOTHERBOARD':
        gpuone = MOTHERBOARD.objects.get(id=id)
        redirect_page='MOTHERBOARD_list'

    if table=='fan':
        gpuone = fan.objects.get(id=id)
        redirect_page='fan_list'

    if table=='ram':
        gpuone = ram.objects.get(id=id)
        redirect_page='ram_list'

    if table=='keybordandmouse':
        gpuone = keybordandmouse.objects.get(id=id)
        redirect_page='keybordandmouse_list'

    if table=='etc':
        gpuone = etc.objects.get(id=id)
        redirect_page='etc_list'


    
    x=gpuone.countt
    if x<=1:
        if request.method == 'POST':
            gpuone.delete()
            messages.success(request,"record has been deleted successfully")
            return redirect(redirect_page) 
        return render(request, 'gpu_delete.html', {'gpuone':gpuone} )    
    else:
        gpuone.countt=x-1
        gpuone.save()
        messages.success(request,"item Number has been -1 successfully")
        return redirect(redirect_page)

