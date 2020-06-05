from django.db import models

# Create your models here.
class student(models.Model):

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=10,unique=True)
    password = models.CharField(max_length=10)
