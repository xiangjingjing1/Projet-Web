"""teamwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from users.views import (
    home_view,
    group_list_view,
    user_creat_view,
    user_profile_view,
    user_admin_view,
    user_admin_panel,
    group_creat_view,
    add_member_view,
    group_member_view,
    projet_creat_view,
    task_creat_view,
    task_list_view,
    user_group_view,
    user_list_task,
    user_processing_view,
    group_delete_view,
    task_prosessing_view,
    member_delete_view,
    user_project_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('register/',user_creat_view,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/',user_profile_view,name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('administration/',user_admin_view,name='administration'),
    path('adminpanel/',user_admin_panel,name='adminpanel'),
    path('group/creat/',group_creat_view,name='group_create'),
    path('group/',group_list_view,name='group_list'),
    path('group/<int:id>/',add_member_view,name='group'),
    path('group/member/<int:id>/',group_member_view,name='group_member'),
    path('group/projet/create/<int:id>/',projet_creat_view,name='projet_creat'),
    path('group/projet/task/create/<int:id>/',task_creat_view,name='task_creat'),
    path('group/projet/task/<int:id>/',task_list_view,name='task_list'),
    path('profile/group/',user_group_view,name='user_group'),
    path('profile/group/task/processing/<int:idT>/',user_processing_view,name='processing'),
    path('profile/group/task/<int:idP>/',user_list_task,name='user_list_task'),
    path('group/delete/<int:idG>/',group_delete_view,name='group_delete'),
    path('group/projet/processing/<int:id>/',task_prosessing_view,name='projet_processing'),
    path('group/member/delete/<int:idG>/<int:idU>/',member_delete_view,name='member_delete'),
    path('profile/project/',user_project_view,name='user_project')
]
