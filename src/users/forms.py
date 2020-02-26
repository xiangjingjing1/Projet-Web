from django import forms

from .models import User,Group,Task,Projet,Processing

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'firstname',
            'lastname',
            'email',
            'password',
            'checkpassword'
        ]

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=[
            'namegrp'
        ]

class ProjetForm(forms.ModelForm):
    class Meta:
        fields=[
            'nameprj',
            'introduction',
            'workgroup',
            'starttime',
            'endtime'
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        fields=[
            'nametsk',
            'description',
            'startingdate',
            'endingdate'
        ]

class ProcessingForm(forms.ModelForm):
    class Meta:
        fields=[
            'done',
            'summery'
        ]

class RegisterForm(forms.Form):
    firstname=forms.CharField(label="firstname",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname=forms.CharField(label="lastname",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    checkpassword=forms.CharField(label="checkpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
