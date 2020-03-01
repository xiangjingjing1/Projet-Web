from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Group

#from .models import User,Group,Task,Projet,Processing

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['firstname','lastname']

class GroupCreationForm(forms.ModelForm):
    nameGroup=forms.CharField(label="Name Group")
    class Meta:
        model=Group
        fields=('nameGroup',)
