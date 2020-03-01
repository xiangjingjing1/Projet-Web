from django.contrib import admin

# Register your models here.
#from .models import User,Group,Projet,Task,Processing,Worker

#admin.site.register(User)
from django.contrib import admin
from .models import Profile,Group,UserGroup

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(UserGroup)
