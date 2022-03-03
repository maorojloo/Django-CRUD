from django.urls import path
from django.urls.resolvers import URLPattern
from .views import post_delete,post_add,post_update,home#,Postlistview

 
urlpatterns = [
    path('',home, name='postـhome' ),
    #path('',Postlistview.as_view(), name='postـhome' ),
    path('post/delete/<int:id>/',post_delete,name='post-delete'),
    path('post/add/',post_add,name='post_add'),
    path('post/update/<int:id>/',post_update,name='post_update'),


    
   
    
]
handler404 = "stuffs.views.page_not_found_view"
 