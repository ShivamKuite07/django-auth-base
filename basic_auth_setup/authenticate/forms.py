from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your name',
        'class': '',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email address',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password again',
    }))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return password2  # Even though it doesn't save, it returns for validation




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your name',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
    }))

