from django.urls import path
# from django.contrib.auth import views as contrib_auth

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    # path('login/', contrib_auth.LoginView.as_view(template_name='authuser/login_page.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.startPage, name='index'),
    path('reg/', views.register, name='registration'),
    path('profile/', views.editUserInfo, name='edit_profile'),
    #### change password   ####
    path('chpass/', views.PasswordChanger.as_view(), name='password_change'),
    # path('password_change/', contrib_auth.PasswordChangeView.as_view(
    #     template_name='authuser/chpass_page.html',
    #     success_url='/',
    #     ), name='password_change'),
]
