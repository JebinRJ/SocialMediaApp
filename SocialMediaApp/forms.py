from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class user(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter EmailAddress'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}), max_length='10')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Confirm Password'}), max_length='10')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']