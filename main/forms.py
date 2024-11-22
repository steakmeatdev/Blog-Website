# Registartion forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):

    # I had to manually create this because it doesn't come by default with UserCreationForm.
    email = forms.EmailField(required=True)

    # I can add as many fields as I want, just have to make them and make sure I can add them to User model.

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]