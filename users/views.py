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
    TaskCreationForm,
    TaskProcessingForm
)
from .models import Profile,User,Group,UserGroup,Projet,Task,Processing
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
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request,'Please enter the right information')
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
        else:
            messages.error(request,'You are not an administration, Contact your supervisor')
    context={}

    return render(request,'administration.html',context)


#### Admin homepage ####
def user_admin_panel(request):
    if request.method=="POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==False:
            return redirect("/login/")
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
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please enter the right information')
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
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
            if form.is_valid():
                user1=Profile.objects.get(id=request.user.id)
                group=Group(nameGroup=form.cleaned_data.get('nameGroup'),idProfile_id=user1.id)
                group.save()
                user_group=UserGroup(id_group_id=group.id,id_user_id=user1.id)
                user_group.save()
                messages.success(request, 'Your group has been created!')
                return redirect('/group/')
        else:
            return redirect("/login/")

    else:
        profile=Profile.objects.get(user=request.user.id)
        form=GroupCreationForm()

    return render(request,'group-create.html',locals())


#### Available group list
@login_required
def group_list_view(request):
    user=request.user.id
    admin=Profile.objects.get(user_id=user)
    if admin.isadmin==True:
        group=Group.objects.all()
    else:
        return redirect("/login/")

    return render(request,'group_list.html',locals())


#### Group page for adding new member ####
@login_required
def add_member_view(request,id):
    obj=get_object_or_404(Group,id=id)
    context={
        "object":obj
    }
    if request.method=="POST":
        user1=request.user.id
        admin=Profile.objects.get(user_id=user1)
        if admin.isadmin==True:
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
                    return redirect("/group/")
        else:
            return redirect("/login/")
    #group=Group.objects.all().values('nameGroup')
    else:
        form=GroupAddUserForm()

    return render(request,'group.html',locals())


####  Member list of a group view  ####
@login_required
def group_member_view(request,id):
    user=request.user.id
    admin=Profile.objects.get(user_id=user)
    if admin.isadmin==True:
        profilelist=[]
        name_group=Group.objects.get(id=id)
        memberlist=UserGroup.objects.filter(id_group_id=name_group.id)
        for member in memberlist:
            profil=Profile.objects.get(id=member.id_user_id)
            profilelist.append(profil)
    else:
        return redirect("/login/")

    return render(request,'group_member.html',locals())


####  Creat projet view ####
@login_required
def projet_creat_view(request,id):
    if request.method=="POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
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
            return redirect("/login/")
    else:
        form=ProjetCreationForm()

    return render(request,'projet_creat.html',locals())


#### Creat a task for a projet ####
@login_required
def task_creat_view(request,id):
    if request.method=="POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
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
            return redirect("/login/")
    else:
        form=TaskCreationForm()

    return render(request,'task_creat.html',locals())


#### Visualise task view ####
@login_required
def task_list_view(request,id):
    if request.method == "POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
            tasklist=[]
    #processinglist=[]
            task_group=Task.objects.filter(id_group_id=id)
            for tsk in task_group:
                task=Task.objects.get(id=tsk.id)
                #processing=Processing.objects.get(id_user_task_id=tsk.id)
                tasklist.append(task)
        else:
            return redirect("/login/")
    return render(request,'task_list.html',locals())


#### Visualise processing view ####
@login_required
def task_prosessing_view(request,id):
    if request.method == "POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
            processinglist=[]
            tasklist=Task.objects.filter(id_group_id=id)
            taskname=[]
            for tsk in tasklist:
                processing=Processing.objects.get(id_user_task_id=tsk.id)
                name=Task.objects.get(id=tsk.id)
                taskname.append(name)
                if processing is not None:
                    processinglist.append(processing)
        else:
            return redirect("/login/")
    return render(request,'task_processing.html',locals())



#### User visualise group view ####
@login_required
def user_group_view(request):
    grouplist=[]
    current_user=request.user
    user_profile=Profile.objects.get(user_id=current_user.id)
    user_group=UserGroup.objects.filter(id_user_id=user_profile.id)
    for grp in user_group:
        group=Group.objects.get(id=grp.id_group_id)
        grouplist.append(group)

    return render(request,'user_group.html',locals())


#### User list of task per group ####
@login_required
def user_list_task(request,idP):
    task_list=[]
    current_user=request.user
    user_profile=Profile.objects.get(user_id=current_user.id)
    user_task=Task.objects.filter(id_employee_id=user_profile.id)
    for tsk in user_task:
        if(tsk.id_group_id==idP):
            task_list.append(tsk)

    return render(request,'user_task.html',locals())



#### User update task view ####
@login_required
def user_processing_view(request,idT):
    if request.method=="POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
            form=TaskProcessingForm(request.POST)
            if form.is_valid():
                current_user=request.user
                user_profile=Profile.objects.get(user_id=current_user.id)
                finished=form.cleaned_data.get('is_finished')
                summary=form.cleaned_data.get('summary')
                processing=Processing(is_finished=finished,summary=summary,id_user_id=user_profile.id,id_user_task_id=idT)
                processing.save()
                messages.success(request,f'Information saved !')
                return redirect('/profile/group/')
                messages.success(request,"You processing has been updated")
            else:
                messages.error(request,"Please fill all the information ")
        else:
            return redirect("/login/")
    else:
        form=TaskProcessingForm(request.POST)

    return render(request,'user_processing.html',locals())


#### Group Delete view ####
@login_required
def group_delete_view(request,idG):
    d_group=Group.objects.get(id=idG)
    user=request.user.id
    admin=Profile.objects.get(user_id=user)
    if admin.isadmin==True:
        d_group.delete()
        messages=messages.success(request,"Your group has been deleted")
        return redirect('/group/')
    else:
        return redirect("login")
    context = {
        "object": d_group
    }
    return render(request, "group_delete.html", context)

#### Member Delete view ####
@login_required
def member_delete_view(request,idG,idU):
    if request.method == "POST":
        user=request.user.id
        admin=Profile.objects.get(user_id=user)
        if admin.isadmin==True:
            member=UserGroup.objects.get(id_user_id=idU)
            member.delete()
            return redirect('/group/')
        else:
            return redirect("login")

    return render(request,"user_delete.html",locals())

@login_required
def user_project_view(request):
    projectlist=[]
    current_user=request.user
    profil=Profile.objects.get(user_id=current_user.id)
    user_group=UserGroup.objects.filter(id_user_id=profil.id)
    for grp in user_group:
        project=Projet.objects.get(group_projet_id=grp.id_group_id)
        projectlist.append(project)
    return render(request,'user_project.html',locals())
