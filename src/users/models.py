from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=128)
    lastname=models.CharField(max_length=128)
    isadmin=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Profile'

class Group(models.Model):
    nameGroup = models.CharField(max_length=42, unique=True)
    idProfile = models.ForeignKey(Profile, on_delete=models.CASCADE, db_column='idemployee')

class UserGroup(models.Model):
    id_group=models.ForeignKey(Group,on_delete=models.CASCADE)
    id_user=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Projet(models.Model):
    group_projet=models.ForeignKey(Group,on_delete=models.CASCADE)
    starting_date=models.DateField(default=timezone.now)
    ending_date=models.DateField(default=timezone.now)
    name_projet=models.CharField(max_length=128)
    description=models.TextField(max_length=500)

class Task(models.Model):
    id_group=models.ForeignKey(Group,on_delete=models.CASCADE)
    id_employee=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name_task=models.CharField(max_length=128)
    discription_task=models.TextField(max_length=500)
    task_start_date=models.DateField(default=timezone.now)
    task_end_date=models.DateField(default=timezone.now)
