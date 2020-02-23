from django.shortcuts import render
from .models import User
from .forms import UserForm,RawUserForm
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    #print(request.user)
    return render(request,"base.html",{}) #string of HTML code {} dictionnary


def user_creat_view(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UserForm()
    context={
    'form':form
    }
    return render(request,"register.html",context)

def user_login_view(request):
    pass
    return render(request,"login.html")
