
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .settings import DEBUG
from django.views.generic.base import TemplateView
import users
from users import views as user_views
from  django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("stuffs.urls") ),
    ################################################
    path('register/', auth_views.LoginView.as_view(template_name='users/login.html'), name='register'),#the regester optin has desabled
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Only append if urlpatterns are empty
if DEBUG and not urlpatterns:
    urlpatterns += staticfiles_urlpatterns()