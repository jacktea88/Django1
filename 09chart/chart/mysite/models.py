from django.db import models
from django.contrib import auth

class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# create user profile
class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField()

    def __str__(self):
        return self.user.username


# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length=20)
    no = models.IntegerField()
    sex = models.BooleanField(default=False)
    byear = models.IntegerField()
    party = models.CharField(max_length=20)
    votes = models.IntegerField()
    
    def __str__(self):
        return self.name

# 建立溫度紀錄資料表
class Temperature(models.Model):
     temperature = models.DecimalField(max_digits=5, decimal_places=1)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return str(self.temperature)   