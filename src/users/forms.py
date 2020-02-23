from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'firstname',
            'lastname',
            'email',
            'password',
            'group'
        ]

class RawUserForm(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    group=forms.DecimalField()
