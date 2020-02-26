from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    admin=models.BooleanField(default=False)
    firstname=models.CharField(max_length=128)
    lastname=models.CharField(max_length=128)
    password=models.CharField(max_length=256)
    checkpassword=models.CharField(max_length=256)
    email=models.EmailField(max_length=245,unique=True)


class Group(models.Model):
    namegrp=models.CharField(max_length=128,unique=True)
    members = models.ForeignKey(User, on_delete=models.CASCADE)


class Projet(models.Model):
    nameprj=models.CharField(max_length=128,unique=True)
    introduction=models.TextField(blank=True,null=True)
    workgroup=models.ForeignKey(Group,on_delete=models.CASCADE)
    starttime=models.DateTimeField(default=timezone.now)
    endtime=models.DateTimeField(default=timezone.now)


class Worker(models.Model):
    worker=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE) #If delate this data delate the related data too
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE)


class Task(models.Model):
    nametsk=models.CharField(max_length=128)
    description=models.TextField(blank=True,null=True)
    startingdate=models.DateTimeField(default=timezone.now)
    endingdate=models.DateTimeField(default=timezone.now)
    idprojet=models.ForeignKey(Projet,on_delete=models.CASCADE)


class Processing(models.Model):
    idtask=models.ForeignKey(Task,on_delete=models.CASCADE)
    done=models.BooleanField(default=False)
    summery=models.TextField(blank=True,null=True)
