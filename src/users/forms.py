from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'firstname',
            'lastname',
            'group'
        ]

class RawUserForm(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    #email=forms.EmailField()
    group=forms.DecimalField()
