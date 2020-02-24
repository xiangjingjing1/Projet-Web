from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm,RegisterForm
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    #print(request.user)
    return render(request,"base.html",{}) #string of HTML code {} dictionnary


def user_creat_view(request):
    if request.method=="POST":
        form_regiseter=RegisterForm(request.POST or None)
        message="Please check the information that you enter"
        if form_regiseter.is_valid():
            firstname=form_regiseter.cleaned_data['firstname']
            lastname=form_regiseter.cleaned_data['lastname']
            email=form_regiseter.cleaned_data['email']
            password=form_regiseter.cleaned_data['password']
            checkpassword=form_regiseter.cleaned_data['checkpassword']
            group=form_regiseter.cleaned_data['group']
            if password != checkpassword:
                message="The password doesn't match"
                return render(request,'register.html',locals())
            else:
                same_email_user=User.objects.filter(email=email)
                if same_email_user:
                    message="This email has already exist!"
                    return render(request,'register.html',locals())

                #If all the data has being check
                new_user=User.objects.create(firstname=firstname
                ,lastname=lastname
                ,password=password
                ,email=email
                ,group=group)
                new_user.save()
                return redirect('/login/')

    form_regiseter=RegisterForm()
    return render(request,'register.html',locals())
    #form=UserForm(request.POST or None)
    #if form.is_valid():
    #    form.save()
    #    form=UserForm()
    #context={
    #'form':form
    #}
    #return render(request,"register.html",context)

def user_login_view(request):
    if request.method=="POST":
        useremail=request.POST.get('useremail',None)
        password=request.POST.get('password',None)
        message="All fields must be completed"
        #The username and password can't be Null
        if useremail and password:
            useremail=useremail.strip()
            try:
                user=User.objects.get(email=useremail)
                if user.password==password:
                    return redirect('/index/')
                else:
                    message="Wrong password"
            except:
                message="The user is not exist"
        return render(request,"login.html",{"message":message})
    return render(request,'login.html')

def user_index_view(request):
    pass
    return render(request,'index.html')
