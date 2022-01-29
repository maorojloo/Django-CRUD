from django.urls import path
from django.urls.resolvers import URLPattern
from django.urls.conf import include
from . import views 


urlpatterns = [

    path('',include("post.urls") ),
    ###############################################
    path('gpu/',views.list_stuffs,name='list_stuffs'),
    path('cpu/',views.cpu_list,name='cpu_list'),
    path('power/',views.power_list,name='power_list'),
    path('hard/',views.hard_list,name='hard_list'),
    path('MOTHERBOARD/',views.MOTHERBOARD_list,name='MOTHERBOARD_list'),
    path('fan/',views.fan_list,name='fan_list'),
    path('ram/',views.ram_list,name='ram_list'),
    path('keybordandmouse/',views.keybordandmouse_list,name='keybordandmouse_list'),
    path('etc/',views.etc_list,name='etc_list'),
    ##################################################################################
    path('update/<str:table>/<int:id>/',views.update_gpu,name='update_gpu'),
    ##################################################################################
    path('delete/<str:table>/<int:id>/',views.delete_gpu,name='delete_gpu'),
    ##################################################################################
    path('plusone/<str:table>/<int:id>/',views.gpu_plusone,name='gpu_plusone'),
    path('minusone/<str:table>/<int:id>',views.gpu_minusone,name='gpu_minusone'),
    ###################################################################################
    path('add/<str:table>/',views.add_gpu,name='add_gpu'),
    ##################################################################################
   
    
]
handler404 = "stuffs.views.page_not_found_view"
