from django.db import models

# Create your models here.
class user(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.BigIntegerField()

class hexauser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.BigIntegerField()
    mobile=models.BigIntegerField()