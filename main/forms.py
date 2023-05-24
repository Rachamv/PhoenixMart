from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from .models import UserProfile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Full Name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    # Additional fields for UserProfile
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter your bio',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'avatar', 'bio')
