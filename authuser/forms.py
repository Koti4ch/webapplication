from django import forms
from .models import User, PersonalUserInfo
from django.conf import settings

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Login or E-Mail', 'style':'width:100%;'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match!')
        return cd['password2']

class RegistrationPersonalUserInfo(forms.ModelForm):
    class Meta:
        model = PersonalUserInfo
        fields = ('avatara' ,'radio_chanal', 'radio_room', 'working_position', 'user_birthday', 'user_telephone')

        widgets = {
            'user_birthday': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Input your birthday'}),
        }



class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

        widgets = {
           'username': forms.TextInput(attrs={'hidden': 'true',}),
        } 



class EditPersonalInfo(forms.ModelForm):
    class Meta:
        model = PersonalUserInfo
        fields = ('avatara', 'radio_chanal', 'radio_room', 'working_position', 'user_birthday', 'user_telephone', 'user_about')

        widgets = {
            'user_about' : forms.Textarea(attrs={'cols': '70', 'rows': '5'}),
            'user_birthday': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Input your birthday'}),
            'user_about': forms.Textarea(attrs={'hidden':'true'}),
        }
