

from django.db import models


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    user_name=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=50,unique=True)
    profile_image=models.ImageField()
    date_joined=models.DateTimeField(auto_now_add=True,null=True)
    date_updated=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.email


