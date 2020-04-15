from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .models import User, PersonalUserInfo
from .forms import LoginForm, RegistrationUserForm, RegistrationPersonalUserInfo
# Create your views here.


####    REGISTRATION FORM       ####
def register(request):
    if request.method == 'POST':
        reg_form = RegistrationUserForm(request.POST)
        reg_personalInfo = RegistrationPersonalUserInfo(request.POST)
        
        if reg_form.is_valid() and reg_personalInfo.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            new_user.save()
            new_info = reg_personalInfo.save(commit=False)
            new_info.user =  new_user
            new_info.save()
        return render(request, 'authuser/registration_page.html', {'reg_form': reg_form, 'userinfo_form':reg_personalInfo})
    else:
        form = LoginForm()
        reg_form = RegistrationUserForm()
        reg_personalInfo = RegistrationPersonalUserInfo()
        return render(request, 'authuser/registration_page.html', {'reg_form': reg_form, 'form': form, 'userinfo_form':reg_personalInfo})



####    LOGIN  FROM       ####
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                username=cd['username'],
                password=cd['password'],
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'authuser/login_form.html', {"form" : form})


def startPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print('Send form data:\nusername: {}\npassword: {}'.format(cd['username'], cd['password']))
            return render(request, 'base_tmpl.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'base_tmpl.html', {'form': form})