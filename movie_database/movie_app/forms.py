from django import forms
from .models import Movie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class userRegistration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


