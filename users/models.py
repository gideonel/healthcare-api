from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
