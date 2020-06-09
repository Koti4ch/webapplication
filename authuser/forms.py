from django import forms
from .models import User, PersonalUserInfo
from django.conf import settings

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Login или E-Mail', 'style': 'width:100%;'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'username': 'Login'}
        
        widgets = {
            'username': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
            'email': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
            'first_name': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
            'last_name': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
        }
    
    password = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput(
        attrs={'class': "standart_form--input"}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': "standart_form--input"}))


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match!')
        return cd['password2']




class RegistrationPersonalUserInfo(forms.ModelForm):
    class Meta:
        model = PersonalUserInfo
        fields = ('radio_chanal', 'radio_room', 'working_position', 'user_birthday', 'user_telephone')

        widgets = {
            'radio_chanal': forms.Select(attrs={'class': "standart_form--select"}),
            'radio_room': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
            'working_position': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
            'user_birthday': forms.DateInput(attrs={'class': "standart_form--input", 'type': "date"}),
            'user_telephone': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
        }



class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

        widgets = {
        # attrs = {'class': 'form-control'}
           'username': forms.TextInput(attrs={'hidden': 'true',}),
           'email': forms.EmailInput(attrs={'class': 'form-control mt-1 mb-1'}),
           'first_name': forms.TextInput(attrs={'class': 'form-control mt-1 mb-1'}),
           'last_name': forms.TextInput(attrs={'class': 'form-control mt-1 mb-1'}),
        } 



class EditPersonalInfo(forms.ModelForm):
    class Meta:
        model = PersonalUserInfo
        fields = ('avatara', 'radio_chanal', 'radio_room', 'working_position', 'user_birthday', 'user_telephone', 'user_about')

        widgets = {
            # 'avatara': forms.FileInput(attrs={'class':"sss", 'style':'position: absolute; top: 78%; left: 16%;', 'value': "Изменить"}),
            'user_about': forms.Textarea(attrs={'cols': '70', 'rows': '5', 'hidden': 'true', 'class': 'form-control mt-1 mb-1'}),
            'user_birthday': forms.DateInput(attrs={'type': 'date', 'style': 'text-align: end;', 'class': 'form-control mt-1 mb-1'}),
            'radio_chanal': forms.Select(attrs={'class': 'form-control mt-1 mb-1'}),
            'radio_room': forms.TextInput(attrs={'class': 'form-control mt-1 mb-1', 'style': 'text-align: end;', 'size': '4'}),
            'working_position': forms.TextInput(attrs={'class': 'form-control mt-1 mb-1'}),
            'user_telephone': forms.TextInput(attrs={'class': 'form-control mt-1 mb-1'}),
        }
