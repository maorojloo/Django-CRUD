from django.urls import path
from django.urls.resolvers import URLPattern
from .views import list_stuffs , add_gpu ,update_gpu ,delete_gpu,gpu_plusone,gpu_minusone,cpu_list
from .views import power_list,hard_list,fan_list,ram_list,etc_list,keybordandmouse_list,MOTHERBOARD_list,home_page



urlpatterns = [

    path('',home_page,name='home_page'),
    ###############################################
    path('gpu/',list_stuffs,name='list_stuffs'),
    path('cpu/',cpu_list,name='cpu_list'),
    path('power/',power_list,name='power_list'),
    path('hard/',hard_list,name='hard_list'),
    path('MOTHERBOARD/',MOTHERBOARD_list,name='MOTHERBOARD_list'),
    path('fan/',fan_list,name='fan_list'),
    path('ram/',ram_list,name='ram_list'),
    path('keybordandmouse/',keybordandmouse_list,name='keybordandmouse_list'),
    path('etc/',etc_list,name='etc_list'),
    ##################################################################################
    path('update/<str:table>/<int:id>/',update_gpu,name='update_gpu'),
    ##################################################################################
    path('delete/<str:table>/<int:id>/',delete_gpu,name='delete_gpu'),
    ##################################################################################
    path('plusone/<str:table>/<int:id>/',gpu_plusone,name='gpu_plusone'),
    path('minusone/<str:table>/<int:id>',gpu_minusone,name='gpu_minusone'),
    ###################################################################################
    path('add/<str:table>/',add_gpu,name='add_gpu'),
]
handler404 = "stuffs.views.page_not_found_view"
