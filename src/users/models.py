from django.db import models
from django.contrib.auth.models import User


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
