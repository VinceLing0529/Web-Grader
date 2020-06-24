from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=10,unique=True)
    password = models.CharField(max_length=10)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to ='profile_pics',blank=True)

    def _str_(self):
        return self.user.username
