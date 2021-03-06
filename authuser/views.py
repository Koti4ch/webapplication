from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

from .models import User, PersonalUserInfo
from .forms import LoginForm, RegistrationUserForm, RegistrationPersonalUserInfo, EditUser, EditPersonalInfo
# Create your views here.

####    Login function
# def authenticateOurUser(request, redirect_next):
#     auth_form = LoginForm(request.POST)
#     if auth_form.is_valid():
#         print('auth_form is valid')
#         clear_data = auth_form.cleaned_data
#         user = authenticate(request, user=clear_data['username'], password=clear_data['password'])

#         if user is not None:
#             if user.is_active:
#                 print('user is active')
#                 login(request, user)
#                 messages.add_message(
#                     request, messages.SUCCESS, 'Вы вошли под именем {}'.format(request.user.username))
#                 if redirect_next == '':
#                     return redirect('index')
#                 else:
#                     return redirect(redirect_next)
#             else:
#                 messages.add_message(
#                     request, messages.WARNING, 'Учетная запись {} отключена!'.format(request.user.username))
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  'Неверный логин или пароль!')
#     return HttpResponseRedirect(next)


####    Custom Password Change view     ####
class PasswordChanger(PasswordChangeView):
    template_name = 'authuser/chpass_page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, "Пароль был успешно изменен.")
        return super().form_valid(form)

####    Custom Password Reset view      ####
class PasswordReset(PasswordResetView):
    template_name = 'authuser/password_reset_page.html'
    # email_template_name = "authuser/password_reset_email_tmplt.html"
    html_email_template_name = "authuser/password_reset_email_tmplt.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "На почту выслана ссылка для смены пароля от аккаунта")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid")
        messages.error(self.request, "Error!")
        return super().form_invalid(form)

####    Custom Password Reset Confirm view      ####
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'authuser/password_reset_confirm.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, "Пароль был успешно изменен")
        return super().form_valid(form)

####    Password Reset Comlete view         ####
# class PasswordResetComplete(PasswordResetCompleteView):
#     template_name = 'base_tmpl.html'

#     def get_template_names(self):
#         messages.success(self.request, "Пароль был успешно изменен")
#         return super().get_template_names()


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
        login_form = LoginForm()
        reg_form = RegistrationUserForm()
        reg_personalInfo = RegistrationPersonalUserInfo()
        # for i in reg_form.fields:
        #     print(i, reg_form.fields[i].required)
        requiredFieldsList = [field for field in reg_form.fields if reg_form.fields[field].required]
        requiredFieldsList += [field for field in reg_personalInfo.fields if reg_personalInfo.fields[field].required]
        return render(request, 'authuser/registration_page.html', {'reg_form': reg_form, 'login_form': login_form, 'userinfo_form':reg_personalInfo, 'requiredFields': requiredFieldsList})



def logout_user(request):
    if  not request.user.is_authenticated:
        return redirect('index')
    else:
        logout(request)
    # form = LoginForm()
        messages.add_message(request, messages.INFO, 'Вы вышли из аккаунта!')
        return redirect('index')



def login_page(request):
    redirect_next = request.GET['next'] if request.GET else ''
    
    if request.method == 'GET':
        if not request.user.is_authenticated:
            login_form = LoginForm()
            return render(request, 'authuser/login_page.html', {'login_form': login_form, 'redirect_next': redirect_next})
        else:
            messages.add_message(request, messages.INFO, 'Вы уже авторизованы на сайте!')
            return redirect('index')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            clear_data = login_form.cleaned_data
            user = authenticate(request, username=clear_data['username'], password=clear_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, 'Вы вошли под именем {}'.format(request.user.username))
                    if redirect_next == '':
                        return redirect('index')
                    else:
                        return redirect(redirect_next)
                else:
                    messages.add_message(
                        request, messages.WARNING, 'Учетная запись {} отключена!'.format(request.user.username))
            else:
                messages.add_message(request, messages.ERROR,
                                    'Неверный логин или пароль!')
        return redirect('index')


def startPage(request):
    if request.method == 'POST':
        pass
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     cd = form.cleaned_data
        #     user = authenticate(request,
        #                         username=cd['username'],
        #                         password=cd['password'],
        #                         )
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         messages.add_message(request, messages.SUCCESS, 'Вы вошли под именем {}'.format(request.user.username))
        #         # return render(request, 'base_tmpl.html', {'form': form})
        #     else:
        #         messages.add_message(
        #             request, messages.WARNING, 'Учетная запись {} отключена!'.format(request.user.username))
        # else:
        #     messages.add_message(request, messages.ERROR, 'Неверный логин или пароль!')
        # return redirect('index')
        login_form = LoginForm()
        return render(request, 'base_tmpl.html', {'login_form': login_form})
    else:
        login_form = LoginForm()
        return render(request, 'base_tmpl.html', {'login_form': login_form})


@login_required
def editUserInfo(request):
    if request.method == 'POST':
        print(request.POST.get('next'))
        user_form = EditUser(instance=request.user, data=request.POST)
        profile_form = EditPersonalInfo(instance=request.user.personaluserinfo, data=request.POST, files=request.FILES)

        print(profile_form)

        if user_form.is_valid() and profile_form.is_valid():
            messages.add_message(request, messages.INFO, 'Данные пользователя обновлены.')
            user_form.save()
            profile_form.save()
    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditPersonalInfo(instance=request.user.personaluserinfo)
    
    return render(request, 'authuser/profile_page.html', {'user_form': user_form, 'profile_form': profile_form})
