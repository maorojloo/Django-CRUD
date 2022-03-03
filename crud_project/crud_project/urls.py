
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
    path('password-reset/',  auth_views.PasswordResetView.as_view(template_name='users/resetpassword.html'), name='password_reset'),
    path('password-reset-done/',  auth_views.PasswordResetDoneView.as_view(template_name='users/resetpassword-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(template_name='users/PasswordReset-Confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',  auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'), name='password_reset_complete'),
    #############################################
    path('admin/', admin.site.urls),
    path('',include("stuffs.urls") ),
    ################################################
    path('register/', auth_views.LoginView.as_view(template_name='users/login.html'), name='register'),#the regester optin has desabled
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),  
]

# Only add this when we in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


