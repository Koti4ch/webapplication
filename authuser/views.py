from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .models import User, PersonalUserInfo
from .forms import LoginForm, RegistrationForm
# Create your views here.


####    REGISTRATION FORM       ####
def register(request):
    # if request.method == 'POST':
    #     reg_form = RegistrationForm(request.POST)
    #     if reg_form.is_valid():
    #         new_user = reg_form.save(commit=False)
    #         new_user.set_password(reg_form.cleaned_data['password'])
    #         new_user.save()
    #         return render(request, 'authuser/registration.html', {'new_user': new_user})
    # else:
    form = LoginForm()
    reg_form = RegistrationForm()
    return render(request, 'authuser/registration.html', {'reg_form': reg_form, 'form': form})



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