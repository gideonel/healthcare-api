from django.db import models
from django.db import models
from users.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100, blank=True)
    availability = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.specialty}"
