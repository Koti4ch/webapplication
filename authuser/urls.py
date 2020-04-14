from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('', views.startPage, name='index'),
    path('reg/', views.register, name='registration'),
]