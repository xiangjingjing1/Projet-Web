from django.db import models

# Create your models here.
class User(models.Model):
    admin=models.BooleanField(default=False)
    firstname=models.CharField(max_length=128,unique=True)
    lastname=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=256)
    email=models.EmailField(max_length=245,unique=True)
    group=models.DecimalField(decimal_places=0,max_digits=10000)
