from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control p_input',
                'placeholder': 'Username',
                'id': "uname",
            }
        )
    )
    
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control p_input',
                'placeholder': 'Password',
                'id': 'pass'
            }
        )
    )
    class Meta:
        model = User
        fields = ('password', 'username')


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': "uname",
            }
        )
    )
    
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'pass'
            }
        )
    )
    
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'pass2'
            }
        )
    )
    check = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "id": 'check',
                'class': 'form-check-input form-check-secondary'
            }
        )
    )
    
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'check',)