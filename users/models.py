from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Roles(models.Model):
    role_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.role_name


class Users(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255)
    id_role = models.ForeignKey(
        Roles, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    def __str__(self):
        return f"{self.name} {self.surname} ({self.username})"
