from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Group,UserGroup,Projet,Task

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
        fields=['nameUser',]

#### Create projet form in administration panel ####
class ProjetCreationForm(forms.ModelForm):
    name_projet=forms.CharField(label="Projet name")
    description=forms.CharField(label="Description projet")
    starting_date=forms.DateField(label="Starting time",widget=forms.DateInput(attrs={'type':'date'}))
    ending_date=forms.DateField(label="Ending time",widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=Projet
        fields=['name_projet','description','starting_date','ending_date']

#### Create task for a projet form ####
class TaskCreationForm(forms.ModelForm):
    name_task=forms.CharField(label="Task name")
    description_task=forms.CharField(label="Description task")
    task_starting_date=forms.DateField(label="Starting time",widget=forms.DateInput(attrs={'type':'date'}))
    task_ending_date=forms.DateField(label="Ending time",widget=forms.DateInput(attrs={'type':'date'}))
    name_user=forms.CharField(label="Member username")
    class Meta:
        model=Task
        fields=['name_task','description_task','task_starting_date','task_ending_date','name_user']
