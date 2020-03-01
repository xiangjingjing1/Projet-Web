from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,GroupCreationForm
from .models import Profile,User,Group,UserGroup
from django.contrib.auth import authenticate,login

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
            messages.success(request, f'Your account has been created! Your account has been updated!')
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

#### Group page ####
@login_required
def group_view(request):
    return render(request,'group.html')
