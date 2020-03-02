from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages,auth
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    GroupCreationForm,
    GroupAddUserForm,
    ProjetCreationForm,
    TaskCreationForm
)
from .models import Profile,User,Group,UserGroup,Projet,Task
from django.contrib.auth import authenticate,login

#### Home page views ####
def home_view(request):
    return render(request,'home.html')

#### Register page ####
def user_creat_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

#### Admin login page ###
def user_admin_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        profile=Profile.objects.get(user=user)
        if user is not None and profile.isadmin==True:
            login(request,user)
            return redirect('/adminpanel/')
    context={}

    return render(request,'administration.html',context)

#### Admin homepage ####
def user_admin_panel(request):
    return render(request,'adminpanel.html')

#### User homepage ####
@login_required
def user_profile_view(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'index.html',context)

#### Creat group page ####
@login_required
def group_creat_view(request):
    if request.method=="POST":
        form=GroupCreationForm(request.POST)
        if form.is_valid():
            user1=Profile.objects.get(id=request.user.id)
            group=Group(nameGroup=form.cleaned_data.get('nameGroup'),idProfile_id=user1.id)
            group.save()
            user_group=UserGroup(id_group_id=group.id,id_user_id=user1.id)
            user_group.save()
            return redirect('/group/')

    else:
        profile=Profile.objects.get(user=request.user.id)
        form=GroupCreationForm()

    return render(request,'group-create.html',locals())

#### Available group list
@login_required
def group_list_view(request):
    group=Group.objects.all()
    context={
        "object":group
    }

    return render(request,'group_list.html',context)

#### Group page for adding new member ####
@login_required
def group_view(request,id):
    obj=get_object_or_404(Group,id=id)
    context={
        "object":obj
    }
    if request.method=="POST":
        form=GroupAddUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('nameUser')
            user=User.objects.get(username=username)
            profil=Profile.objects.get(user_id=user.id)
            if user is not None:
                usergroup=UserGroup(id_group_id=id,id_user_id=profil.id)
                usergroup.save()
                messages.success(request, f'New member has been add')
                return redirect('/group/')
            else:
                messages.error(request,"User doesn't exist ")
    #group=Group.objects.all().values('nameGroup')
    else:
        form=GroupAddUserForm()

    return render(request,'group.html',locals())

####  Member list of a group view  ####
def group_member_view(request,id):
    profilelist=[]
    name_group=Group.objects.get(id=id)
    memberlist=UserGroup.objects.filter(id_group_id=name_group.id)
    for member in memberlist:
        profil=Profile.objects.get(id=member.id_user_id)
        profilelist.append(profil.firstname)

    return render(request,'group_member.html',locals())

####  Creat projet view ####
def projet_creat_view(request,id):
    if request.method=="POST":
        form=ProjetCreationForm(request.POST)
        if form.is_valid():
            stardate=form.cleaned_data.get('starting_date')
            enddate=form.cleaned_data.get('ending_date')
            dscp=form.cleaned_data.get('description')
            namep=form.cleaned_data.get('name_projet')
            projet=Projet(group_projet_id=id,starting_date=stardate,ending_date=enddate,name_projet=namep)
            projet.save()
            messages.success(request,f'Projet created !')
            return redirect('/group/')
        else:
            messages.error(request,"Please fill all the information ")
    else:
        form=ProjetCreationForm()

    return render(request,'projet_creat.html',locals())

#### Creat a task for a projet ####
def task_creat_view(request,id):
    if request.method=="POST":
        form=TaskCreationForm(request.POST)
        if form.is_valid():
            stardate=form.cleaned_data.get('task_starting_date')
            enddate=form.cleaned_data.get('task_ending_date')
            dscp=form.cleaned_data.get('description_task')
            nametask=form.cleaned_data.get('name_task')
            nameuser=form.cleaned_data.get('name_user')
            user_profil=User.objects.get(username=nameuser)
            id_profil=Profile.objects.get(user_id=user_profil.id)
            task=Task(name_task=nametask,discription_task=dscp,task_start_date=stardate,task_end_date=enddate,id_employee_id=id_profil.id,id_group_id=id)
            task.save()
            messages.success(request,f'Task created !')
            return redirect('/group/')
        else:
            messages.error(request,"Please fill all the information ")
    else:
        form=TaskCreationForm()

    return render(request,'task_creat.html',locals())
