from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    position = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
