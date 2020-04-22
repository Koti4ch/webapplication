from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, PersonalUserInfo
from .forms import LoginForm, RegistrationUserForm, RegistrationPersonalUserInfo, EditUser, EditPersonalInfo
# Create your views here.


####    REGISTRATION FORM       ####
def register(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'Вы уже зарегистрированы ')
        return redirect('edit_profile')
    if request.method == 'POST':
        reg_form = RegistrationUserForm(request.POST)
        reg_personalInfo = RegistrationPersonalUserInfo(request.POST)
        
        if reg_form.is_valid() and reg_personalInfo.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            new_user.save()
            new_info = reg_personalInfo.save(commit=False)
            new_info.user = new_user
            new_info.save()
            messages.add_message(
                request, messages.INFO, 'Пользователь {} зарегистрирован. Можете <a class="alert-link" href="#" data-toggle="modal" data-target="#auth-popup">войти</a> используя логин и пароль.'.format(new_user.username))
            return redirect('index')
    else:
        form = LoginForm()
        reg_form = RegistrationUserForm()
        reg_personalInfo = RegistrationPersonalUserInfo()
        return render(request, 'authuser/registration_page.html', {'reg_form': reg_form, 'form': form, 'userinfo_form':reg_personalInfo})



def logout_user(request):
    if  not request.user.is_authenticated:
        return redirect('index')
    else:
        logout(request)
    # form = LoginForm()
        messages.add_message(request, messages.INFO, 'Вы вышли из аккаунта!')
        return redirect('index')



def startPage(request):
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
                messages.add_message(request, messages.SUCCESS, 'Вы вошли под именем {}'.format(request.user.username))
                # return render(request, 'base_tmpl.html', {'form': form})
            else:
                messages.add_message(
                    request, messages.WARNING, 'Учетная запись {} отключена!'.format(request.user.username))
        else:
            messages.add_message(request, messages.ERROR, 'Неверный логин или пароль!')
        return redirect('index')
    else:
        form = LoginForm()
        return render(request, 'base_tmpl.html', {'form': form})


@login_required
def editUserInfo(request):
    if request.method == 'POST':
        print(request.POST.get('next'))
        user_form = EditUser(instance=request.user, data=request.POST)
        profile_form = EditPersonalInfo(instance=request.user.personaluserinfo, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            messages.add_message(request, messages.INFO, 'Данные пользователя обновлены.')
            user_form.save()
            profile_form.save()
    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditPersonalInfo(instance=request.user.personaluserinfo)
    
    return render(request, 'authuser/profile_page.html', {'user_form': user_form, 'profile_form': profile_form})
