from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your usernmae',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Your Password',
        'class':'w-full px-6 py-4 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class':'w-full px-6 py-4 rounded-xl'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your usernmae',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Your Password',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
