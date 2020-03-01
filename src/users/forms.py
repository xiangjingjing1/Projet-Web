from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Group,UserGroup

#from .models import User,Group,Task,Projet,Processing

####  Register form for user ####
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#### Update information form for user ####
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

#### Update user information form ####
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['firstname','lastname']

#### Create group form for administration ####
class GroupCreationForm(forms.ModelForm):
    nameGroup=forms.CharField(label="Group name")
    class Meta:
        model=Group
        fields=('nameGroup',)

#### Add user in group form ####
class GroupAddUserForm(forms.ModelForm):
    nameUser=forms.CharField(label="User name")
    class Meta:
        model=UserGroup
        fields=('nameUser',)
