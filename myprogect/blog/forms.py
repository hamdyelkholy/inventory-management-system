from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'tags']