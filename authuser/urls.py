from django.urls import path
from django.contrib.auth import views as contrib_auth

from . import views

urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('login/', contrib_auth.LoginView.as_view(template_name='authuser/login_page.html'), name='login'),
    path('logout/', contrib_auth.LogoutView.as_view(), name='logout'),
    path('', views.startPage, name='index'),
    path('reg/', views.register, name='registration'),
    #### change password   ####
    path('password_change/', contrib_auth.PasswordChangeView.as_view(
        template_name='authuser/chpass_page.html'), name='password_change'),
]
