from django.contrib import admin

# Register your models here.
from .models import User,Group,Projet,Task,Processing,Worker

admin.site.register(User)
