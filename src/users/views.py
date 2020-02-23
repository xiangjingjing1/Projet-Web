from django.shortcuts import render
from .models import User
from .forms import UserForm,RawUserForm
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    #print(request.user)
    return render(request,"base.html",{}) #string of HTML code {} dictionnary


def user_creat_view(request):
    user_form=RawUserForm(request.GET)
    if request.method=="POST":
        user_form=RawUserForm(request.POST)
        #Check all the data form
        if user_form.is_valid():
            print(user_form.cleaned_data)
            Product.objetcts.create(**user_form.cleaned_data)
        else:
            print(user_form.errors)

    context={
        "form":user_form
    }
    return render(request,"register.html",context)
